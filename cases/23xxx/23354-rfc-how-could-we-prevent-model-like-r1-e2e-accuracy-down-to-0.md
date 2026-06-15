# vllm-project/vllm#23354: [RFC] How could we prevent model like R1 E2E accuracy down to 0?

| 字段 | 值 |
| --- | --- |
| Issue | [#23354](https://github.com/vllm-project/vllm/issues/23354) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC] How could we prevent model like R1 E2E accuracy down to 0?

### Issue 正文摘录

Can we have any tests to prevent this kind of issues happening again? IIRC we had similar accuracy issues for deepseek several times before. _Originally posted by @WoosukKwon in https://github.com/vllm-project/vllm/issues/23294#issuecomment-3208293971_

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [RFC] How could we prevent model like R1 E2E accuracy down to 0? RFC Can we have any tests to prevent this kind of issues happening again? IIRC we had similar accuracy issues for deepseek several times before. _Original...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [RFC] How could we prevent model like R1 E2E accuracy down to 0? RFC Can we have any tests to prevent this kind of issues happening again? IIRC we had similar accuracy issues for deepseek several times before. _Original...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [RFC] How could we prevent model like R1 E2E accuracy down to 0? RFC Can we have any tests to prevent this kind of issues happening again? IIRC we had similar accuracy issues for deepseek several times before. _Original...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
