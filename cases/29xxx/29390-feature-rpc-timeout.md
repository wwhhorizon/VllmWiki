# vllm-project/vllm#29390: [Feature]: rpc timeout

| 字段 | 值 |
| --- | --- |
| Issue | [#29390](https://github.com/vllm-project/vllm/issues/29390) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: rpc timeout

### Issue 正文摘录

### 🚀 The feature, motivation and pitch there is no way to set timeout for vllm.v1.executor.multiproc_executor.MultiprocExecutor.collective_rpc it is a bit uncomfortable to debug model. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: rpc timeout feature request;stale ### 🚀 The feature, motivation and pitch there is no way to set timeout for vllm.v1.executor.multiproc_executor.MultiprocExecutor.collective_rpc it is a bit uncomfortable to d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tor.MultiprocExecutor.collective_rpc it is a bit uncomfortable to debug model. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searche...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
