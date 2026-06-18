# Bitwise 下一轮复核队列

状态：active queue。  
作用：记录下一轮要补证的 bitwise/deterministic 工作项。本文只放队列和缺口，不承载最终机制结论；稳定结论应下沉到 [本专题机制页](README.md)。

## 已完成本轮推进

| Source | 状态 | 本轮结论 |
| --- | --- | --- |
| [#39096](https://github.com/vllm-project/vllm/issues/39096) / [#38938](https://github.com/vllm-project/vllm/pull/38938) | include | 已确认 batch invariance regression 至少包含两个具体机制：`ParallelLMHead` 的 `UnquantizedEmbeddingMethod.apply` 未走 deterministic Triton persistent kernel，以及 SM<90 下 `torch.compile` + CUDA graphs 组合需要边界处理。 |
| [#40179](https://github.com/vllm-project/vllm/pull/40179) | include + boundary | scheduler split 是核心机制方向；本轮确认 review comment 直接命中当前 patch：`request.num_output_tokens > 0` 与 `remainder == 0` 两个早退会漏掉 resumed request、block-aligned prompt 和 final-token scheduler 约束。 |
| [#39591](https://github.com/vllm-project/vllm/pull/39591) | include + invariant | `BlockTable` 的稳定契约不是“写入当前 slice”，而是 `num_blocks_per_row` 之后 tail 必须为零；本轮确认 `move_row` 整行复制是性能/简化建议，不是 correctness 阻塞。 |
| [#42240](https://github.com/vllm-project/vllm/pull/42240) | include + workaround | `splitK=0` 是 scoped workaround，绕过 CK/CK-Tile split-K atomic reduction；本轮确认 128x128 weight group guard 已进入 `can_implement` 和 call-site assert，env opt-out 也被删除。 |
| [#43355](https://github.com/vllm-project/vllm/pull/43355) | include + risk | PR 的 bit-identical test 有价值；本轮深读修正了风险状态：HND/NHD layout gate 与 key/value row guard 已在 patch 中出现，FP8 `scaled_convert` 仍使用 `raw_kv_scalar_t`，且 PR 仍 open/unmerged、有 merge conflict 提醒。 |
| [#44250](https://github.com/vllm-project/vllm/issues/44250) | strong defer | issue body 和评论已足以支持 external KV key 缺 adapter identity 的 root-cause 方向；但评论中的 `lora_name` patch 只是本地对照实验，未证明上游 MP connector、vLLM vendored connector 和 regression test 已闭环。 |
| [#42699](https://github.com/vllm-project/vllm/issues/42699) / [#40896](https://github.com/vllm-project/vllm/issues/40896) | defer | prefix-read/no-prefix-read 与 cold/warm prefix cache 的 greedy token 差异更像 BF16 batch/kernel geometry 边界：评论显示 `fp32` 或 `VLLM_BATCH_INVARIANT=1` 可让输出收敛，但缺 linked fix PR 和 regression test。 |
| [#42670](https://github.com/vllm-project/vllm/pull/42670) | include + boundary | FlashInfer/CUTLASS FP4 MoE 已有 batch-invariant code path，但 support gate 继承 base-class `False`，导致 `VLLM_BATCH_INVARIANT=1` 不可达；PR 用两个 capability override 暴露路径，并以 MiniMax-M2 NVFP4 并发复现的相同 sha256 证明 workaround 有效。仍 open，且模型级复现不适合 CI。 |
| [#42007](https://github.com/vllm-project/vllm/issues/42007) / [#42120](https://github.com/vllm-project/vllm/pull/42120) | include + boundary | FP8 MoE LoRA corruption 拆成两个契约：LoRA kernel 需要原始 BF16/FP16 activation，而 base GEMM 需要量化 activation；无 active LoRA 的 base batch 必须按 `no_lora_flag` 早退，避免 stale mapping 写坏输出。PR 有 approval 和 Blackwell 验证，但仍 open，且 wrong input dtype 单测欠缺。 |
| [#42325](https://github.com/vllm-project/vllm/issues/42325) / [#42379](https://github.com/vllm-project/vllm/pull/42379) | include | RMSNorm native-dtype multiply fix 已 merged，并同步 regular/fused quant path；但后续评论对 Python IR 是否是 CUDA spec 有争议，因此结论边界写成“已合并 native-dtype behavior + 现有测试覆盖”，不把某一侧实现扩展成通用规范。 |
| [#39146](https://github.com/vllm-project/vllm/issues/39146) / [#39283](https://github.com/vllm-project/vllm/pull/39283) / [#43741](https://github.com/vllm-project/vllm/pull/43741) | include + boundary | recycled KV block zeroing 需要两个 gate：`needs_kv_cache_zeroing` 覆盖 FullAttentionSpec family，manager 用 `isinstance` 把所有 FullAttentionSpec 子类的新 block id 送进 zeroing pipeline。`#43741` 仍 open，unit tests 强但 patched e2e 还要追踪。 |
| [#25404](https://github.com/vllm-project/vllm/issues/25404) / [#25603](https://github.com/vllm-project/vllm/pull/25603) | include | merged PR 提供 batch-invariant mode 的首批 C++/Python/env hook 和 kernel override plumbing；review 后把命名从 deterministic 收敛为 batch invariant，并补 logprob bit equality。结论边界是“plumbing 已有”，不是“所有 kernel 已覆盖”。 |

## Must Review

| Source | 机制 | 当前状态 | 缺口 | 下一步 |
| --- | --- | --- | --- | --- |
| [#38991](https://github.com/vllm-project/vllm/issues/38991) | quant/dtype loading identity | defer | 本地 evidence 只有 open issue body，comments/timeline 均为空；`clone()`、每次或最终 `torch.cuda.synchronize()`、改变 stream file 顺序只是作者定位实验，不能当作 upstream fix。 | 寻找 linked PR/commit/test，重点看 `runai_safetensors_weights_iterator` ownership、`BaseModelLoader.load_model()` copy synchronization、shared buffer lifetime 和 unified-memory 平台回归测试。 |
| [#44250](https://github.com/vllm-project/vllm/issues/44250) | external KV / LoRA identity | defer | 已有端到端 cross-adapter 命中、key schema 代码证据、unpatched/patched connector 对照；但缺 linked fix PR、changed files、maintainer resolution 和 regression test。`lora_name` 对照 patch 只能证明缺 adapter 维度，不能证明最终 external cache key schema。 | 继续抓取或等待 linked fix PR；重点看 MP lookup/store key 是否纳入稳定 LoRA identity/version，并同时覆盖 LMCache MP connector、vLLM vendored connector、同 adapter hit 保留与跨 adapter negative test。 |
| [#42699](https://github.com/vllm-project/vllm/issues/42699), [#40896](https://github.com/vllm-project/vllm/issues/40896) | prefix cache 等价 | defer | 复现和评论证据支持 prefix 路径可翻转 greedy token；但当前只有 mitigation 线索，没有 root-cause patch、maintainer resolution 或 regression test。 | 寻找 linked fix/docs/test PR；补齐 no-prefix、cold prefix、warm prefix、fp32、`VLLM_BATCH_INVARIANT=1` 的验证矩阵。 |

## Strong Include Needs More Detail

| Source | 机制 | 下一步 |
| --- | --- | --- |
| [#40179](https://github.com/vllm-project/vllm/pull/40179) | prefix cache 等价 | 继续追踪 follow-up patch：用 `num_computed_tokens` 判断 prefill、用 `(num_prompt_tokens - 1)` 计算 block boundary，并补 resumed request 与 block-aligned prompt 回归测试。 |
| [#42240](https://github.com/vllm-project/vllm/pull/42240) | deterministic reduction | 继续追踪 PR 是否转为 ready/merged，以及上游 AITER 是否落地 deterministic split-K 修复；当前仍按 scoped workaround 维护，不外推到非 128x128 block-scaled shape。 |
| [#43355](https://github.com/vllm-project/vllm/pull/43355) | verification contract | 追踪 FP8 conversion 是否改为 `qk_t`/浮点输入，以及 NHD layout gate、key/value row guard 是否被 maintainer 接受并进入最终合并版本；未闭环前只作为 verification boundary/risk。 |
| [#42670](https://github.com/vllm-project/vllm/pull/42670) | batch invariance support gate | 追踪 PR merge/CI；若继续推进，优先补轻量 selector/support-gate 测试，证明 `VLLM_BATCH_INVARIANT=1` 下 FlashInfer 与 CUTLASS FP4 MoE 不再被 `False` gate 拦截。 |
| [#42120](https://github.com/vllm-project/vllm/pull/42120) | quant/dtype LoRA MoE | 追踪 PR merge；补 wrong-input-dtype regression，以及 routed-expert LoRA weights 非零时的 adapter path 验证。 |
| [#42325](https://github.com/vllm-project/vllm/issues/42325) / [#42379](https://github.com/vllm-project/vllm/pull/42379) | RMSNorm dtype semantics | 若后续 maintainer 重新定义 CUDA reference 为 FP32 multiply，要同步改机制页的 reference boundary。 |
| [#43741](https://github.com/vllm-project/vllm/pull/43741) | recycled KV block zeroing | 追踪 PR merge；若最终 patch 改动，确认 spec gate、`new_block_ids` tracking 和 patched e2e validation 都保留。 |
| [#25603](https://github.com/vllm-project/vllm/pull/25603) | batch-invariant plumbing | 后续检查更多 kernels 是否接入 `VLLM_BATCH_INVARIANT`，尤其是 review 中提到的 multidim `torch.sum` / mean deterministic reduction。 |

## 不应 Promotion 的情况

- 只有关键词命中，没有 issue/PR 正文或评论证据。
- 只有问题描述，没有 linked fix、patch、maintainer resolution 或复现闭环。
- umbrella issue 没有拆到具体 PR 或具体机制。
- 只能证明 semantic answer 相似，不能证明 token/logprob/tensor/KV identity。
