# vllm-project/vllm#15568: [Bug]: --api-key argument ignored when VLLM_API_KEY is set

| 字段 | 值 |
| --- | --- |
| Issue | [#15568](https://github.com/vllm-project/vllm/issues/15568) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: --api-key argument ignored when VLLM_API_KEY is set

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Example ```text VLLM_API_KEY=123 vllm serve --api-key ABC ``` Expected behavior: API Key = "ABC" Observed behavior: API Key = "123" Other environment variables should also be checked to ensure the expected precedence order is applied. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
