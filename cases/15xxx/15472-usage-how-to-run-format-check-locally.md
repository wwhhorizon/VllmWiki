# vllm-project/vllm#15472: [Usage]: How to run format check locally?

| 字段 | 值 |
| --- | --- |
| Issue | [#15472](https://github.com/vllm-project/vllm/issues/15472) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to run format check locally?

### Issue 正文摘录

### Your current environment ![Image](https://github.com/user-attachments/assets/02a0661c-a93c-4e8c-9e7f-f66f68c005d4) ![Image](https://github.com/user-attachments/assets/3e407b8b-52b1-4e2e-9963-e15a41b368e5) ### How would you like to use vllm I can pass the pre-commit format test on my machine, however the check in ci failed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: can pass the pre-commit format test on my machine, however the check in ci failed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the botto...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: How to run format check locally? usage ### Your current environment ![Image](https://github.com/user-attachments/assets/02a0661c-a93c-4e8c-9e7f-f66f68c005d4) ![Image](https://github.com/user-attachments/assets/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 5) ### How would you like to use vllm I can pass the pre-commit format test on my machine, however the check in ci failed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
