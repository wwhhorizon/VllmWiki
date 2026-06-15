# vllm-project/vllm#33874: [Bug]: GLM-OCR POST bug

| 字段 | 值 |
| --- | --- |
| Issue | [#33874](https://github.com/vllm-project/vllm/issues/33874) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GLM-OCR POST bug

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug If the image resolution exceeds 2300, there will be no response received after sending the POST request. After sending the POST request and checking the VLLM logs, it was found that no such POST request was received. 1.no response received after sending the POST request 2. no POST request was received 3.resolution exceeds 2300, there will be no response received after sending the POST request ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: exceeds 2300, there will be no response received after sending the POST request. After sending the POST request and checking the VLLM logs, it was found that no such POST request was received. 1.no response received aft...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
