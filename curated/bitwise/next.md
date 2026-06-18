# Bitwise 下一轮复核队列

状态：active queue。  
作用：记录下一轮要补证的 bitwise/deterministic 工作项。本文只放队列和缺口，不承载最终机制结论；稳定结论应下沉到 [本专题机制页](README.md)。

## 已完成本轮推进

| Source | 状态 | 本轮结论 |
| --- | --- | --- |
| [#39096](https://github.com/vllm-project/vllm/issues/39096) / [#38938](https://github.com/vllm-project/vllm/pull/38938) | include | 已确认 batch invariance regression 至少包含两个具体机制：`ParallelLMHead` 的 `UnquantizedEmbeddingMethod.apply` 未走 deterministic Triton persistent kernel，以及 SM<90 下 `torch.compile` + CUDA graphs 组合需要边界处理。 |
| [#40179](https://github.com/vllm-project/vllm/pull/40179) | include + boundary | scheduler split 是核心机制方向；本轮确认 review comment 直接命中当前 patch：`request.num_output_tokens > 0` 与 `remainder == 0` 两个早退会漏掉 resumed request、block-aligned prompt 和 final-token scheduler 约束。 |
| [#39591](https://github.com/vllm-project/vllm/pull/39591) | include + invariant | `BlockTable` 的稳定契约不是“写入当前 slice”，而是 `num_blocks_per_row` 之后 tail 必须为零；`move_row`、`clear_row`、row reuse 都要维护该 invariant。 |
| [#42240](https://github.com/vllm-project/vllm/pull/42240) | include + workaround | `splitK=0` 是 scoped workaround，绕过 CK/CK-Tile split-K atomic reduction；本轮确认 128x128 weight group guard 已进入 `can_implement` 和 call-site assert，env opt-out 也被删除。 |
| [#43355](https://github.com/vllm-project/vllm/pull/43355) | include + risk | PR 的 bit-identical test 有价值；本轮深读修正了风险状态：HND/NHD layout gate 与 key/value row guard 已在 patch 中出现，FP8 `scaled_convert` 仍使用 `raw_kv_scalar_t`，且 PR 仍 open/unmerged、有 merge conflict 提醒。 |
| [#44250](https://github.com/vllm-project/vllm/issues/44250) | strong defer | issue body 和评论已足以支持 external KV key 缺 adapter identity 的 root-cause 方向；但评论中的 `lora_name` patch 只是本地对照实验，未证明上游 MP connector、vLLM vendored connector 和 regression test 已闭环。 |

## Must Review

| Source | 机制 | 当前状态 | 缺口 | 下一步 |
| --- | --- | --- | --- | --- |
| [#38991](https://github.com/vllm-project/vllm/issues/38991) | quant/dtype loading identity | defer | 本地 evidence 只有 open issue body，comments/timeline 均为空；`clone()`、每次或最终 `torch.cuda.synchronize()`、改变 stream file 顺序只是作者定位实验，不能当作 upstream fix。 | 寻找 linked PR/commit/test，重点看 `runai_safetensors_weights_iterator` ownership、`BaseModelLoader.load_model()` copy synchronization、shared buffer lifetime 和 unified-memory 平台回归测试。 |
| [#44250](https://github.com/vllm-project/vllm/issues/44250) | external KV / LoRA identity | defer | 已有端到端 cross-adapter 命中、key schema 代码证据、unpatched/patched connector 对照；但缺 linked fix PR、changed files、maintainer resolution 和 regression test。`lora_name` 对照 patch 只能证明缺 adapter 维度，不能证明最终 external cache key schema。 | 继续抓取或等待 linked fix PR；重点看 MP lookup/store key 是否纳入稳定 LoRA identity/version，并同时覆盖 LMCache MP connector、vLLM vendored connector、同 adapter hit 保留与跨 adapter negative test。 |

## Strong Include Needs More Detail

| Source | 机制 | 下一步 |
| --- | --- | --- |
| [#40179](https://github.com/vllm-project/vllm/pull/40179) | prefix cache 等价 | 继续追踪 follow-up patch：用 `num_computed_tokens` 判断 prefill、用 `(num_prompt_tokens - 1)` 计算 block boundary，并补 resumed request 与 block-aligned prompt 回归测试。 |
| [#39591](https://github.com/vllm-project/vllm/pull/39591) | KV cache identity | 继续确认 `move_row` 优化建议是否被采纳；若未采纳，标为性能边界而非 correctness 缺口。 |
| [#42240](https://github.com/vllm-project/vllm/pull/42240) | deterministic reduction | 继续追踪 PR 是否转为 ready/merged，以及上游 AITER 是否落地 deterministic split-K 修复；当前仍按 scoped workaround 维护，不外推到非 128x128 block-scaled shape。 |
| [#43355](https://github.com/vllm-project/vllm/pull/43355) | verification contract | 追踪 FP8 conversion 是否改为 `qk_t`/浮点输入，以及 NHD layout gate、key/value row guard 是否被 maintainer 接受并进入最终合并版本；未闭环前只作为 verification boundary/risk。 |

## 不应 Promotion 的情况

- 只有关键词命中，没有 issue/PR 正文或评论证据。
- 只有问题描述，没有 linked fix、patch、maintainer resolution 或复现闭环。
- umbrella issue 没有拆到具体 PR 或具体机制。
- 只能证明 semantic answer 相似，不能证明 token/logprob/tensor/KV identity。
