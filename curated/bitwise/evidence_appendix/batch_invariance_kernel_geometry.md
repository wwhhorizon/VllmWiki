# Batch Invariance 与 Kernel Geometry Evidence Appendix

状态：curated public evidence summary。
父页：[../batch_invariance_kernel_geometry.md](../batch_invariance_kernel_geometry.md)。

本文只保存机制页之外的长证据摘要、case 表格、验证矩阵、详细边界和补证记录；通用问题定义、机制解释和修复模式以父页为准。

## 代表证据

| Source | 证据事实 | 炼化结论 |
| --- | --- | --- |
| [#36488](https://github.com/vllm-project/vllm/pull/36488) | MXFP4 MoE `matmul_ogs` 根据 tokens-per-expert 和 SM count 动态选择 `block_m`/`split_k`；PR 传入 `enforce_bitwise_invariance=True` 固定参数。 | batch invariant mode 必须传到实际 kernel config 层。 |
| [#39096](https://github.com/vllm-project/vllm/issues/39096), [#38938](https://github.com/vllm-project/vllm/pull/38938) | SM<90 GPU 上，`VLLM_BATCH_INVARIANT=1` 与 `torch.compile` 或 CUDA graphs 组合时不能保持 batch-invariant 输出；PR #38938 将问题拆成两个修复点：`ParallelLMHead` 使用的 `UnquantizedEmbeddingMethod.apply` 漏掉 batch-invariant GEMM 路由，以及 SM<90 下 `torch.compile` + CUDA graph 组合需要 enforce-eager 边界。 | 可以 promotion 为具体机制：batch invariance 必须覆盖 final logits projection 和 compile/graph support gate。 |
| [#32481](https://github.com/vllm-project/vllm/issues/32481), [#32561](https://github.com/vllm-project/vllm/pull/32561) | PR body 说明 cascade attention 会在某些 input batch 上条件性启用，造成 output logprobs 数值差异；merged patch 在 `VLLM_BATCH_INVARIANT=1` 下自动设置 `disable_cascade_attn=True`，并更新 logprob batch-invariance test。原始 test 在 FlashAttention backend 上 34/128 prompts 失败，关闭后通过。评论还把 FlashInfer/chunked prefill、MoE 和 AWQ 的后续失败拆为独立边界。 | batch-invariant mode 必须禁用或 gate 掉会随 batch composition 条件性启用的 attention 优化；logprob bitwise test 比文本相同更能暴露 ranking 边界。 |
| [#29581](https://github.com/vllm-project/vllm/issues/29581), [#38670](https://github.com/vllm-project/vllm/pull/38670) | AWQ 模型在 batch-invariant mode 下仍被自动转换到 AWQ_Marlin；Marlin CUDA kernel 绕开 batch-invariant Triton matmul override。merged PR 在 `VLLM_BATCH_INVARIANT=1` 时让 `awq_marlin.override_quantization_method()` 返回 `None`，并强制 AWQ dequant + `torch.matmul` path，使 BI override 能接管；测试从 Qwen3-4B-AWQ 7 failed/2 passed 变为 9 passed，并有 H200 验证评论和 approval。 | 支持某个 quantized model 的 BI，有时不是改 sampler，而是阻止自动转换到不可控 fused kernel。代价是放弃 AWQ_Marlin 性能，回到可被 deterministic override 控制的 matmul path。 |
| [#33688](https://github.com/vllm-project/vllm/pull/33688) | merged PR 将 `TRITON_ATTN` 纳入 decode-invariant backend，并在 batch-invariant mode 下强制 `triton_unified_attention` 走 2D kernel，避免随 decode batch shape 选择 3D path。B200 上 `TRITON_ATTN` logprob BI test 原本 128/128 prompts fail，patch 后通过；GPT-OSS 120B 也从 128/128 fail 到通过。 | backend support gate 不能只声明“可运行”；还要证明该 backend 在 prefill/decode 与 batch-size 变化下选到同一 deterministic kernel family。 |

## Source-Adjacent 摘要

- `#42670` 把一个常见误判拆开了：并不是每次 batch-invariant 失效都意味着“底层 kernel 没有 invariant 实现”，也可能是 support gate 把已有 invariant path 整条挡掉。当前证据里，PR 的 changed files 和测试计划都把问题收敛到 FlashInfer/CUTLASS FP4 MoE 在 `VLLM_BATCH_INVARIANT=1` 下仍被 base capability `False` 拦截，因此用户虽然开了 BI mode，实际却到不了目标路径。
- 这也解释了为什么 `#42670` 更适合写成 support-gate workaround，而不是 checkpoint root-cause 修复：它解决的是“deterministic path 不可达”，不是“该 NVFP4 checkpoint 对低精度噪声为什么这么敏感”。即使 patch 合并，wiki 仍应保留 MiniMax-M2-family、B200、TP/concurrency 和 backend scope。
- `#38670/#33688` 则给了两个已 landed 的对照样例：一个是 BI mode 下绕开 AWQ_Marlin 自动转换，让 Triton matmul override 真正接管；另一个是把 `TRITON_ATTN` decode 路径固定到 2D kernel。它们共同说明 support gate 的验证不能只停留在“backend 名称被列进 supported list”，而要证明最终 dispatch 的 kernel family 真的变得稳定可达。

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

## Verification matrices

### Support-Gate 最小验证矩阵

| Source | 保护对象 | 最小验证矩阵 | 合格契约 | 不能被什么替代 |
| --- | --- | --- | --- | --- |
| [#42670](https://github.com/vllm-project/vllm/pull/42670) | `VLLM_BATCH_INVARIANT=1` 下 FlashInfer/CUTLASS FP4 MoE 的可达性与输出稳定性 | MiniMax-M2-family、B200、TP=2、concurrency=2、patched/unpatched 对照、`supports_batch_invariance()` 或 selector path 命中、输出 hash 或 token equality、CI 不覆盖原因 | BI mode 真的命中目标 backend/support gate，且已知复现不再分叉 | 只看 PR body；只有 capability flag 改动；没有模型级 before/after 复现 |
| [#38670](https://github.com/vllm-project/vllm/pull/38670) | AWQ 模型在 BI mode 下不再被自动转换到 Marlin fast path | AWQ model、BI on/off、patched/unpatched quantization override、最终 kernel path 对照、token/logprob equality | BI mode 下最终执行路径受 deterministic matmul override 控制 | 只证明 `override_quantization_method()` 返回变化；不检查最终 kernel path |
| [#33688](https://github.com/vllm-project/vllm/pull/33688) | `TRITON_ATTN` decode path 的 2D invariant kernel family | target hardware、decode batch-size matrix、patched/unpatched backend path、logprob before/after failure | BI mode 下 decode 不再落到 batch-sensitive 3D kernel | 只看 backend 名称；只看最终文本不看 logprob |

