# vllm-project/vllm#16204: [Bug]: github-action bot have a error

| 字段 | 值 |
| --- | --- |
| Issue | [#16204](https://github.com/vllm-project/vllm/issues/16204) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: github-action bot have a error

### Issue 正文摘录

### Your current environment When I submit a PR and write some comments, they will be cleared by github-action bot after submission. I don’t know if other people have encountered similar problems. ![Image](https://github.com/user-attachments/assets/54dc4b1a-89c8-496d-a83b-0d1444e76e68) ![Image](https://github.com/user-attachments/assets/020d2370-f7bd-46cd-b28f-7baa94c03d8b) ### 🐛 Describe the bug nothing ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ing ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
