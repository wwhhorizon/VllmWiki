# vllm-project/vllm#37271: [Bug]: In_proj_ba of GDN in Qwen3Next use MergeColumnParallelLinear may cause accuracy decrease?

| 字段 | 值 |
| --- | --- |
| Issue | [#37271](https://github.com/vllm-project/vllm/issues/37271) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: In_proj_ba of GDN in Qwen3Next use MergeColumnParallelLinear may cause accuracy decrease?

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I found that in_proj_ba is a MergeColumnParallelLinear now, and it was a ColumnParallelLinear before. It leads to a different way of weight loading. And it will cause accuracy decrease on gsm8k dataset. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: different way of weight loading. And it will cause accuracy decrease on gsm8k dataset. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the b...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: : In_proj_ba of GDN in Qwen3Next use MergeColumnParallelLinear may cause accuracy decrease? bug ### Your current environment ### 🐛 Describe the bug I found that in_proj_ba is a MergeColumnParallelLinear now, and it was...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: : In_proj_ba of GDN in Qwen3Next use MergeColumnParallelLinear may cause accuracy decrease? bug ### Your current environment ### 🐛 Describe the bug I found that in_proj_ba is a MergeColumnParallelLinear now, and it was...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: In_proj_ba of GDN in Qwen3Next use MergeColumnParallelLinear may cause accuracy decrease? bug ### Your current environment ### 🐛 Describe the bug I found that in_proj_ba is a MergeColumnParallelLinear now, and it...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
