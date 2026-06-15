# vllm-project/vllm#1465: Failed to connect to GCS within 60 seconds

| 字段 | 值 |
| --- | --- |
| Issue | [#1465](https://github.com/vllm-project/vllm/issues/1465) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Failed to connect to GCS within 60 seconds

### Issue 正文摘录

my env: `vllm: 0.2.1-post` `ray: 2.7.1` and everything is ok when I run with `tensor_parallel_size=1` but something goes wrong when I set `tensor_parallel_size=2` > gcs_rpc_client.h:552: Failed to connect to GCS within 60 seconds. GCS may have been killed. It's either GCS is terminated by `ray stop` or is killed unexpectedly. And my hardware is a single machine with two A10 cards. Can someone help me plz?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
