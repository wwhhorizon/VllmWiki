# Bitwise 下一轮复核队列

状态：active queue。  
作用：记录下一轮要补证的 bitwise/deterministic 工作项。本文只放队列和缺口，不承载最终机制结论；稳定结论应下沉到 [本专题机制页](README.md)。

## 已完成本轮推进

| Source | 状态 | 本轮结论 |
| --- | --- | --- |
| [#39096](https://github.com/vllm-project/vllm/issues/39096) / [#38938](https://github.com/vllm-project/vllm/pull/38938) | include | 已确认 batch invariance regression 至少包含两个具体机制：`ParallelLMHead` 的 `UnquantizedEmbeddingMethod.apply` 未走 deterministic Triton persistent kernel，以及 SM<90 下 `torch.compile` + CUDA graphs 组合需要边界处理。 |
| [#40179](https://github.com/vllm-project/vllm/pull/40179) | include + boundary | scheduler split 是核心 fix；review comment 暴露 resumed request、block-aligned prompt、final-token scheduler 约束，后续验证矩阵必须覆盖。 |
| [#39591](https://github.com/vllm-project/vllm/pull/39591) | include + invariant | `BlockTable` 的稳定契约不是“写入当前 slice”，而是 `num_blocks_per_row` 之后 tail 必须为零；`move_row`、`clear_row`、row reuse 都要维护该 invariant。 |
| [#42240](https://github.com/vllm-project/vllm/pull/42240) | include + workaround | `splitK=0` 是 scoped workaround，绕过 CK split-K atomic reduction；review comment 暴露 direct CK call 与 weight group shape / 128x128 兼容性边界。 |
| [#43355](https://github.com/vllm-project/vllm/pull/43355) | include + risk | PR 的 bit-identical test 有价值，但本轮证据中 PR 仍 open/unmerged 且有 merge conflict 提醒；review comments 暴露 FP8 conversion type、HND/NHD layout、key/value shape guard 三类未闭环验证缺口。 |

## Must Review

| Source | 机制 | 当前状态 | 缺口 | 下一步 |
| --- | --- | --- | --- | --- |
| [#38991](https://github.com/vllm-project/vllm/issues/38991) | quant/dtype loading identity | defer | 本地 evidence 只有 open issue body，comments/timeline 均为空；`clone()`、每次或最终 `torch.cuda.synchronize()`、改变 stream file 顺序只是作者定位实验，不能当作 upstream fix。 | 寻找 linked PR/commit/test，重点看 `runai_safetensors_weights_iterator` ownership、`BaseModelLoader.load_model()` copy synchronization、shared buffer lifetime 和 unified-memory 平台回归测试。 |
| [#44250](https://github.com/vllm-project/vllm/issues/44250) | external KV / LoRA identity | defer | 已有 unpatched/patched connector 复现对照，但缺上游 MP connector fix、vLLM vendored connector patch 和 regression test；评论提到的 LoRA-aware POC 可能只覆盖 V1 path。 | 继续抓取或等待 linked fix PR；重点看 MP lookup/store key 是否纳入 LoRA identity/version，并覆盖 vendored connector。 |

## Strong Include Needs More Detail

| Source | 机制 | 下一步 |
| --- | --- | --- |
| [#40179](https://github.com/vllm-project/vllm/pull/40179) | prefix cache 等价 | 继续确认 review comment 中 resumed/block-aligned 风险是否已有后续 patch 或 maintainer resolution。 |
| [#39591](https://github.com/vllm-project/vllm/pull/39591) | KV cache identity | 继续确认 `move_row` 优化建议是否被采纳；若未采纳，标为性能边界而非 correctness 缺口。 |
| [#42240](https://github.com/vllm-project/vllm/pull/42240) | deterministic reduction | 确认 weight group shape guard 是否已经落入 patch；否则保留为 workaround 边界。 |
| [#43355](https://github.com/vllm-project/vllm/pull/43355) | verification contract | 追踪 FP8 conversion、NHD layout gate、key/value row guard 三个 review risk 是否有 follow-up patch 或 maintainer resolution；未闭环前只作为 boundary/risk。 |

## 不应 Promotion 的情况

- 只有关键词命中，没有 issue/PR 正文或评论证据。
- 只有问题描述，没有 linked fix、patch、maintainer resolution 或复现闭环。
- umbrella issue 没有拆到具体 PR 或具体机制。
- 只能证明 semantic answer 相似，不能证明 token/logprob/tensor/KV identity。
