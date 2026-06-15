# vllm-project/vllm#2954: Qwen streaming inference leads to a significant decrease in accuracy

| 字段 | 值 |
| --- | --- |
| Issue | [#2954](https://github.com/vllm-project/vllm/issues/2954) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Qwen streaming inference leads to a significant decrease in accuracy

### Issue 正文摘录

The flow cytometry results of vllm for qwen7B or qwen14B are inconsistent with the original qwen results, resulting in an accuracy decrease of 10% -20%.

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: Qwen streaming inference leads to a significant decrease in accuracy The flow cytometry results of vllm for qwen7B or qwen14B are inconsistent with the original qwen results, resulting in an accuracy decrease of 10% -20...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Qwen streaming inference leads to a significant decrease in accuracy The flow cytometry results of vllm for qwen7B or qwen14B are inconsistent with the original qwen results, resulting in an accuracy decrease of 10% -20%
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Qwen streaming inference leads to a significant decrease in accuracy The flow cytometry results of vllm for qwen7B or qwen14B are inconsistent with the original qwen results, resulting in an accuracy decrease of 10% -20...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
