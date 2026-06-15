# vllm-project/vllm#17157: [Bug]:  GLM-Z1 uses vllm batch inference to output confusion

| 字段 | 值 |
| --- | --- |
| Issue | [#17157](https://github.com/vllm-project/vllm/issues/17157) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  GLM-Z1 uses vllm batch inference to output confusion

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Please review the relevant description here: https://github.com/THUDM/GLM-4/issues/762 When using GLM-Z1 for batch prediction, the results are chaotic, but predictions with single data entries are normal. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: al. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: GLM-Z1 uses vllm batch inference to output confusion bug;stale ### Your current environment ### 🐛 Describe the bug Please review the relevant description here: https://github.com/THUDM/GLM-4/issues/762 When using...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
