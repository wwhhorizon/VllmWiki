# vllm-project/vllm#4747: [Usage]: prompt_logprompt from endpoint

| 字段 | 值 |
| --- | --- |
| Issue | [#4747](https://github.com/vllm-project/vllm/issues/4747) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: prompt_logprompt from endpoint

### Issue 正文摘录

### Your current environment I want to get the logprobs from a vLLM endpoint on the prompt + answer in order to evaluate the LLM on selective task. How can I do that? ``` curl --location URL/v1/chat/completions \ --header "Content-Type: application/json" \ --data '{ "model": "model_name", "echo": true, "messages": [ { "role": "user", "content": "hello"} ], "logprobs": true, "top_logprobs": 1 }' ``` I am using this code but I get only the logprobs of the answer. Can anyone help please? ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: e? ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: at/completions \ --header "Content-Type: application/json" \ --data '{ "model": "model_name", "echo": true, "messages": [ { "role": "user", "content": "hello"} ], "logprobs": true, "top_logprobs": 1 }' ``` I am using th...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: prompt_logprompt from endpoint usage;stale ### Your current environment I want to get the logprobs from a vLLM endpoint on the prompt + answer in order to evaluate the LLM on selective task. How can I do that?...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: get the logprobs from a vLLM endpoint on the prompt + answer in order to evaluate the LLM on selective task. How can I do that? ``` curl --location URL/v1/chat/completions \ --header "Content-Type: application/json" \ -...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
