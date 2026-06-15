# vllm-project/vllm#24096: [Feature]: Support extendable configuration files

| 字段 | 值 |
| --- | --- |
| Issue | [#24096](https://github.com/vllm-project/vllm/issues/24096) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support extendable configuration files

### Issue 正文摘录

### 🚀 The feature, motivation and pitch It's common to have different configuration files that essentially serve the same system with minor changes (i.e. using a different model or just changing the topology). While it is possible to provide these changes in the command line arguments, it would be nice to have the support for extending configuration files, so that you could have: "serve_azure.yml" - base config "serve_azure_qwen32.yml" - extends base with qwen32 model "serve_azure_Llama-3.2.yml" - extends base with Llama-3.2 model And instead of having to copy the same configurations both could have some key like "extends" to reference the base config and only change what is required. ### Alternatives The alternative solution could be the ability to specify multiple configuration files in serving args and merge their dictionaries, but then it might be a bit confusing when looking at the configuration files alone, or given the fact that the order for providing them will change the behavior ... ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: Support extendable configuration files feature request;stale ### 🚀 The feature, motivation and pitch It's common to have different configuration files that essentially serve the same system with minor changes...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support extendable configuration files feature request;stale ### 🚀 The feature, motivation and pitch It's common to have different configuration files that essentially serve the same system with minor changes...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: . ### Alternatives The alternative solution could be the ability to specify multiple configuration files in serving args and merge their dictionaries, but then it might be a bit confusing when looking at the configurati...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
