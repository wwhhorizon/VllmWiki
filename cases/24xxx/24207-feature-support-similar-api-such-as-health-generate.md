# vllm-project/vllm#24207: [Feature]: Support similar API, such as /health_generate

| 字段 | 值 |
| --- | --- |
| Issue | [#24207](https://github.com/vllm-project/vllm/issues/24207) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support similar API, such as /health_generate

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, there is a health check endpoint called /health. Could we add another endpoint /health_generate? The purpose of this endpoint would be to have the model perform inference to generate a token, thereby confirming that the service can perform inference normally and avoiding situations where it appears alive but is actually unresponsive. Health Check /health: Check the health of the server. /health_generate: Check the health of the server by generating one token. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support similar API, such as /health_generate feature request;stale ### 🚀 The feature, motivation and pitch Currently, there is a health check endpoint called /health. Could we add another endpoint /health_ge...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: oint /health_generate? The purpose of this endpoint would be to have the model perform inference to generate a token, thereby confirming that the service can perform inference normally and avoiding situations where it a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
