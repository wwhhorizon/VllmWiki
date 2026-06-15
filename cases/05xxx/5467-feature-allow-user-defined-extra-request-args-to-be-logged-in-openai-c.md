# vllm-project/vllm#5467: [Feature]: Allow user defined extra request args to be logged in OpenAI compatible server

| 字段 | 值 |
| --- | --- |
| Issue | [#5467](https://github.com/vllm-project/vllm/issues/5467) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Allow user defined extra request args to be logged in OpenAI compatible server

### Issue 正文摘录

### 🚀 The feature, motivation and pitch **Motivation** Using universal request ID/UUID when logging is common practice for production systems involving multiple components. My team wanted to use an UUID from upstream to trace logs produced by vLLM's OpenAI compatible webserver, but it doesn't seem like this is supported. Currently, vLLM generates its own UUID for each request, but it is 1. a separate ID, adding difficulty for tracing 2. the request ID does not always return to the API calling client, such as in cases of errors. **Solution** Allow extra args defined by the user to be passed in via a request to the OpenAI compatible frontend server, such that it can be propagated and logged via the logger. - Currently, the server will throw an error for the extra args passed via the request body. - The current proposal is to allow any extra args to be passed in via request body, and the extra args not matching supported args will just be logged during logging - See below for alternatives ### Alternatives - Alternatively, allow user to pass in extra args via request header instead of request body - Alternatively, allow user to pass all extra args via a single field (e.g. `"extra_args...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Allow user defined extra request args to be logged in OpenAI compatible server feature request;stale ### 🚀 The feature, motivation and pitch **Motivation** Using universal request ID/UUID when logging is comm...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: D for each request, but it is 1. a separate ID, adding difficulty for tracing 2. the request ID does not always return to the API calling client, such as in cases of errors. **Solution** Allow extra args defined by the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
