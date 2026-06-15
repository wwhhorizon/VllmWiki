# vllm-project/vllm#1787: Is SequenceOutputs indeed SequenceOutput (removing the s suffix)?

| 字段 | 值 |
| --- | --- |
| Issue | [#1787](https://github.com/vllm-project/vllm/issues/1787) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Is SequenceOutputs indeed SequenceOutput (removing the s suffix)?

### Issue 正文摘录

Based on the implementation, it appears that each `SequenceOutputs` object represents [a single token rather than multiple tokens generated from a sequence](https://github.com/vllm-project/vllm/blob/7c600440f7560348e571f021f2b2d1469de5264d/vllm/sequence.py#L373). In light of this, should the class be renamed to `SequenceOutput` by removing the 's' suffix to more accurately reflect its functionality? In the same way, `SequenceGroupOutputs` should be `SequenceGroupOutput` and `SamplerOutput` could be `SequenceGroupOutputs`?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
