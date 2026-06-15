# vllm-project/vllm#23072: [Bug]: eagle3 draft model len > 2048 will be broken

| 字段 | 值 |
| --- | --- |
| Issue | [#23072](https://github.com/vllm-project/vllm/issues/23072) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: eagle3 draft model len > 2048 will be broken

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I trained an Eagle3 draft model that supports 8K length, it runs normally when using --enforce-eager. However, when I do not use this parameter, I get a kernel error. The current kernel only supports 2048 lengths and does not support longer lengths. How can I modify the kernel to support lengths greater than 2048? Thanks a lot. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: eagle3 draft model len > 2048 will be broken bug;stale ### Your current environment ### 🐛 Describe the bug When I trained an Eagle3 draft model that supports 8K length, it runs normally when using --enforce-eager...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ot. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: eagle3 draft model len > 2048 will be broken bug;stale ### Your current environment ### 🐛 Describe the bug When I trained an Eagle3 draft model that supports 8K length, it runs normally when using --enforce-eager...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
