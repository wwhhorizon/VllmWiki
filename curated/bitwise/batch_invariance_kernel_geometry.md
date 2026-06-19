# Batch Invariance 与 Kernel Geometry

状态：curated。  
父页：[Bitwise 确定性与数值等价](README.md)。
范围：同一请求在单独运行、混 batch、并发 prefill/decode、first request 与 warmup 后的输出等价。

## 问题定义

同一个请求的输出不应因为其他无关请求进入同一个 batch 而改变。batch composition 可以改变吞吐、排队和调度，但不能改变 deterministic decoding 的可见 token。

## 典型触发条件

- tokens-per-expert、batch size、sequence grouping 改变 MoE/GEMM kernel config。
- `block_m`、`split_k`、tile choice、backend path 或 graph capture 状态随 batch composition 改变。
- cascade attention、chunked prefill、FlashInfer CTA tile size 等条件性 attention 优化随 batch shape 或其他请求长度改变。
- FP4/FP8/MXFP4 MoE 路径中，scale layout、expert routing 和低精度累加放大差异。
- quantization method 自动转换到 fused kernel，绕开 batch-invariant override。
- first real request 触发 CUDA graph、Triton JIT、allocator/cache warmup。
- SM<90 上 `torch.compile` 或 CUDA graphs 与 batch-invariant mode 组合出现 strict equality 失败。

## 代表证据

