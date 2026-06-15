# vllm-project/vllm#2179: tmp directory gets locked by other user

| 字段 | 值 |
| --- | --- |
| Issue | [#2179](https://github.com/vllm-project/vllm/issues/2179) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> tmp directory gets locked by other user

### Issue 正文摘录

It seems if mulitiple users using vllm on the same machine, there is a problem with a file.lock. PermissionError: [Errno 13] Permission denied: '/tmp/XXX-XXX-7b-chat.lock' Can you add a random number or timestamp to these lock files? (weights_utils.py: line 141) Thx. Best Regards. Matthias

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
