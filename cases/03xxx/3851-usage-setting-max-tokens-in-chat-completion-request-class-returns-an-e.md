# vllm-project/vllm#3851: [Usage]: Setting max_tokens in chat completion request class returns an empty output

| 字段 | 值 |
| --- | --- |
| Issue | [#3851](https://github.com/vllm-project/vllm/issues/3851) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Setting max_tokens in chat completion request class returns an empty output

### Issue 正文摘录

### Your current environment I am using vllm version 0.3.0 I am using this class `ChatCompletionRequest` to create the request for my chat completion endpoint Whenever I set the `max_tokens` to any number and send a large prompt close in length to the `max_model_len` the endpoint sends and empty output with `status_code=200` Can you tell me how the `max_tokens` is used or related to the `max_model_len` or if I'm using it incorrectly altogether? ### How would you like to use vllm I am using vllm to create a chat_completions endpoint for inference purposes

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: urns an empty output usage ### Your current environment I am using vllm version 0.3.0 I am using this class `ChatCompletionRequest` to create the request for my chat completion endpoint Whenever I set the `max_tokens` t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: okens` to any number and send a large prompt close in length to the `max_model_len` the endpoint sends and empty output with `status_code=200` Can you tell me how the `max_tokens` is used or related to the `max_model_le...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Setting max_tokens in chat completion request class returns an empty output usage ### Your current environment I am using vllm version 0.3.0 I am using this class `ChatCompletionRequest` to create the request f...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
