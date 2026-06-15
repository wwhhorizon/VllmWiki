# vllm-project/vllm#11950: [Feature]: Support for serving two llms at the same time

| 字段 | 值 |
| --- | --- |
| Issue | [#11950](https://github.com/vllm-project/vllm/issues/11950) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for serving two llms at the same time

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I want to implement the interaction between two llms. But I found it will encounter error or lock when initializing two llms like following. Could you help to support this feature? It will be great useful! ``` python first_model_name = "Qwen/Qwen2.5-1.5B-Instruct" second_model_name = "Qwen/Qwen2.5-7B-Instruct" first_llm = LLM(model=first_model_name, tensor_parallel_size=2) second_llm = LLM(model=second_model_name, tensor_parallel_size=2) ``` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: help to support this feature? It will be great useful! ``` python first_model_name = "Qwen/Qwen2.5-1.5B-Instruct" second_model_name = "Qwen/Qwen2.5-7B-Instruct" first_llm = LLM(model=first_model_name, tensor_parallel_si...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support for serving two llms at the same time feature request;stale ### 🚀 The feature, motivation and pitch I want to implement the interaction between two llms. But I found it will encounter error or lock wh...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
