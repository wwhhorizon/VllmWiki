# vllm-project/vllm#26157: [Feature]: Make Custom I/O Processing Plugins More General

| 字段 | 值 |
| --- | --- |
| Issue | [#26157](https://github.com/vllm-project/vllm/issues/26157) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Make Custom I/O Processing Plugins More General

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Granite Speech models, e.g., [granite-speech-3.3-8b](https://huggingface.co/ibm-granite/granite-speech-3.3-8b) have a two pass design for responding to the content of provided audio, since it first needs to transcribe text. As an example, in order to get the answer `4` from an audio clip with the content `what is 2+2?`, a user would first need to call the model to transcribe to text, and then call it again with the resulting input to get the response `4` out. This has turned out to be a big point of confusion for people adopting this model, and we would like the ability to abstract the two passes for non-transcription use-cases. This essentially boils down to: - Calling it normally if there's no audio - If there's audio, call generate w/ the audio, then pass the result into generate again With that in mind, I think that the cleanest way to support this would be to make [IO processor plugins](https://github.com/vllm-project/vllm/pull/22820), which are currently only used for pooling models, more general. If we were to take this approach and allow support for IO processor plugins on different model types / entrypoints, this would enable us to...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: re request;stale ### 🚀 The feature, motivation and pitch Granite Speech models, e.g., [granite-speech-3.3-8b](https://huggingface.co/ibm-granite/granite-speech-3.3-8b) have a two pass design for responding to the conten...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Make Custom I/O Processing Plugins More General feature request;stale ### 🚀 The feature, motivation and pitch Granite Speech models, e.g., [granite-speech-3.3-8b](https://huggingface.co/ibm-granite/granite-sp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
