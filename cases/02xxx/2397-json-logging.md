# vllm-project/vllm#2397: JSON Logging

| 字段 | 值 |
| --- | --- |
| Issue | [#2397](https://github.com/vllm-project/vllm/issues/2397) |
| 状态 | closed |
| 标签 | help wanted;feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> JSON Logging

### Issue 正文摘录

It would be nice if the logging output can be configured to be JSON formatted. This is particularly useful when parsing logs with logging infrastructure.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nted;feature request;stale It would be nice if the logging output can be configured to be JSON formatted. This is particularly useful when parsing logs with logging infrastructure.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: JSON Logging help wanted;feature request;stale It would be nice if the logging output can be configured to be JSON formatted. This is particularly useful when parsing logs with logging infrastructure.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