| Source | 证据事实 | 炼化结论 |
| --- | --- | --- |
| [#36488](https://github.com/vllm-project/vllm/pull/36488) | MXFP4 MoE `matmul_ogs` 根据 tokens-per-expert 和 SM count 动态选择 `block_m`/`split_k`；PR 传入 `enforce_bitwise_invariance=True` 固定参数。 | batch invariant mode 必须传到实际 kernel config 层。 |
| [#39096](https://github.com/vllm-project/vllm/issues/39096), [#38938](https://github.com/vllm-project/vllm/pull/38938) | SM<90 GPU 上，`VLLM_BATCH_INVARIANT=1` 与 `torch.compile` 或 CUDA graphs 组合时不能保持 batch-invariant 输出；PR #38938 将问题拆成两个修复点：`ParallelLMHead` 使用的 `UnquantizedEmbeddingMethod.apply` 漏掉 batch-invariant GEMM 路由，以及 SM<90 下 `torch.compile` + CUDA graph 组合需要 enforce-eager 边界。 | 可以 promotion 为具体机制：batch invariance 必须覆盖 final logits projection 和 compile/graph support gate。 |
| [#32481](https://github.com/vllm-project/vllm/issues/32481), [#32561](https://github.com/vllm-project/vllm/pull/32561) | PR body 说明 cascade attention 会在某些 input batch 上条件性启用，造成 output logprobs 数值差异；merged patch 在 `VLLM_BATCH_INVARIANT=1` 下自动设置 `disable_cascade_attn=True`，并更新 logprob batch-invariance test。原始 test 在 FlashAttention backend 上 34/128 prompts 失败，关闭后通过。评论还把 FlashInfer/chunked prefill、MoE 和 AWQ 的后续失败拆为独立边界。 | batch-invariant mode 必须禁用或 gate 掉会随 batch composition 条件性启用的 attention 优化；logprob bitwise test 比文本相同更能暴露 ranking 边界。 |
| [#29581](https://github.com/vllm-project/vllm/issues/29581), [#38670](https://github.com/vllm-project/vllm/pull/38670) | AWQ 模型在 batch-invariant mode 下仍被自动转换到 AWQ_Marlin；Marlin CUDA kernel 绕开 batch-invariant Triton matmul override。merged PR 在 `VLLM_BATCH_INVARIANT=1` 时让 `awq_marlin.override_quantization_method()` 返回 `None`，并强制 AWQ dequant + `torch.matmul` path，使 BI override 能接管；测试从 Qwen3-4B-AWQ 7 failed/2 passed 变为 9 passed，并有 H200 验证评论和 approval。 | 支持某个 quantized model 的 BI，有时不是改 sampler，而是阻止自动转换到不可控 fused kernel。代价是放弃 AWQ_Marlin 性能，回到可被 deterministic override 控制的 matmul path。 |
| [#33688](https://github.com/vllm-project/vllm/pull/33688) | merged PR 将 `TRITON_ATTN` 纳入 decode-invariant backend，并在 batch-invariant mode 下强制 `triton_unified_attention` 走 2D kernel，避免随 decode batch shape 选择 3D path。B200 上 `TRITON_ATTN` logprob BI test 原本 128/128 prompts fail，patch 后通过；GPT-OSS 120B 也从 128/128 fail 到通过。 | backend support gate 不能只声明“可运行”；还要证明该 backend 在 prefill/decode 与 batch-size 变化下选到同一 deterministic kernel family。 |

## 根因机制

Batch invariance 被破坏时，根因常常不是 sampler，而是 kernel geometry。batch composition 改变了每个 kernel 看到的 shape、expert token 分布、graph/capture 状态或 reduction order。低精度 MoE/FP4/FP8 路径中，scale layout 和 expert routing 会进一步放大这些差异。

`#42670` 补充了一个容易漏掉的层次：即使底层 backend 已经有固定 split size、禁用 split-KV 或固定 per-expert tile 的 invariant path，selector/oracle 的 support gate 仍可能让该路径完全不可达。此时问题不是“没有 deterministic kernel”，而是“deterministic kernel 没有被声明为可选能力”。

`#32561` 再补充一个 attention 侧机制：某些优化不是固定 backend，而是按当前 batch 的形状、长度或内部 heuristics 条件性启用。cascade attention 在普通模式下是性能优化，但在 batch-invariant mode 下会让同一请求因为同 batch 的其他请求不同而走不同 attention path。评论中的 FlashInfer CTA tile size 讨论也说明，query tile 如果取决于 batch 内最大/平均 query length，就天然不是 batch-invariant。

`#38670/#30018/#33688` 显示 BI 覆盖面不是一个总开关。每个 backend 或 quantization path 都必须证明自己的执行路径能被 deterministic override 管住：AWQ 需要绕开 Marlin 自动转换，FA2 需要固定 attention split，TRITON_ATTN 需要在 BI mode 下强制 2D kernel；LoRA 这类扩展路径即使已有测试覆盖，也要继续复核最终 landed code 是否真的固定 reduction geometry。否则用户设置了 `VLLM_BATCH_INVARIANT=1`，但实际 kernel 仍可能走到未被覆盖的 fast path。

`#42513/#42518` 则提供了一个更适合写成契约边界、而不是“等待 landed fix”的案例。作者先用 `#42513` 给出最小 root-cause 假说，随后在 `#42518` 提供完整复现矩阵、maintainer 评论和后续 prototype 线索。现有最佳证据支持这样一条链路：MTP verification forward 的 batch_size=2 与普通 decode 的 batch_size=1 改变 eager 模式下的 attention GEMM 几何，1-2 ULP BF16 差异写入 KV 后在后续 decode 中放大到 token 分叉；而 maintainer 明确把这类 exact reproducibility 需求收口到 `VLLM_BATCH_INVARIANT=1`，没有接受单独的官方 fix PR。

`#42699/#40896` 也显示出同样的收口方式：对 prefix-read/no-prefix-read、cold/warm prefix cache 这类 exact reproducibility 报告，评论证据表明 `fp32` 或 `VLLM_BATCH_INVARIANT=1` 都能让输出重新收敛；其中 `#42699` 还把缓解直接指向已合并的 [#40193](https://github.com/vllm-project/vllm/pull/40193)。这说明在当前上游语义下，默认 prefix-cache path 的这类差异更适合先解释为 batch/query-length 改变 backend geometry 的数值路径边界，而不是先假设存在独立的 prefix-cache KV corruption。

## 修复方式

1. 找出 batch composition 改变的 kernel config：`block_m`、`split_k`、tile、backend、graph capture、tokens-per-expert。
2. 在 deterministic/batch-invariant mode 下固定这些 config，或拆分 fast path 与 deterministic path。
3. 确认 support gate、backend selector、MoE oracle 都能到达 invariant path。
4. 对 quantized MoE 同时记录 scale layout、expert routing、hardware SM count 和 backend。
5. 对 support-gate fix，除了 patch kernel 本身，还要检查 `supports_batch_invariance()`、MoE expert capability、attention backend selector 和实际 engine config 是否一致。
6. 对条件性 attention 优化，在 batch-invariant mode 下禁用该优化，或证明它的启用条件和内部 tile size 不依赖同 batch 的其他请求。
7. 对 quantization auto-conversion，检查最终 kernel 是否仍会经过 BI override；若 fused kernel 不受控，应在 BI mode 下绕开或提供独立 deterministic kernel。

## 验证契约

- 同一请求分别在 batch=1、混 batch、并发 prefill/decode 中输出 token 一致。
- first request、warmup 后请求、CUDA graph capture 前后都要覆盖。
- 对 low precision MoE，要同时记录 kernel config 和 strict/token equality。
- 对 `torch.compile` / CUDA graphs 问题，要区分 compiler graph、CUDA graph、kernel 本身和 test harness 的归因。
- 对 support-gate 类修复，至少要证明 invariant mode 能选到目标 backend；若只能做模型级复现，也要记录硬件、模型、TP/concurrency、backend、输出 hash 和 CI 不覆盖原因。
- 对 warmup 类修复，要分清首请求 latency 稳定、graph/JIT 编译完成和 token/logprob bitwise 稳定；三者不能互相替代。
- 对 attention path gate，优先比较 logprobs 和 token，而不是只看最终文本；`#32561` 的 34/128 prompts failure 说明 logprob ranking 可以在文本变化前暴露问题。
- 对 backend enablement，测试必须覆盖 before/after failure、目标 backend 名称、硬件、模型和是否 `enforce_eager`；若 CUDA graph 未覆盖，要明说。

## 适用边界

- `#27433` 是 umbrella，不直接 promotion。
- `#39096/#38938` 已能支持 final logits projection 与 SM<90 compile/graph 边界这两个具体机制；但不要外推为所有 torch.compile 场景都不支持 batch invariance。
- `#42670` 的证据集中在 MiniMax-M2-family NVFP4、FlashInfer/CUTLASS FP4 MoE 和 `VLLM_BATCH_INVARIANT=1`；PR body 也把它定位成移除一个具体噪声源的 workaround，而不是修复该 checkpoint 对低精度噪声敏感的根因。PR 仍 open/unmerged，不能写成已发布能力。
- `#33537` 的 warmup 机制合理，但本地 evidence 中缺少“无 warmup token/logprob diverge、有 warmup bitwise 收敛”的闭环；目前只能作为 cold-start serving-state 边界，不进入代表证据。
- `#32561` 已 merged，可作为 cascade attention gate 的稳定结论；但 PR 讨论明确把 FlashInfer chunked prefill、MoE、AWQ 继续拆成后续问题，因此不能外推为所有 attention backend 和所有 quantized/MoE 模型都已 batch-invariant。
- `#38670` 已 merged，但它是 AWQ/Marlin 的性能换确定性方案：BI mode 绕开 Marlin，走 dequant + `torch.matmul`。不能外推为 AWQ_Marlin 本身已 batch-invariant。
- `#30018` 已 merged，FA2 split path 有直接 patch 证据，LoRA 有 PR body、测试矩阵和 review 支持；但本地 evidence 不足以把 LoRA landed-code 子路径写成完全闭环，且作者明确说该 PR 不支持 CUDA graph，测试依赖 `enforce_eager`。
- `#33688` 已 merged，证据集中在 B200、TRITON_ATTN、2D kernel 和 GPT-OSS/Qwen 测试；它不代表所有 Triton attention variant、MLA 或 FlashInfer 已覆盖。
- `#42513/#42518` 目前最准确的定位是契约边界：maintainer 明确认为 eager 模式下这类 drift 是 known issue，若需要 exact invariance 应使用 batch-invariant mode。现有本地证据支持“MTP verification batch geometry -> eager attention GEMM 数值路径变化 -> KV 放大 -> token 分叉”的根因方向，但没有官方 linked fix、changed files 或 regression test，因此不能写成 landed 机制。
- `#42699/#40896` 目前也更准确地属于契约边界，而不是 prefix-cache 主线 direct-closure 缺口：`#40896` maintainer 明确说 prefix caching determinism 还未完全支持，`#42699` 评论则显示 `fp32` 与 `VLLM_BATCH_INVARIANT=1` 可以消除复现。除非后续出现 prefix-cache 专属 patch、官方 docs 变更或 regression test，否则不要把这两条 open issue 继续维护成独立主机制。
- batch invariance 与 deterministic dispatch/reduction 机制高度交叉；当根因是 split-K/atomic/autotune，应交叉写入 dispatch 页。

## 仍需补证

- 继续补充 `#38938` review comments 中关于 L4/H100 test placement、`enforce_eager` 边界和 CI 分组的细节。
- 继续拆 `#27433` 中的 umbrella 讨论，把具体 PR 映射到单独机制，不把 umbrella issue 当结论。
- 追踪 `#42670` 是否合并；最好补一个轻量 support-gate/selector test，证明 `VLLM_BATCH_INVARIANT=1` 下 FlashInfer 与 CUTLASS FP4 MoE 不再被 base-class `False` 拦截。
- 若继续推进 `#33537`，需要补 first-request token/logprob 复现矩阵，而不只是 latency benchmark。
- 继续拆 `#32561` 评论里留下的后续边界：FlashInfer CTA tile size/chunked prefill、MoE router gate、AWQ 长输出 failure 应各自寻找独立 PR/test，不能混入 cascade attention 的 landed fix。
- 对 `#38670/#30018/#33688` 后续追踪更广硬件和 backend 矩阵：AWQ_Marlin 是否未来提供 deterministic fused path，FA2 CUDA graph 是否补齐，LoRA landed-code split-K 子路径是否补证，TRITON_ATTN 是否扩展到更多 attention variant。
- 对 `#42513/#42518`，除非上游接受 selective fix 或新增明确的 eager-vs-BI contract test，否则继续按 batch-invariant 契约边界维护；优先寻找官方 regression test、文档化声明或后续 PR，而不是默认等待 `Fixes #42513`。
