# vllm-project/vllm#4963: [Misc]: How to get the string value of token in the output of logprobs?

| 字段 | 值 |
| --- | --- |
| Issue | [#4963](https://github.com/vllm-project/vllm/issues/4963) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: How to get the string value of token in the output of logprobs?

### Issue 正文摘录

I am passing in logprobs to the asyncllmengine, from my understanding this should generate [List[Dict[int, Logprob]]](https://github.com/vllm-project/vllm/blob/main/vllm/sequence.py#L37) but my output is ``` "logprobs": [ { "16622": -11.455507278442383, "29992": -1.5785541534423828, "29991": -2.023866653442383, "29892": -2.172304153442383, "14332": -2.809022903442383, "727": -3.367616653442383, "29889": -3.422304153442383, "1449": -3.789491653442383, "3186": -4.059022903442383, "322": -4.078554153442383, "10404": -4.101991653442383, "515": -4.187929153442383, "29899": -4.387147903442383, "29918": -4.637147903442383, "599": -4.769960403442383, "18239": -5.086366653442383, "474": -5.256288528442383, "26077": -5.281679153442383, "304": -5.527772903442383, "7875": -5.627382278442383, "732": -5.676210403442383 }, {... ] ``` which is a List[Dict[int, float]] Is this to be expected? How can I get the string value of the token instead of the token id?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
