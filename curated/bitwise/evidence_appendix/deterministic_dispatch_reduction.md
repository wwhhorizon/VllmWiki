# Deterministic Dispatch 与 Reduction Control Evidence Appendix

状态：curated public evidence summary。

父页：[../deterministic_dispatch_reduction.md](../deterministic_dispatch_reduction.md)。

本文保存公开可追溯的长证据摘要、case 表格、验证矩阵和补证记录。它来自机制页重构前的详细结论层文本，不包含本地 raw evidence 全文。

## 问题定义

deterministic mode 必须控制 kernel/backend dispatch 和 reduction geometry。只设置随机种子不够；如果 dispatcher 仍可选择不同 autotune candidate、split-K、atomic reduction、backend fallback 或 warmup 状态，输出仍可能变化。

## 典型触发条件

- autotuner 在数值不等价 candidate 中选择。
- split-K 或 atomic reduction 改变浮点累加顺序。
- fast kernel 使用非 bitwise stable reduction。
- 首次请求触发 JIT、CUDA graph capture 或 allocator/cache warmup。
- hardware-specific dispatcher 从 CSV/heuristic 中选出不同策略。
- backend selector 把已知 bad shape 路由到 native special kernel，而不是已有的更稳定 fallback。
- batch-invariant mode 声明支持某 backend，但内部仍可选择 batch-dependent 2D/3D kernel、split count 或 fused quant path。
- `torch.compile` / cuBLAS 路径没有关闭 batch-size-sensitive reduced-precision reduction 或 split-K 行为。
- attention metadata builder 使用 model-wide head count 做 plan/scratch allocation，但 runtime kernel 使用 per-layer Q-head 数。

## 代表证据

