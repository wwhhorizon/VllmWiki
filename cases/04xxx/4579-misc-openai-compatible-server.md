# vllm-project/vllm#4579: [Misc]: openai compatible server

| 字段 | 值 |
| --- | --- |
| Issue | [#4579](https://github.com/vllm-project/vllm/issues/4579) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: openai compatible server

### Issue 正文摘录

### Anything you want to discuss about vllm. I have been using vllm for a while and i am really grateful to the community for all the features and improvement in this project! I am seeing a trend where features that are built mostly cater towards integrating with OpenAI-compatible API. One such example is the `guided_generation`, where the `guided_decoding` classes accepts OpenAI `ChatCompletionRequest` format. As someone who uses vllm with the default `api_server` entrypoint, i am curious why many of such features, including profiling of metrics are implemented with openai compatible integration in mind. What are the considerations when deciding on openai server over the default api server? One aspect i could think of is probably the wide usage of OpenAI API in many applications out there, hence, it will make more sense to provide such integration as a drop-in replacement.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: enai compatible integration in mind. What are the considerations when deciding on openai server over the default api server? One aspect i could think of is probably the wide usage of OpenAI API in many applications out...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ere the `guided_decoding` classes accepts OpenAI `ChatCompletionRequest` format. As someone who uses vllm with the default `api_server` entrypoint, i am curious why many of such features, including profiling of metrics...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: tion`, where the `guided_decoding` classes accepts OpenAI `ChatCompletionRequest` format. As someone who uses vllm with the default `api_server` entrypoint, i am curious why many of such features, including profiling of...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: pi_server` entrypoint, i am curious why many of such features, including profiling of metrics are implemented with openai compatible integration in mind. What are the considerations when deciding on openai server over t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
