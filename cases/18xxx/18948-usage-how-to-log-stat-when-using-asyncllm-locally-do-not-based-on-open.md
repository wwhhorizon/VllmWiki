# vllm-project/vllm#18948: [Usage]: How to log stat when using AsyncLLM locally (do not based on openAI api)

| 字段 | 值 |
| --- | --- |
| Issue | [#18948](https://github.com/vllm-project/vllm/issues/18948) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to log stat when using AsyncLLM locally (do not based on openAI api)

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a model in asyncLLM and set disable_log_stats=False, but I don't see any statistics associated with throughput, batch size.When using v0 AsyncLLMEngine, there is no such problem. SO my question is how to print log stat when using AsyncLLM? ![Image](https://github.com/user-attachments/assets/79cc7609-47b1-4d39-a4e8-3b52588b31cc) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: disable_log_stats=False, but I don't see any statistics associated with throughput, batch size.When using v0 AsyncLLMEngine, there is no such problem. SO my question is how to print log stat when using AsyncLLM? ![Image...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: cLLM and set disable_log_stats=False, but I don't see any statistics associated with throughput, batch size.When using v0 AsyncLLMEngine, there is no such problem. SO my question is how to print log stat when using Asyn...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: cc) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: want to run inference of a model in asyncLLM and set disable_log_stats=False, but I don't see any statistics associated with throughput, batch size.When using v0 AsyncLLMEngine, there is no such problem. SO my question...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: y` ``` ### How would you like to use vllm I want to run inference of a model in asyncLLM and set disable_log_stats=False, but I don't see any statistics associated with throughput, batch size.When using v0 AsyncLLMEngin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
