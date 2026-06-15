# vllm-project/vllm#286: Long context will cause the vLLM stop

| 字段 | 值 |
| --- | --- |
| Issue | [#286](https://github.com/vllm-project/vllm/issues/286) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Long context will cause the vLLM stop

### Issue 正文摘录

If I exceed the token limit of 4096, the vLLM abruptly stops. It would be helpful if you could incorporate some logging functionality into the stopping code. This way, users can easily modify the code to resume the vLLM from where it left off.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