| Source | 证据事实 | 炼化结论 |
| --- | --- | --- |
| [#25194](https://github.com/vllm-project/vllm/issues/25194), [#25197](https://github.com/vllm-project/vllm/pull/25197) | Triton `_chunk_cumsum_fwd_kernel` 中 `BLOCK_H=1` 与 `BLOCK_H>1` 输出不同；PR 直接移除 `BLOCK_H=1` autotune config。 | autotune candidate 必须先证明数值等价，不能只按速度进入候选集。 |
| [#35183](https://github.com/vllm-project/vllm/pull/35183) | ROCm skinny GEMM 拆成 deterministic store-then-reduce 与 fast `atomicAdd` path，默认 deterministic，fast path 需显式 opt-in。 | deterministic 与 fast path 应拆开，而不是用同一个 kernel 隐式切换。 |
| [#34878](https://github.com/vllm-project/vllm/pull/34878) | ROCm beam search test 因 batch-size-dependent FP reduction 失败：Triton attention、hipBLAS/rocBLAS GEMM 和 skinny GEMM 的 reduction order 随 M 维改变，同一 logits row 的 `1e-5` 级 logprob 差异足以翻转 beam ranking。merged PR 在 ROCm 上显式设置 `async_scheduling=False`、`enforce_eager=True`、`enable_prefix_caching=False`、`max_num_seqs=1`，并把 `VLLM_ROCM_USE_SKINNY_GEMM=0` 写进测试，非 ROCm 不变。 | 有些 bitwise 修复是 verification-harness boundary：为了测试 beam search 语义，需要固定 batch composition、graph padding、prefix side effect 和 GEMM path，避免测试本身被 backend drift 污染。 |
| [#25404](https://github.com/vllm-project/vllm/issues/25404), [#25603](https://github.com/vllm-project/vllm/pull/25603) | `#25404` 提出 per-kernel deterministic override；merged PR `#25603` 实际落地为第一批 batch-invariant plumbing：C++ `batch_invariant.hpp` env hook、Python `batch_invariant.py`、GPU runner 初始化、layernorm/fused quant/topk softmax/flex attention 的 batch-invariant branch，以及 `tests/v1/generation/test_batch_invariance.py`。PR 测试显示没有 override 时 batch-size 64 的 5 次试验中 2 次输出偏离 batch=1，logprob test 也出现 `torch.equal` 失败；启用 `VLLM_KERNEL_OVERRIDE_BATCH_INVARIANT=1` 后通过。review 后把命名从 deterministic 调整为 batch invariant，并接受全局 env hook 作为当前 plumbing。 | 真实落地不是完整 per-kernel 配置系统，而是 batch-invariant mode 的全局开关与首批 kernel override；它提供后续 determinism 工作的接入点，但不能宣称所有 kernel 已被覆盖。 |
| [#27660](https://github.com/vllm-project/vllm/pull/27660) | merged PR 让 batch-invariant mode 不再简单强制 `enforce_eager`，而是为 `torch.compile` 路径补 cuBLAS 控制：关闭 FP16/BF16 reduced-precision reduction，优先 `cublaslt`，在 PyTorch 2.9 及更早版本通过 `CUBLAS_WORKSPACE_CONFIG` / `CUBLASLT_WORKSPACE_SIZE` 降低 batch-size-sensitive 行为；同时在 BI mode 下关闭 vLLM AOT compile，避免尚未验证的组合。review 还修正了 PyTorch 2.9 boolean flag 与 2.10.dev tuple flag 的版本边界，并把 DeepGEMM support 查询提前，避免 Dynamo trace 进入 runtime capability check。DeepSeek V3.1 + FlashAttention MLA 的 logprob batch-invariance test 通过，并有多 `max_model_len` / batch size 的 Inductor reduction kernel经验验证。 | `torch.compile` 不是天然不 deterministic，也不是可以无条件开启；关键是把 cuBLAS/reduced-precision/split-K 和 Dynamo trace side effect 写入 deterministic contract。AOT compile 仍是边界，PyTorch 版本能力也必须显式声明。 |
| [#41651](https://github.com/vllm-project/vllm/issues/41651), [#42650](https://github.com/vllm-project/vllm/pull/42650) | Laguna XS.2 FP8 在 sm120 上出现 FlashInfer random output；评论进一步确认 TRITON_ATTN 也受两个独立 bug 影响。merged PR #42650 定位其中一个根因：FlashInfer/Triton metadata builder 用 `model_config.get_num_attention_heads()` 的 model-wide 48 做 plan/scratch allocation，但该模型某些 layer 的 runtime `q.shape[1]` 是 64。FlashInfer plan-time tile budget 少 25%，tail rows 返回 zero 并污染 next-token logits；Triton 预分配 `softmax_segm_*` scratch 为 48 heads，kernel 按 64 heads 写越界并可能破坏 `slot_mapping`。patch 改为从 served `Attention` layer 的 `impl.num_heads` 读取 per-layer/per-TP-rank Q-head，并断言同一 attention group 内一致。 | backend metadata 也是 dispatch contract：plan-time allocation、scratch shape 和 runtime kernel shape 必须来自同一个 per-layer source of truth。 |
| [#33688](https://github.com/vllm-project/vllm/pull/33688) | `TRITON_ATTN` 原本在 decode 时可走 3D Triton unified attention；merged patch 将其列为 decode-invariant backend，并在 `VLLM_BATCH_INVARIANT=1` 时强制 2D kernel。before/after logprob test 显示 128/128 prompts fail 到通过。 | 对 attention backend 的 BI 支持，要固定 kernel family，而不是只允许 backend 名称进入 supported list。 |
| [#40408](https://github.com/vllm-project/vllm/pull/40408) | Cutlass FP8 path 原本在 BI mode 下倾向 dequant 到 BF16；merged PR 为 sm89/sm90/sm100/sm120 增加 batch-invariant Cutlass FP8 dispatch，并在 FP8 quant layer 中优先 direct FP8 path。review 明确追问 Cutlass 是否真的 batch invariant，作者补充 test 覆盖不同 M；patch 注释要求 CUTLASS config independent of M。 | fast direct FP8 path 可以进入 BI，但前提是 kernel config 不随 batch M 维调参；一旦 tuning 重新依赖 M，这个结论要重新审。 |

## 根因机制

这类问题来自“可变但未被 deterministic contract 管住”的执行路径。dispatcher、autotuner、CSV heuristic 或 graph warmup 为了性能选择不同 kernel；这些 kernel 在数学上近似等价，但在浮点累加顺序、atomic interleaving 或低精度 rounding 上不 bitwise 等价。

`#25603` 还澄清了一个命名边界：batch invariant 比普通 deterministic 更严格。只要其中一个 op 仍随 batch shape 改变输出，整条 serving path 就不再 batch invariant；因此 review 最终倾向于全局 batch-invariant mode，而不是让用户以为可以随意混搭 per-kernel deterministic/variant 状态。

`#34878` 则展示了测试环境本身也需要 deterministic contract。beam search 的目标是比较候选序列排名，若 ROCm backend 在不同 batch/concurrency 下改变 logits M 维 reduction order，测试看到的 failure 可能来自 harness geometry，而不是 beam search 逻辑。此类修复要写成 test placement / engine-config boundary。

`#39849` 展示了 dispatch 层的另一种修复：当 native backend 的某些 hardware/shape specialization 已知有数值或稳定性问题时，deterministic contract 可以先通过 selector 把这些 shape 路由到已有 fallback。这个动作本身是 support gate/workaround，不等于 native ROCM_ATTN `mfma4` kernel 已经修好。

`#33688/#40408` 则说明 deterministic path 不必永远是“慢路径”。只要 backend 能证明自己的 kernel family 和 config 不再随 batch composition 改变，就可以把更快的 TRITON_ATTN 2D path 或 Cutlass FP8 direct path纳入 BI mode。关键不是快慢，而是 dispatch 条件是否可证明稳定。

`#27660` 进一步说明 compile path 的判断不能停留在“compile/eager 二选一”。Inductor 生成的 reduction kernel 如果 thread layout 固定并用 mask 处理边界，可以比 eager custom op 更容易保持 batch invariant；真正需要管住的是 cuBLAS 层的 reduced-precision reduction、split-K、workspace/algorithm 选择，以及 Dynamo trace 过程中不应执行的 runtime capability query。

`#42650` 则把 metadata builder 也拉进 deterministic/dispatch contract。FlashInfer plan 和 Triton scratch buffer 都在 kernel launch 前根据 metadata 分配资源；如果 metadata 用的是 model-wide head count，而 runtime tensor 用 per-layer head count，后续即使 kernel 本身 deterministic，也是在错误的 buffer/tile geometry 上 deterministic。

## Source-Adjacent 摘要

- `#42240` 的 patch 重点不是“证明 AITER 所有 block-scaled FP8 linear 都 deterministic”，而是把已知不稳定的 CK/CK-Tile split-K reduction 从可选 dispatch 中机械移除：当前证据显示 patch 同时在 `can_implement` 和 call-site guard 上把范围收敛到 `128x128` weight group shape，并强制 `splitK=0`，因此它更像一个 scoped workaround，而不是 kernel 根因修复。
- `#42240` 的 review 也说明这类 workaround 的 closure 条件很具体：只要上游 AITER 还没有 accepted 的 deterministic split-K 修复，vLLM 侧就不能把这条路径重新包装成“通用 deterministic support”，更不能再留一个生产 opt-out 让用户回到已知不稳定 reduction。
- `#39849` 则把“修 kernel”换成“改 selector”：当前 patch 的核心是把 gfx9 上 `gqa_ratio=2/4` 的 native ROCM_ATTN `mfma4` path 路由到 fallback backend，以绕开 issue `#35569` 里已经观察到的 reranker score drift。这个 changed-files 方向能证明 dispatch workaround 存在，但还不能替代 patched e2e numeric regression。
- `#39849` 的证据边界也因此很明确：selector 单测最多证明 known-bad shape 被改道，不能证明 Qwen3-VL reranker 分数已经恢复，更不能证明 gqa_ratio 2/4 之外的 shape 没有被误路由。只要这两类证据缺一，wiki 就应继续把它写成 selector fallback/workaround。

## 修复方式

1. 枚举 deterministic mode 下所有可变 dispatch 点。
2. 移除数值不等价 autotune candidate，或把它们降为 fast opt-in path。
3. 固定 reduction geometry：split-K、block size、atomic path、store-then-reduce。
4. 为 kernel 提供 deterministic override，而不是让全局开关停留在调度层。
5. 文档中写清 deterministic path 的性能代价和 hardware/backend 边界。
6. 对 workaround 型 fix，显式写清它绕过了哪个 dispatcher/上游 bug，以及哪些 shape/group-size 才允许调用。
7. 去掉 deterministic workaround 的环境变量反向开关：如果生产路径没有合法理由回到非确定 split-K，就不应保留 opt-out 让用户重新进入不稳定 kernel。
8. 对 batch-invariant plumbing，区分“全局 mode 可接入”和“某个 kernel 已实际覆盖”；新增 hook 不能替代逐 kernel 的 exact/logprob 验证。
9. 对 backend-specific workaround，明确列出 hardware family、head size、GQA ratio、selected backend 和 fallback backend；不要把 selector fallback 写成 kernel 根因修复。
10. 对 fast path 重新纳入 BI mode，必须证明 config 与 batch M 维无关，或把所有会随 M 变化的选择固定下来。
11. 对 `torch.compile` 路径，显式设置 cuBLAS reduced-precision 与 workspace 策略；对 PyTorch 版本差异做 guard，并把 AOT compile、Dynamo trace side effect 和 runtime capability query 拆开处理。
12. 对 metadata builder，所有 plan-time head count、scratch shape、tile budget 必须从实际 served layer 或 runtime tensor 的同一语义来源派生；同一 attention group 内若 head count 不一致，应在分组层拆开或显式报错。

## 验证契约

- 对同一输入 back-to-back 调用 kernel，要求 bit-identical 或明确 strict tolerance。
- 对 serving path 覆盖首次请求、warmup 后请求、CUDA graph capture 前后。
- fast opt-in path 不能借用 deterministic path 的 correctness claim。
- 对 split-K/atomic 修复，要记录 hardware、dtype、backend、kernel config、weight group shape 和 dispatcher source。
- 对 batch-invariant override，要同时比较输出 token 和 logprob bit equality；只比较生成文本可能漏掉排名边界的数值漂移。
- 对 beam search / ranking 测试，要检查 logprob ranking 是否被 `1e-5` 级差异翻转；测试 harness 必须固定 batch size、async scheduling、graph padding和 backend kernel path。
- 对 backend score drift，要同时做 selector 单测和模型级 numeric regression；selector 单测只能证明 bad shape 被绕开，不能证明下游分数偏差已消失。
- 对 backend enablement，至少要有 before/after logprob/token test；对于 Cutlass/GEMM fast path，还要做多 batch size/M 维的固定 config test。
- 对 compile path，至少覆盖多 `max_model_len`、多 batch size、目标大模型、目标 attention backend，并记录是否启用了 AOT compile、DeepGEMM/FP8 path、PyTorch 版本和 cuBLAS flags。
- 对 attention metadata，覆盖非均匀 per-layer Q-head 模型、FlashInfer/Triton 两个 metadata builder、FP8 KV、CUDA graphs/compile，以及 plan-time allocation 与 runtime `q.shape[1]` 一致性。

### Dispatch / Reduction 最小验证矩阵

| Source | 保护对象 | 最小验证矩阵 | 合格契约 | 不能被什么替代 |
| --- | --- | --- | --- | --- |
| [#42240](https://github.com/vllm-project/vllm/pull/42240) | AITER block-scaled FP8 linear 的 split-K / reduction geometry | target hardware、patched/unpatched 对照、`128x128` weight group shape、`splitK=0` 命中、相邻 shape negative check、上游 AITER 未修复前的 deterministic path 固定 | token/logprob 不漂移，且 dispatcher 不再把受影响 shape 送回 split-K path | 只看 PR body；只测单一 happy-path shape；把 open workaround 当根因修复 |
| [#39849](https://github.com/vllm-project/vllm/pull/39849), [#35569](https://github.com/vllm-project/vllm/issues/35569) | ROCM_ATTN known-bad shape 的 selector fallback 与下游 score 稳定性 | gfx9、`gqa_ratio=2/4`、patched/unpatched route compare、selector unit test、Qwen3-VL reranker patched e2e score regression、邻近 shape 不误路由 | bad shape 被稳定路由到 fallback，且 score drift 不再复现 | 只有 selector mock；只有 backend route 改变；没有 patched 模型级 numeric regression |

## 适用边界

- [#42240](https://github.com/vllm-project/vllm/pull/42240) 是 scoped workaround：强制 `splitK=0` 绕过 CK/CK-Tile reduction 问题，直到上游修复；当前 patch 只允许 128x128 weight group shape，不能外推为所有 AITER block-scaled shape 都安全。
- [#35183](https://github.com/vllm-project/vllm/pull/35183) 的 fast path 是显式性能取舍，不应默认承诺 bitwise stability。
- [#34878](https://github.com/vllm-project/vllm/pull/34878) 是 ROCm test-harness 修复，不等于生产服务默认关闭所有 batch-size-sensitive ROCm kernel；它证明 beam-search 测试需要固定几何，不证明所有 ROCm serving path 已 bitwise。
- [#25603](https://github.com/vllm-project/vllm/pull/25603) 已 merged，但它只是第一批 batch-invariant override plumbing；review 中仍保留 envvar 性能/可维护性讨论，且 coverage 只包括当时 patch touched 的 kernels，不代表全 vLLM serving path 已 batch invariant。
- [#27660](https://github.com/vllm-project/vllm/pull/27660) 已 merged，结论覆盖 batch-invariant mode 与 `torch.compile`/cuBLAS 控制的组合；它不等于所有 AOT compile 或所有 Dynamo-traced runtime check 都安全。PR 中仍明确把 `VLLM_USE_AOT_COMPILE` 在 BI mode 下关掉，并且 PyTorch 2.9 与 2.10.dev 的 flag 类型不同。
- [#33537](https://github.com/vllm-project/vllm/pull/33537) 仍 open/stale；现有 evidence 主要是 warmup 框架和首请求 latency 稳定性，不足以当作 token/logprob bitwise 修复。它只算 verification boundary，不是主机制。
- [#39849](https://github.com/vllm-project/vllm/pull/39849) 仍 open/unmerged；它只覆盖 gfx9 上 `gqa_ratio=2/4` 的 ROCM_ATTN native `mfma4` path，并没有证明所有 ROCM_ATTN score drift、所有 head size、或 Qwen3-VL reranker e2e deviation 都已修复。
- [#42650](https://github.com/vllm-project/vllm/pull/42650) 已 merged，但它只覆盖 metadata head-count source；`#41651` 评论明确还提到独立的 Triton FP8 `k_scale/v_scale` 问题（#42580），因此不能写成 TRITON_ATTN FP8 KV 全部由该 PR 修复。后续评论还暴露 Gemma4 MTP target/draft Q-head 混入同一 attention group 的断言风险，说明 grouping key 仍需后续处理。（补充：`#42580` 已于 2026-05-21 被作者主动关闭，原因是 concurrent fix [#42080](https://github.com/vllm-project/vllm/pull/42080) 已于 2026-05-19 合并，该 PR 为 Triton attention backend 添加了 FP8 per-tensor Q scale 支持；因此 TRITON_ATTN FP8 `k_scale/v_scale` 边界应重新定位为“已由 `#42080` 收口”，而不是“仍需单独追踪 `#42580`”。）
- [#30018](https://github.com/vllm-project/vllm/pull/30018) 的 FA2 support 是 merged，LoRA 有测试/review 支持但 landed-code 子路径仍需补证；本地证据明确标注不支持 CUDA graph，CUDA graph 下 `max_num_splits` 与 metadata 仍需独立闭环。
- [#40408](https://github.com/vllm-project/vllm/pull/40408) 的 Cutlass FP8 direct path 已 merged；边界是当前测试覆盖的 sm89/sm90/sm100/sm120 config 和 M 维矩阵。review 提醒“如果 tuning 改变，该性质可能消失”，所以后续 tuning PR 需要重新跑 BI test。
- 与 batch invariance 页交叉：当 batch 改变触发不同 dispatch/reduction，最终归因应落到本机制。

- [#44115](https://github.com/vllm-project/vllm/pull/44115) 是 open PR（1 comment、0 review comments、1 changed file），揭示 FlashInfer MoE kernels 在 CUDA graph capture 时 bypass 了 device cache capture，导致 internal-router/capture mismatch。在 GB200 上 TRTLLM 路径输出全零，而 Triton 路径有真实 routing。修复方向是让 routed_experts fall back 到 Triton MoE backend 作为 interim guardrail。这和 `#39849`（selector fallback）和 `#42670`（support-gate workaround）是同类 dispatch fallback 模式，但根因是 CUDA graph capture 与 FlashInfer internal router 的不兼容。PR 仍 open/unmerged，不能写成 landed fix。

## 仍需补证

- 继续复核 `kernel_autotune_reduction` cluster 中只被 benchmark 证明、但没有 exact/token equality 证明的 fast path。
- 补充 `#35183` deterministic/fast path 的性能边界和 opt-in 文档证据。
- 补充 `#25603` 后续 PR 是否继续把更多 kernels 接入 `VLLM_BATCH_INVARIANT`；特别检查 review comment 中提到的 multidim `torch.sum`/mean 是否已替换为 deterministic reduction。
- 后续追踪 `torch.compile`/AOT compile 与 batch-invariant mode 的组合：如果 AOT compile 重新开启，必须补独立 logprob/token equality 和 Dynamo trace safety evidence。
- 若继续保留 `#33537`，需要找到 first-request token/logprob divergence 的直接复现；否则只把它维护为 latency/warmup boundary。
- 继续追踪 `#42240` 是否转为 ready/merged，以及上游 AITER 是否有对应 deterministic split-K 修复；只有上游闭环后才可把 vLLM workaround 视为可移除。
- 追踪 `#39849` 是否合并；若继续推进，需要补 Qwen3-VL reranker patched e2e score regression，并确认 gqa_ratio 2/4 以外 shape 没有被误路由或遗漏。
- 追踪 FA2 CUDA graph BI 支持、LoRA landed-code split-K 子路径、TRITON_ATTN 更多 variant，以及 Cutlass FP8 后续 tuning 是否仍保持 config independent of M。
- 追踪 `#42650` 后续是否修复 Gemma4 MTP grouping key，让 target/draft 不同 Q-head 的 layers 不再进入同一个 attention group；`#42580` 已于 2026-05-21 被作者关闭（被已合并的 `#42080` 替代），不再单独追踪；后续只在 TRITON_ATTN FP8 scale 出现新复现时才重新升回复核。
- 追踪 #44115 是否合并或转为 RFC #39701 的 native capture 路径；若合并，验证 routed_experts capture 是否在 FlashInfer TRTLLM/CUTLASS 路径上返回真实 top-k routing 而非全零，并确认 --moe-backend auto + capture 的 guard 是否阻止 silent mismatch。

