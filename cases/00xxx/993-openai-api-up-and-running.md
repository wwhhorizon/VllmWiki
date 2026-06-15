# vllm-project/vllm#993: Openai API - Up and running..

| 字段 | 值 |
| --- | --- |
| Issue | [#993](https://github.com/vllm-project/vllm/issues/993) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Openai API - Up and running..

### Issue 正文摘录

but it appears there is something missing here? very much appreciate some love here :) When using AutoGPT/Mentat/Aider(something that is looking fro chatgpt)...what are they looking for? INFO: 124.148.xxx.xxx:5xxx - "POST /v1/chat/completions HTTP/1.1" 404 Not Found Invalid response object from API: '{"object":"error","message":"The model `gpt-3.5-turbo-16k` does not exist.","type":"invalid_request_error","param":null,"code":null}' (HTTP response code was 404) curl works same endpoint? curl http://35.229.xxx.xx:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "meta-llama/Llama-2-7b-chat-hf", "messages": [ { "role": "system", "content": "You are a helpful assistant." }, { "role": "user", "content": "Who are you?" } ] }' INFO: 124.148.219.201:50922 - "POST /v1/chat/completions HTTP/1.1" 200 OK

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: und Invalid response object from API: '{"object":"error","message":"The model `gpt-3.5-turbo-16k` does not exist.","type":"invalid_request_error","param":null,"code":null}' (HTTP response code was 404) curl works same e...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: unning.. but it appears there is something missing here? very much appreciate some love here :) When using AutoGPT/Mentat/Aider(something that is looking fro chatgpt)...what are they looking for? INFO: 124.148.xxx.xxx:5...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: message":"The model `gpt-3.5-turbo-16k` does not exist.","type":"invalid_request_error","param":null,"code":null}' (HTTP response code was 404) curl works same endpoint? curl http://35.229.xxx.xx:8000/v1/chat/completion...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
