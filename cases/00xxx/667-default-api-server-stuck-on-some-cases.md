# vllm-project/vllm#667: Default api server stuck on some cases

| 字段 | 值 |
| --- | --- |
| Issue | [#667](https://github.com/vllm-project/vllm/issues/667) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Default api server stuck on some cases

### Issue 正文摘录

As title, default api server stuck on some samples. It might related to #633 I can locate that the process get stuck in the here since a timeout error. And increasing `TIMEOUT_TO_PREVENT_DEADLOCK` could reduce the chances that server get stuck. Any chance to fix this? https://github.com/vllm-project/vllm/blob/aa84c92ef636e689b506b9842c712e5c615cc73a/vllm/engine/async_llm_engine.py#L136-L160

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ck in the here since a timeout error. And increasing `TIMEOUT_TO_PREVENT_DEADLOCK` could reduce the chances that server get stuck. Any chance to fix this? https://github.com/vllm-project/vllm/blob/aa84c92ef636e689b506b9...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
