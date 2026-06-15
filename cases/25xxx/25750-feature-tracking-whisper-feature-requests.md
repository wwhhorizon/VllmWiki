# vllm-project/vllm#25750: [Feature]: Tracking Whisper feature requests

| 字段 | 值 |
| --- | --- |
| Issue | [#25750](https://github.com/vllm-project/vllm/issues/25750) |
| 状态 | open |
| 标签 | help wanted;good first issue;feature request;keep-open;multi-modality |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Tracking Whisper feature requests

### Issue 正文摘录

### 🚀 The feature, motivation and pitch This issue is for keeping track of the recurrent Whisper asks as well as the linked on-going efforts to support that feature, if any. When a feature request has no linked PR, feel free to claim the work here if you want to help! - [ ] Support different `response_formats` https://platform.openai.com/docs/api-reference/audio/createTranscription - Related issues: https://github.com/vllm-project/vllm/issues/19556, https://github.com/vllm-project/vllm/issues/14818, https://github.com/vllm-project/vllm/issues/24302 - PR(s): https://github.com/vllm-project/vllm/pull/24209 (`verbose_json`, **help needed with other formats**) - [ ] Support timestamp granularities: - Context: Very much related to the above. Unfortunately outputting by `word` requires aligning encoder latents (usually extrapolated from the crossattn layers) with decoder ones. I feel a lot of these whsper-specific techniques bring in added complexity to vLLM. However, I think we're open to exploring in this direction if we can come up with a less invasive solutions. Some references to get started https://github.com/m-bain/whisperX https://github.com/openai/whisper/discussions/684 . - ht...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: issue is for keeping track of the recurrent Whisper asks as well as the linked on-going efforts to support that feature, if any. When a feature request has no linked PR, feel free to claim the work here if you want to h...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: at it would be ideal to _guide_ the output tokens among valid languages. Accuracy to evaluate. - Related issues: https://github.com/vllm-project/vllm/issues/14174 - PR: https://github.com/vllm-project/vllm/pull/34342 -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: im the work here if you want to help! - [ ] Support different `response_formats` https://platform.openai.com/docs/api-reference/audio/createTranscription - Related issues: https://github.com/vllm-project/vllm/issues/195...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Tracking Whisper feature requests help wanted;good first issue;feature request;keep-open;multi-modality ### 🚀 The feature, motivation and pitch This issue is for keeping track of the recurrent Whisper asks as...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: at it would be ideal to _guide_ the output tokens among valid languages. Accuracy to evaluate. - Related issues: https://github.com/vllm-project/vllm/issues/14174 - PR: https://github.com/vllm-project/vllm/pull/34342 -...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
