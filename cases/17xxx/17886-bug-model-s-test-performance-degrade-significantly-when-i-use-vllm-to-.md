# vllm-project/vllm#17886: [Bug]: Model's test performance degrade significantly when I use vllm to deploy it with a concurrency number exceeding 5

| 字段 | 值 |
| --- | --- |
| Issue | [#17886](https://github.com/vllm-project/vllm/issues/17886) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Model's test performance degrade significantly when I use vllm to deploy it with a concurrency number exceeding 5

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I deployed a Qwen2.5-7b-Instruct server using vLLM. Without enabling concurrency, the accuracy remains above 70%, but with 50 concurrent requests enabled, the accuracy drops to 0. Upon inspecting the model's outputs, I observed a significant amount of hallucinations. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Model's test performance degrade significantly when I use vllm to deploy it with a concurrency number exceeding 5 bug;stale ### Your current environment ### 🐛 Describe the bug I deployed a Qwen2.5-7b-Instruct ser...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: y when I use vllm to deploy it with a concurrency number exceeding 5 bug;stale ### Your current environment ### 🐛 Describe the bug I deployed a Qwen2.5-7b-Instruct server using vLLM. Without enabling concurrency, the ac...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Model's test performance degrade significantly when I use vllm to deploy it with a concurrency number exceeding 5 bug;stale ### Your current environment ### 🐛 Describe the bug I deployed a Qwen2.5-7b-Instruct ser...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: Qwen2.5-7b-Instruct server using vLLM. Without enabling concurrency, the accuracy remains above 70%, but with 50 concurrent requests enabled, the accuracy drops to 0. Upon inspecting the model's outputs, I observed a si...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: inspecting the model's outputs, I observed a significant amount of hallucinations. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the botto...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
