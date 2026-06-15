# vllm-project/vllm#1031: vllm sample 

| 字段 | 值 |
| --- | --- |
| Issue | [#1031](https://github.com/vllm-project/vllm/issues/1031) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vllm sample 

### Issue 正文摘录

When I use the sample method generate token, I find that I get the same result for multiple calculation processes. sampling_parameters: top_p=0.9, temperature=0.3,max_tokens=1024

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
