# vllm-project/vllm#29885: [Bug]: vllm-0.11.2 --enable-log-requests not print prompt

| 字段 | 值 |
| --- | --- |
| Issue | [#29885](https://github.com/vllm-project/vllm/issues/29885) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm-0.11.2 --enable-log-requests not print prompt

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm serve with `--enable-log-requests --enable-log-outputs` in vllm-0.11.0 ![Image](https://github.com/user-attachments/assets/ad36d668-bcd3-484a-9375-4476d3222bbe) in vllm-0.11.2 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: vllm-0.11.2 --enable-log-requests not print prompt bug ### Your current environment ### 🐛 Describe the bug vllm serve with `--enable-log-requests --enable-log-outputs` in vllm-0.11.0 ![Image](https://github.com/u...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
