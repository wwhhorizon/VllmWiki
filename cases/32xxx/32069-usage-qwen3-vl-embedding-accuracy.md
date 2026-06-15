# vllm-project/vllm#32069: [Usage]: Qwen3-VL-Embedding Accuracy

| 字段 | 值 |
| --- | --- |
| Issue | [#32069](https://github.com/vllm-project/vllm/issues/32069) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Qwen3-VL-Embedding Accuracy

### Issue 正文摘录

Comparison testing between Qwen3-VL-Embedding-2B vLLM 13.0 and Qwen3VLEmbedder revealed inconsistencies in accuracy.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Usage]: Qwen3-VL-Embedding Accuracy usage Comparison testing between Qwen3-VL-Embedding-2B vLLM 13.0 and Qwen3VLEmbedder revealed inconsistencies in accuracy.
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Usage]: Qwen3-VL-Embedding Accuracy usage Comparison testing between Qwen3-VL-Embedding-2B vLLM 13.0 and Qwen3VLEmbedder revealed inconsistencies in accuracy.
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Qwen3-VL-Embedding-2B vLLM 13.0 and Qwen3VLEmbedder revealed inconsistencies in accuracy.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: Qwen3-VL-Embedding Accuracy usage Comparison testing between Qwen3-VL-Embedding-2B vLLM 13.0 and Qwen3VLEmbedder revealed inconsistencies in accuracy.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
