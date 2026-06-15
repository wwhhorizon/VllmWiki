# vllm-project/vllm#10949: [Bug]: Mismatch of tqdm when n > 1

| 字段 | 值 |
| --- | --- |
| Issue | [#10949](https://github.com/vllm-project/vllm/issues/10949) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Mismatch of tqdm when n > 1

### Issue 正文摘录

### Your current environment The progress of tqdm seems to be mismatched when n is not equal to 1. For example, if I run vllm on a dataset consisting of 1000 examples and set n = 5, tqdm displays as 0-5000, while it actually finishes when tqdm is loaded to 1000. ### Model Input Dumps - ### 🐛 Describe the bug - ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Mismatch of tqdm when n > 1 bug ### Your current environment The progress of tqdm seems to be mismatched when n is not equal to 1. For example, if I run vllm on a dataset consisting of 1000 examples and set n = 5...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: Mismatch of tqdm when n > 1 bug ### Your current environment The progress of tqdm seems to be mismatched when n is not equal to 1. For example, if I run vllm on a dataset consisting of 1000 examples and set n = 5...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: as 0-5000, while it actually finishes when tqdm is loaded to 1000. ### Model Input Dumps - ### 🐛 Describe the bug - ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and aske...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
