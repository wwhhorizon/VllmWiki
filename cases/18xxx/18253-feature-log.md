# vllm-project/vllm#18253: [Feature]: log

| 字段 | 值 |
| --- | --- |
| Issue | [#18253](https://github.com/vllm-project/vllm/issues/18253) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: log

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Why is the log constantly being output after deployment ![Image](https://github.com/user-attachments/assets/0e494c2d-35c6-4455-b5a3-c1866b1767f8) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: log feature request ### 🚀 The feature, motivation and pitch Why is the log constantly being output after deployment ![Image](https://github.com/user-attachments/assets/0e494c2d-35c6-4455-b5a3-c1866b1767f8) ##...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
