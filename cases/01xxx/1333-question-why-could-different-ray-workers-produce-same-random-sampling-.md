# vllm-project/vllm#1333: Question: why could different ray.Workers produce same random sampling result when processing the same prob tensor?

| 字段 | 值 |
| --- | --- |
| Issue | [#1333](https://github.com/vllm-project/vllm/issues/1333) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Question: why could different ray.Workers produce same random sampling result when processing the same prob tensor?

### Issue 正文摘录

I am referring to the `_random_sample` method from `vllm/model_executor/layers/sampler.py`

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: me prob tensor? I am referring to the `_random_sample` method from `vllm/model_executor/layers/sampler.py`

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
