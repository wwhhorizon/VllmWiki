# vllm-project/vllm#15781: [Feature]: Implementation of Zero Overhead Scheduling

| 字段 | 值 |
| --- | --- |
| Issue | [#15781](https://github.com/vllm-project/vllm/issues/15781) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Implementation of Zero Overhead Scheduling

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I have implemented zero overhead scheduling and I would like to submit the PR to you. I don't know how you plan it here. Is anyone currently developing this logic? This is a performance analysis chart before and after the implementation of zero overhead scheduling, where all kernels are distributed to computing devices in advance. Excluding scheduling overhead, the performance improvement ranges from approximately 1% to 10% for different sizes. ![Image](https://github.com/user-attachments/assets/d2b4d2ba-0771-4625-b517-c9450e5ab8df) ![Image](https://github.com/user-attachments/assets/5988b31f-ac2b-4808-b465-eb66452d5646) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Implementation of Zero Overhead Scheduling feature request;stale ### 🚀 The feature, motivation and pitch I have implemented zero overhead scheduling and I would like to submit the PR to you. I don't know how...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
