# vllm-project/vllm#19933: [Bug]: The vllm/vllm-openai version 0.9.1 is nearly 30% faster compared to lmsysorg/sglang:v0.4.7.post, but it stops running every two to three hours.

| 字段 | 值 |
| --- | --- |
| Issue | [#19933](https://github.com/vllm-project/vllm/issues/19933) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The vllm/vllm-openai version 0.9.1 is nearly 30% faster compared to lmsysorg/sglang:v0.4.7.post, but it stops running every two to three hours.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ray error ![Image](https://github.com/user-attachments/assets/f380c593-e7a8-471b-bd3f-dfe505cf6331) env Two 8-GPU servers with 96GB H20 each ![Image](https://github.com/user-attachments/assets/c2cae191-efbe-43e2-b579-579e8dc29b25) ![Image](https://github.com/user-attachments/assets/a57400c9-17c7-4624-af18-5431d8603453) ![Image](https://github.com/user-attachments/assets/fcfc9ddb-8e0d-4660-a0ac-e5d2a4a681a1) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: The vllm/vllm-openai version 0.9.1 is nearly 30% faster compared to lmsysorg/sglang:v0.4.7.post, but it stops running every two to three hours. bug;stale ### Your current environment ### 🐛 Describe the bug ray er...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: a1) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: g/sglang:v0.4.7.post, but it stops running every two to three hours. bug;stale ### Your current environment ### 🐛 Describe the bug ray error ![Image](https://github.com/user-attachments/assets/f380c593-e7a8-471b-bd3f-df...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
