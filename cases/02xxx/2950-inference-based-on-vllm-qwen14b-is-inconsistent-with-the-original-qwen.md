# vllm-project/vllm#2950: Inference based on vllm qwen14B is inconsistent with the original qwen results, and the accuracy will drop significantly

| 字段 | 值 |
| --- | --- |
| Issue | [#2950](https://github.com/vllm-project/vllm/issues/2950) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Inference based on vllm qwen14B is inconsistent with the original qwen results, and the accuracy will drop significantly

### Issue 正文摘录

Inference based on vllm qwen14B is inconsistent with the original qwen results, and the accuracy will drop significantly

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: on vllm qwen14B is inconsistent with the original qwen results, and the accuracy will drop significantly Inference based on vllm qwen14B is inconsistent with the original qwen results, and the accuracy will drop signifi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Inference based on vllm qwen14B is inconsistent with the original qwen results, and the accuracy will drop significantly Inference based on vllm qwen14B is inconsistent with the original qwen results, and the accuracy w...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: on vllm qwen14B is inconsistent with the original qwen results, and the accuracy will drop significantly Inference based on vllm qwen14B is inconsistent with the original qwen results, and the accuracy will drop signifi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
