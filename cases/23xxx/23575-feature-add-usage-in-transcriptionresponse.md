# vllm-project/vllm#23575: [Feature]: Add usage in TranscriptionResponse

| 字段 | 值 |
| --- | --- |
| Issue | [#23575](https://github.com/vllm-project/vllm/issues/23575) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add usage in TranscriptionResponse

### Issue 正文摘录

### 🚀 The feature, motivation and pitch OpenAI recently added the `usage` field to its `TranscriptionResponse` response object returned for audio transcriptions (see [specs](https://platform.openai.com/docs/api-reference/audio/json-object#audio/json-object-usage)) Currently vLLM [only output the `text` field](https://github.com/vllm-project/vllm/blob/2a167b2eeb993638c198db49f3927bae5d55508b/vllm/entrypoints/openai/protocol.py#L2235) in its TranscriptionResponse, while the duration (seconds) is [actually already extracted](https://github.com/vllm-project/vllm/blob/2a167b2eeb993638c198db49f3927bae5d55508b/vllm/entrypoints/openai/speech_to_text.py#L155). It would be nice to have the usage populated for the TranscriptionResponse object. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Add usage in TranscriptionResponse feature request ### 🚀 The feature, motivation and pitch OpenAI recently added the `usage` field to its `TranscriptionResponse` response object returned for audio transcripti...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
