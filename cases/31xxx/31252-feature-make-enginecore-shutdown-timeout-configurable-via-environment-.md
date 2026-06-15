# vllm-project/vllm#31252: [Feature]: Make EngineCore shutdown timeout configurable via environment variable

| 字段 | 值 |
| --- | --- |
| Issue | [#31252](https://github.com/vllm-project/vllm/issues/31252) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Make EngineCore shutdown timeout configurable via environment variable

### Issue 正文摘录

### 🚀 The feature, motivation and pitch **Description:** When adding cleanup work for the Connector during vLLM shutdown, the cleanup is interrupted halfway because the EngineCore process is terminated by the api server process. Currently, the shutdown function called by the api server only provides a fixed 5-second timeout for the EngineCore process. This fixed timeout is insufficient for cleanup operations that may take longer. **Proposed Solution:** Make the EngineCore shutdown timeout configurable via an environment variable, allowing users to adjust it based on their cleanup requirements. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ngineCore shutdown timeout configurable via environment variable feature request;stale ### 🚀 The feature, motivation and pitch **Description:** When adding cleanup work for the Connector during vLLM shutdown, the cleanu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: -second timeout for the EngineCore process. This fixed timeout is insufficient for cleanup operations that may take longer. **Proposed Solution:** Make the EngineCore shutdown timeout configurable via an environment var...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Make EngineCore shutdown timeout configurable via environment variable feature request;stale ### 🚀 The feature, motivation and pitch **Description:** When adding cleanup work for the Connector during vLLM shu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
