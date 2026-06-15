# vllm-project/vllm#1202: Greedy decoding generates different outputs

| 字段 | 值 |
| --- | --- |
| Issue | [#1202](https://github.com/vllm-project/vllm/issues/1202) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Greedy decoding generates different outputs

### Issue 正文摘录

I have tried the same prompt to run 100 times with temp=0, top_p=1, I did not get the same results for 100 times. But there are a few dominated outputs there. My understanding is that with the setup, greedy decoding should generate the same outputs with the same prompt. But this is not what I observed.

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: Greedy decoding generates different outputs I have tried the same prompt to run 100 times with temp=0, top_p=1, I did not get the same results for 100 times. But there are a few dominated outputs there. My understanding...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
