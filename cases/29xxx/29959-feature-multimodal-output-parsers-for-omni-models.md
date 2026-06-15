# vllm-project/vllm#29959: [Feature]: Multimodal Output Parsers for Omni Models

| 字段 | 值 |
| --- | --- |
| Issue | [#29959](https://github.com/vllm-project/vllm/issues/29959) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Multimodal Output Parsers for Omni Models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Concepts - Chat templates are used to convert structured chat messages into a single prompt string that the model can process. These function as input formatters. - Reasoning and tool call parsers are used to interpret the model’s generated output and convert it back into OpenAI Chat messages or response API formats. These function as structured output parsers. ## Motivation - Omni models now generate modality such as vision, audio, or speech actions that are represented using XML like tags, such as followings. ``` ... ... ... ... ... ... ``` - vLLM users will likely need to convert these multimodal outputs into OpenAI Chat Completion or Responses API formats to maintain compatibility with existing clients. - While some of these outputs might be expressible as tool calls, most are model-native multimodal actions that are produced frequently and are tightly integrated into the model training. Also omni model doesn't need tool lists to calls about these. - Therefore, just like reasoning parsers or tool call parsers, we likely need a dedicated multimodal output parser to interpret these tags and convert them into structured response objects....

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Multimodal Output Parsers for Omni Models feature request ### 🚀 The feature, motivation and pitch ## Concepts - Chat templates are used to convert structured chat messages into a single prompt string that the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Multimodal Output Parsers for Omni Models feature request ### 🚀 The feature, motivation and pitch ## Concepts - Chat templates are used to convert structured chat messages into a single prompt string that the...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
