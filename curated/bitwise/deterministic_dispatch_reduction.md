# Deterministic Dispatch 与 Reduction Control

状态：curated。  
父页：[Bitwise 确定性与数值等价](README.md)。
范围：autotune candidate、backend dispatch、split-K、atomic reduction、fast/deterministic path 和 warmup 状态。

## 问题定义

deterministic mode 必须控制 kernel/backend dispatch 和 reduction geometry。只设置随机种子不够；如果 dispatcher 仍可选择不同 autotune candidate、split-K、atomic reduction、backend fallback 或 warmup 状态，输出仍可能变化。

## 典型触发条件

- autotuner 在数值不等价 candidate 中选择。
- split-K 或 atomic reduction 改变浮点累加顺序。
- fast kernel 使用非 bitwise stable reduction。
- 首次请求触发 JIT、CUDA graph capture 或 allocator/cache warmup。
- hardware-specific dispatcher 从 CSV/heuristic 中选出不同策略。

## 代表证据

| Source | 证据事实 | 炼化结论 |
| --- | --- | --- |
| [#25194](https://github.com/vllm-project/vllm/issues/25194), [#25197](https://github.com/vllm-project/vllm/pull/25197) | Triton `_chunk_cumsum_fwd_kernel` 中 `BLOCK_H=1` 与 `BLOCK_H>1` 输出不同；PR 直接移除 `BLOCK_H=1` autotune config。 | autotune candidate 必须先证明数值等价，不能只按速度进入候选集。 |
| [#35183](https://github.com/vllm-project/vllm/pull/35183) | ROCm skinny GEMM 拆成 deterministic store-then-reduce 与 fast `atomicAdd` path，默认 deterministic，fast path 需显式 opt-in。 | deterministic 与 fast path 应拆开，而不是用同一个 kernel 隐式切换。 |
| [#34878](https://github.com/vllm-project/vllm/pull/34878) | ROCm beam search test 因 batch-size-dependent FP reduction 失败：Triton attention、hipBLAS/rocBLAS GEMM 和 skinny GEMM 的 reduction order 随 M 维改变，同一 logits row 的 `1e-5` 级 logprob 差异足以翻转 beam ranking。merged PR 在 ROCm 上显式设置 `async_scheduling=False`、`enforce_eager=True`、`enable_prefix_caching=False`、`max_num_seqs=1`，并把 `VLLM_ROCM_USE_SKINNY_GEMM=0` 写进测试，非 ROCm 不变。 | 有些 bitwise 修复是 verification-harness boundary：为了测试 beam search 语义，需要固定 batch composition、graph padding、prefix side effect 和 GEMM path，避免测试本身被 backend drift 污染。 |
| [#42240](https://github.com/vllm-project/vllm/pull/42240) | AITER FP8 block-scaled GEMM 的 CSV dispatcher 可能选择 `splitK >= 2`；CK/CK-Tile split-K reduction 通过 atomic floating-point adds 累加 partial K products。PR 在 non-Triton CK path 强制 `splitK=0`，保留 Triton path；第二个 commit 移除环境变量 opt-out，并在 `can_implement` 与 call site 同时约束 `weight_group_shape == GroupShape(128, 128)`。review 讨论还确认 vLLM wrapper 原本也没有真正把 `block_size` 传给 AITER。 | split-K / atomic reduction 是 deterministic contract 的直接控制点；workaround 已把 128x128 applicability 写入 patch，但仍是绕过上游 AITER reduction bug 的 scoped workaround。 |
| [#25404](https://github.com/vllm-project/vllm/issues/25404), [#25603](https://github.com/vllm-project/vllm/pull/25603) | `#25404` 提出 per-kernel deterministic override；merged PR `#25603` 实际落地为第一批 batch-invariant plumbing：C++ `batch_invariant.hpp` env hook、Python `batch_invariant.py`、GPU runner 初始化、layernorm/fused quant/topk softmax/flex attention 的 batch-invariant branch，以及 `tests/v1/generation/test_batch_invariance.py`。PR 测试显示没有 override 时 batch-size 64 的 5 次试验中 2 次输出偏离 batch=1，logprob test 也出现 `torch.equal` 失败；启用 `VLLM_KERNEL_OVERRIDE_BATCH_INVARIANT=1` 后通过。review 后把命名从 deterministic 调整为 batch invariant，并接受全局 env hook 作为当前 plumbing。 | 真实落地不是完整 per-kernel 配置系统，而是 batch-invariant mode 的全局开关与首批 kernel override；它提供后续 determinism 工作的接入点，但不能宣称所有 kernel 已被覆盖。 |
| [#33537](https://github.com/vllm-project/vllm/pull/33537) | batch invariant mode 下首次真实请求可能受 CUDA graph、Triton JIT、cache warming 影响；PR 增加 `VLLM_DETERMINISM_WARMUP_ITERATIONS`、`run_determinism_warmup()` 和 GPU worker warmup hook，单测覆盖默认值、显式覆盖、异常继续、禁用 warmup 等 12 项。review 要求可复现问题，作者后续给出的主要证据是 DeepSeek-V3 + TRITON_MLA + 8xH200 首请求 latency 从 8.7/6.0/3.2s 收敛到约 3.2s，而不是 token/logprob divergence。PR 后续被标 stale。 | warmup 是 serving-state boundary，而不是 kernel root-cause fix；当前证据更强支持 first-request latency predictability，作为 bitwise 修复只能 include-with-boundary。 |

## 根因机制

这类问题来自“可变但未被 deterministic contract 管住”的执行路径。dispatcher、autotuner、CSV heuristic 或 graph warmup 为了性能选择不同 kernel；这些 kernel 在数学上近似等价，但在浮点累加顺序、atomic interleaving 或低精度 rounding 上不 bitwise 等价。

`#25603` 还澄清了一个命名边界：batch invariant 比普通 deterministic 更严格。只要其中一个 op 仍随 batch shape 改变输出，整条 serving path 就不再 batch invariant；因此 review 最终倾向于全局 batch-invariant mode，而不是让用户以为可以随意混搭 per-kernel deterministic/variant 状态。

`#34878` 则展示了测试环境本身也需要 deterministic contract。beam search 的目标是比较候选序列排名，若 ROCm backend 在不同 batch/concurrency 下改变 logits M 维 reduction order，测试看到的 failure 可能来自 harness geometry，而不是 beam search 逻辑。此类修复要写成 test placement / engine-config boundary。

## 修复方式

1. 枚举 deterministic mode 下所有可变 dispatch 点。
2. 移除数值不等价 autotune candidate，或把它们降为 fast opt-in path。
3. 固定 reduction geometry：split-K、block size、atomic path、store-then-reduce。
4. 为 kernel 提供 deterministic override，而不是让全局开关停留在调度层。
5. 文档中写清 deterministic path 的性能代价和 hardware/backend 边界。
6. 对 workaround 型 fix，显式写清它绕过了哪个 dispatcher/上游 bug，以及哪些 shape/group-size 才允许调用。
7. 去掉 deterministic workaround 的环境变量反向开关：如果生产路径没有合法理由回到非确定 split-K，就不应保留 opt-out 让用户重新进入不稳定 kernel。
8. 对 batch-invariant plumbing，区分“全局 mode 可接入”和“某个 kernel 已实际覆盖”；新增 hook 不能替代逐 kernel 的 exact/logprob 验证。

## 验证契约

- 对同一输入 back-to-back 调用 kernel，要求 bit-identical 或明确 strict tolerance。
- 对 serving path 覆盖首次请求、warmup 后请求、CUDA graph capture 前后。
- fast opt-in path 不能借用 deterministic path 的 correctness claim。
- 对 split-K/atomic 修复，要记录 hardware、dtype、backend、kernel config、weight group shape 和 dispatcher source。
- 对 batch-invariant override，要同时比较输出 token 和 logprob bit equality；只比较生成文本可能漏掉排名边界的数值漂移。
- 对 beam search / ranking 测试，要检查 logprob ranking 是否被 `1e-5` 级差异翻转；测试 harness 必须固定 batch size、async scheduling、graph padding和 backend kernel path。

## 适用边界

- [#42240](https://github.com/vllm-project/vllm/pull/42240) 是 scoped workaround：强制 `splitK=0` 绕过 CK/CK-Tile reduction 问题，直到上游修复；当前 patch 只允许 128x128 weight group shape，不能外推为所有 AITER block-scaled shape 都安全。
- [#35183](https://github.com/vllm-project/vllm/pull/35183) 的 fast path 是显式性能取舍，不应默认承诺 bitwise stability。
- [#34878](https://github.com/vllm-project/vllm/pull/34878) 是 ROCm test-harness 修复，不等于生产服务默认关闭所有 batch-size-sensitive ROCm kernel；它证明 beam-search 测试需要固定几何，不证明所有 ROCm serving path 已 bitwise。
- [#25603](https://github.com/vllm-project/vllm/pull/25603) 已 merged，但它只是第一批 batch-invariant override plumbing；review 中仍保留 envvar 性能/可维护性讨论，且 coverage 只包括当时 patch touched 的 kernels，不代表全 vLLM serving path 已 batch invariant。
- [#33537](https://github.com/vllm-project/vllm/pull/33537) 仍 open/stale；现有 evidence 主要是 warmup 框架和首请求 latency 稳定性，不足以当作 token/logprob bitwise 修复。
- 与 batch invariance 页交叉：当 batch 改变触发不同 dispatch/reduction，最终归因应落到本机制。

## 仍需补证

- 继续复核 `kernel_autotune_reduction` cluster 中只被 benchmark 证明、但没有 exact/token equality 证明的 fast path。
- 补充 `#35183` deterministic/fast path 的性能边界和 opt-in 文档证据。
- 补充 `#25603` 后续 PR 是否继续把更多 kernels 接入 `VLLM_BATCH_INVARIANT`；特别检查 review comment 中提到的 multidim `torch.sum`/mean 是否已替换为 deterministic reduction。
- 若继续保留 `#33537`，需要找到 first-request token/logprob divergence 的直接复现；否则只把它维护为 latency/warmup boundary。
- 继续追踪 `#42240` 是否转为 ready/merged，以及上游 AITER 是否有对应 deterministic split-K 修复；只有上游闭环后才可把 vLLM workaround 视为可移除。
