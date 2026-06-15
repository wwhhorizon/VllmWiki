# vllm-project/vllm#2139: How to provide api endpoint from running vllm on aws sagemaker without tunneling.

| 字段 | 值 |
| --- | --- |
| Issue | [#2139](https://github.com/vllm-project/vllm/issues/2139) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to provide api endpoint from running vllm on aws sagemaker without tunneling.

### Issue 正文摘录

Im using the code : `python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8888 --model mistralai/Mistral-7B-Instruct-v0.1` to run a model on on aws sagemaker terminal , i can access this via curl on another sagemaker terminal by : `curl http://0.0.0.0:8888/v1/completions -H "Content-Type: application/json" -d '{"model": "mistralai/Mistral-7B-Instruct-v0.1" prompt": "Paris is a","max_tokens": 7,"temperature": 0}'` works but when i try to access it from postman locally : by sending a post request to : http://38.216.54.823:8888/v1/completions where 38.216.54.823 is the same address of the sagemaker terminal where i am running the vllm server for the model. got by the code : `curl ipv4.icanhazip.com` with Body and POST request: {"model": "mistralai/Mistral-7B-Instruct-v0.1","prompt": "San Francisco is a","max_tokens": 7,"temperature": 0} It doesnt respond. How do i access the endpoint http://0.0.0.0:8888/v1/completions outside local without tunneling or if tunneling is absolutely necessary how do do it with aws services.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: uest: {"model": "mistralai/Mistral-7B-Instruct-v0.1","prompt": "San Francisco is a","max_tokens": 7,"temperature": 0} It doesnt respond. How do i access the endpoint http://0.0.0.0:8888/v1/completions outside local with...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ython -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8888 --model mistralai/Mistral-7B-Instruct-v0.1` to run a model on on aws sagemaker terminal , i can access this via curl on another sagemaker terminal b...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: s but when i try to access it from postman locally : by sending a post request to : http://38.216.54.823:8888/v1/completions where 38.216.54.823 is the same address of the sagemaker terminal where i am running the vllm...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
