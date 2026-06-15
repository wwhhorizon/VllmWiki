# vllm-project/vllm#1462: cumulatve log_probs not available anymore

| 字段 | 值 |
| --- | --- |
| Issue | [#1462](https://github.com/vllm-project/vllm/issues/1462) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> cumulatve log_probs not available anymore

### Issue 正文摘录

Is this the prefered way to not calculate the cumulative_logprob? In [v0.2.0](https://github.com/vllm-project/vllm/releases/tag/v0.2.0) they were available in [v0.2.1](https://github.com/vllm-project/vllm/releases/tag/v0.2.1) removed. It is always returning 0.0 with awq quant

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: vllm/releases/tag/v0.2.1) removed. It is always returning 0.0 with awq quant

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
