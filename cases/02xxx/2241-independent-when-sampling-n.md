# vllm-project/vllm#2241: Independent when sampling n?

| 字段 | 值 |
| --- | --- |
| Issue | [#2241](https://github.com/vllm-project/vllm/issues/2241) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Independent when sampling n?

### Issue 正文摘录

I have a question regarding `generate`. and `sampling_params`. If I'm trying to generate with the following params: ``` stop_tokens = [" ", " "] SamplingParams(temperature=0.7, top_p=1, max_tokens=512, stop=stop_tokens, n=100) # some large number. ``` Then, is the quality of these generated N samples independent of each other?

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
