# vllm-project/vllm#2955: The inference result of vllm's qwen is inconsistent with the original qwen result

| 字段 | 值 |
| --- | --- |
| Issue | [#2955](https://github.com/vllm-project/vllm/issues/2955) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> The inference result of vllm's qwen is inconsistent with the original qwen result

### Issue 正文摘录

The streaming results/service results/inference of vllm qwen7B/qwen14B are inconsistent with the original qwen results (accuracy decreases). Accuracy decreases by 10-20%, which is a significant decrease

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: of vllm qwen7B/qwen14B are inconsistent with the original qwen results (accuracy decreases). Accuracy decreases by 10-20%, which is a significant decrease
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: The inference result of vllm's qwen is inconsistent with the original qwen result The streaming results/service results/inference of vllm qwen7B/qwen14B are inconsistent with the original qwen results (accuracy decrease...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: of vllm qwen7B/qwen14B are inconsistent with the original qwen results (accuracy decreases). Accuracy decreases by 10-20%, which is a significant decrease

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
