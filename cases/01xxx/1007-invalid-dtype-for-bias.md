# vllm-project/vllm#1007: invalid dtype for bias

| 字段 | 值 |
| --- | --- |
| Issue | [#1007](https://github.com/vllm-project/vllm/issues/1007) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> invalid dtype for bias

### Issue 正文摘录

RuntimeError: invalid dtype for bias - should match query's dtype

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: invalid dtype for bias RuntimeError: invalid dtype for bias - should match query's dtype

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
