# vllm-project/vllm#16296: [Bug]: TP4 Accuracy Worse Than TP8 for LLaMa4

| 字段 | 值 |
| --- | --- |
| Issue | [#16296](https://github.com/vllm-project/vllm/issues/16296) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: TP4 Accuracy Worse Than TP8 for LLaMa4

### Issue 正文摘录

### Your current environment N/A ### 🐛 Describe the bug We are aware of Scout performing worse on MMLU Pro, GSM8K on TP4 and are actively debugging those. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 🐛 Describe the bug We are aware of Scout performing worse on MMLU Pro, GSM8K on TP4 and are actively debugging those. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and as...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: TP4 Accuracy Worse Than TP8 for LLaMa4 bug ### Your current environment N/A ### 🐛 Describe the bug We are aware of Scout performing worse on MMLU Pro, GSM8K on TP4 and are actively debugging those. ### Before sub...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: TP4 Accuracy Worse Than TP8 for LLaMa4 bug ### Your current environment N/A ### 🐛 Describe the bug We are aware of Scout performing worse on MMLU Pro, GSM8K on TP4 and are actively debugging those. ### Before sub...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: TP4 Accuracy Worse Than TP8 for LLaMa4 bug ### Your current environment N/A ### 🐛 Describe the bug We are aware of Scout performing worse on MMLU Pro, GSM8K on TP4 and are actively debugging those. ### Before sub...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
