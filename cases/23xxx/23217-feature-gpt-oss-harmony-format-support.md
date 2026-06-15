# vllm-project/vllm#23217: [Feature]: GPT-OSS harmony format support

| 字段 | 值 |
| --- | --- |
| Issue | [#23217](https://github.com/vllm-project/vllm/issues/23217) |
| 状态 | closed |
| 标签 | help wanted;good first issue;feature request;stale;gpt-oss |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: GPT-OSS harmony format support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch From the view of API server, GPT-OSS introduces the following features: * Builtin tool call: tool calls that happens inside chain of thought. It is different from most existing models where tool call only exists in the output to users. * Harmony: a new text format to represent the chain of thought, tool calls, etc. vLLM needs to implement the parsing between `OpenAI API harmony model input/output tokens` vLLM has basic support of the above features on response API now. But as shown in https://docs.vllm.ai/projects/recipes/en/latest/OpenAI/GPT-OSS.html#harmony-format-support , the response API with streaming, and chat completion is still in an early stage. And help wanted on completing these features! ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: GPT-OSS harmony format support help wanted;good first issue;feature request;stale;gpt-oss ### 🚀 The feature, motivation and pitch From the view of API server, GPT-OSS introduces the following features: * Buil...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: re]: GPT-OSS harmony format support help wanted;good first issue;feature request;stale;gpt-oss ### 🚀 The feature, motivation and pitch From the view of API server, GPT-OSS introduces the following features: * Builtin to...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: res on response API now. But as shown in https://docs.vllm.ai/projects/recipes/en/latest/OpenAI/GPT-OSS.html#harmony-format-support , the response API with streaming, and chat completion is still in an early stage. And...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: onse API now. But as shown in https://docs.vllm.ai/projects/recipes/en/latest/OpenAI/GPT-OSS.html#harmony-format-support , the response API with streaming, and chat completion is still in an early stage. And help wanted...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
