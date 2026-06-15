# vllm-project/vllm#28933: [Feature]: Structured request_id in logs and inclusion in error logs

| 字段 | 值 |
| --- | --- |
| Issue | [#28933](https://github.com/vllm-project/vllm/issues/28933) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Structured request_id in logs and inclusion in error logs

### Issue 正文摘录

# Structured request_id in logs and inclusion in error logs When sending a request with the `x-request-id` header, vLLM logs an entry like: ``` [2025-11-14 13:57:07] [INFO] [vllm.v1.engine.async_llm] Added request cmpl-833171a7b8c84e5eb20408b3e4fe2377 ``` This is quite useful for traceability, but it currently has two limitations. ## 1. `request_id` is not available as a structured logging field The `request_id` appears only inside the log message text, not as a dedicated log record field. This prevents using it in structured logging formats such as: ```json { "formatters": { "vllm": { "class": "vllm.logging_utils.NewLineFormatter", "datefmt": "%m-%d %H:%M:%S", "format": "%(levelname)s %(asctime)s %(filename)s:%(lineno)d %(request_id)s %(message)s" } } } ``` Since `request_id` is not part of the log record, any formatter referencing it fails. Adding `request_id` as an optional field in the logger would enable proper log correlation and integration with observability tools. ## 2. Error logs do not include the `request_id` If the request is valid, vLLM logs the “Added request …” line containing the `request_id`, as stated above. However, if the request fails before being accepted—e....

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: dedicated log record field. This prevents using it in structured logging formats such as: ```json { "formatters": { "vllm": { "class": "vllm.logging_utils.NewLineFormatter", "datefmt": "%m-%d %H:%M:%S", "format": "%(lev...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Structured request_id in logs and inclusion in error logs feature request;stale # Structured request_id in logs and inclusion in error logs When sending a request with the `x-request-id` header, vLLM logs an...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Since `request_id` is not part of the log record, any formatter referencing it fails. Adding `request_id` as an optional field in the logger would enable proper log correlation and integration with observability tools....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
