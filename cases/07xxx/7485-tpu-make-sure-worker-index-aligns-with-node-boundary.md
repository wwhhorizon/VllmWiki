# vllm-project/vllm#7485: [TPU] Make sure worker index aligns with node boundary

| 字段 | 值 |
| --- | --- |
| Issue | [#7485](https://github.com/vllm-project/vllm/issues/7485) |
| 状态 | closed |
| 标签 | tpu |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [TPU] Make sure worker index aligns with node boundary

### Issue 正文摘录

In ray gpu executor, there are these lines: https://github.com/vllm-project/vllm/blob/7025b11d949b4efeb2584690c35f919c77027368/vllm/executor/ray_gpu_executor.py#L175-L191 to make sure the worker index aligns with machine boundary. you might need it in TPU, too. Otherwise local ranks can be wrong. for example, rank 0, 1, 2, 4 in one node, and 3, 5, 6, 7 in another node. _Originally posted by @youkaichao in https://github.com/vllm-project/vllm/issues/7457#issuecomment-2285381534_

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
