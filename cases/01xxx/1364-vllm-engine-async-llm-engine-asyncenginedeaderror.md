# vllm-project/vllm#1364: vllm.engine.async_llm_engine.AsyncEngineDeadError

| 字段 | 值 |
| --- | --- |
| Issue | [#1364](https://github.com/vllm-project/vllm/issues/1364) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vllm.engine.async_llm_engine.AsyncEngineDeadError

### Issue 正文摘录

Task finished unexpectedly. This should never happen! Please open an issue on Github. See stack trace above for the actual cause. INFO 10-16 04:29:09 async_llm_engine.py:134] Aborted request cmpl-3c72dd29170e41ca93c2acbfabe2f326. I can provide full stack trace of need be

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: r the actual cause. INFO 10-16 04:29:09 async_llm_engine.py:134] Aborted request cmpl-3c72dd29170e41ca93c2acbfabe2f326. I can provide full stack trace of need be

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
