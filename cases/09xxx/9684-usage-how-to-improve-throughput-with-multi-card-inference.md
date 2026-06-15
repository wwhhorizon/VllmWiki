# vllm-project/vllm#9684: [Usage]: How to improve throughput with multi-card inference？

| 字段 | 值 |
| --- | --- |
| Issue | [#9684](https://github.com/vllm-project/vllm/issues/9684) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to improve throughput with multi-card inference？

### Issue 正文摘录

### Your current environment ![cpuinfo](https://github.com/user-attachments/assets/3ae887a0-ce7b-49e7-9651-de14cc77155a) ![gpuinfo](https://github.com/user-attachments/assets/9ef5b0cf-281b-4320-9902-b5f2fe91e3e5) ![ncclinfo](https://github.com/user-attachments/assets/4dc79b29-7408-48d1-a110-5bfeda1b611c) ### How would you like to use vllm At present, the throughput of Vincent model inference has not been significantly improved by increasing graphics card resources. What can I do to improve this indicator? ![test](https://github.com/user-attachments/assets/71bddfc1-25ec-4486-b3de-b5c9833d4a2b) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Usage]: How to improve throughput with multi-card inference？ usage;stale ### Your current environment ![cpuinfo](https://github.com/user-attachments/assets/3ae887a0-ce7b-49e7-9651-de14cc77155a) ![gpuinfo](https://githu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 2b) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ## How would you like to use vllm At present, the throughput of Vincent model inference has not been significantly improved by increasing graphics card resources. What can I do to improve this indicator? ![test](https:/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: How to improve throughput with multi-card inference？ usage;stale ### Your current environment ![cpuinfo](https://github.com/user-attachments/assets/3ae887a0-ce7b-49e7-9651-de14cc77155a) ![gpuinfo](https://githu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
