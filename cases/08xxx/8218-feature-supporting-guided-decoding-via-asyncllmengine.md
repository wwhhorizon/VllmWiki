# vllm-project/vllm#8218: [Feature]: Supporting Guided Decoding via AsyncLLMEngine

| 字段 | 值 |
| --- | --- |
| Issue | [#8218](https://github.com/vllm-project/vllm/issues/8218) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Supporting Guided Decoding via AsyncLLMEngine

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Today, Guided Decoding can only be accessed if we use the OpenAI compatible API interface, since that is the only way of passing in a `GuidedDecodingRequest` object into the generation query. It should theoretically also be possible to support this via the AsyncLLMEngine.generate() interface. Anything blocking from supporting this today? I don't see it being possible to pass in a `GuidedDecodingRequest` into the generate method today. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: le to support this via the AsyncLLMEngine.generate() interface. Anything blocking from supporting this today? I don't see it being possible to pass in a `GuidedDecodingRequest` into the generate method today. ### Altern...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Supporting Guided Decoding via AsyncLLMEngine feature request ### 🚀 The feature, motivation and pitch Today, Guided Decoding can only be accessed if we use the OpenAI compatible API interface, since that is t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
