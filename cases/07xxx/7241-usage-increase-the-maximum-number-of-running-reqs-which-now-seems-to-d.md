# vllm-project/vllm#7241: [Usage]: Increase the maximum number of running reqs, which now seems to default to 100

| 字段 | 值 |
| --- | --- |
| Issue | [#7241](https://github.com/vllm-project/vllm/issues/7241) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Increase the maximum number of running reqs, which now seems to default to 100

### Issue 正文摘录

### Your current environment How do I increase the maximum number of concurrent reqs, which now seems to default to 100 ### How would you like to use vllm The current command is as following: ``` python -m vllm.entrypoints.openai api_server ——enable-prefix-caching ——disable-log-request ```

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: maximum number of running reqs, which now seems to default to 100 usage;stale ### Your current environment How do I increase the maximum number of concurrent reqs, which now seems to default to 100 ### How would you lik...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
