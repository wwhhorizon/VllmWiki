# vllm-project/vllm#101: Add tests for models

| 字段 | 值 |
| --- | --- |
| Issue | [#101](https://github.com/vllm-project/vllm/issues/101) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Add tests for models

### Issue 正文摘录

We need tests for the models we support. The tests should ensure that the outputs of our models when using greedy sampling are equivalent to those of HF models.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Add tests for models We need tests for the models we support. The tests should ensure that the outputs of our models when using greedy sampling are equivalent to those of HF models.
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Add tests for models We need tests for the models we support. The tests should ensure that the outputs of our models when using greedy sampling are equivalent to those of HF models.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
