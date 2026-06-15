# vllm-project/vllm#16653: [Feature]: Optimize performance for MLX/Metal/Apple Silicon

| 字段 | 值 |
| --- | --- |
| Issue | [#16653](https://github.com/vllm-project/vllm/issues/16653) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api |
| 子分类 | throughput |
| Operator 关键词 | cuda |
| 症状 | slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Optimize performance for MLX/Metal/Apple Silicon

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I'm using Mac Studio M3 Ultra to serve Qwen2.5-72B and performance is enough for personal use but the FTT is very long when the context length get larger and the throughput can't compare with cuda gpu. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: when the context length get larger and the throughput can't compare with cuda gpu. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already sea...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Optimize performance for MLX/Metal/Apple Silicon feature request;stale ### 🚀 The feature, motivation and pitch I'm using Mac Studio M3 Ultra to serve Qwen2.5-72B and performance is enough for personal use but...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: use but the FTT is very long when the context length get larger and the throughput can't compare with cuda gpu. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: he feature, motivation and pitch I'm using Mac Studio M3 Ultra to serve Qwen2.5-72B and performance is enough for personal use but the FTT is very long when the context length get larger and the throughput can't compare...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
