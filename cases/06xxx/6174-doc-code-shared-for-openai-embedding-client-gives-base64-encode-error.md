# vllm-project/vllm#6174: [Doc]: Code Shared for OpenAI Embedding Client gives base64 encode error

| 字段 | 值 |
| --- | --- |
| Issue | [#6174](https://github.com/vllm-project/vllm/issues/6174) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Code Shared for OpenAI Embedding Client gives base64 encode error

### Issue 正文摘录

### 📚 The doc issue The code given in the docs will always give error when someone is trying for first time to access embeding model hosted over vllm through openai api : https://docs.vllm.ai/en/latest/getting_started/examples/openai_embedding_client.html # Error BadRequestError: Error code: 400 - {'object': 'error', 'message': 'base64 encoding is not currently supported', 'type': 'BadRequestError', 'param': None, 'code': 400} Which is due to base64 encoding. # Erreneous code : from openai import OpenAI #Modify OpenAI's API key and API base to use vLLM's API server openai_api_key = "EMPTY" openai_api_base = "http://localhost:8000/v1" client = OpenAI( # defaults to os.environ.get("OPENAI_API_KEY") api_key=openai_api_key, base_url=openai_api_base, ) models = client.models.list() model = models.data[0].id responses = client.embeddings.create(input=[ "Hello my name is", "The best thing about vLLM is that it supports many different models" ], model=model) for data in responses.data: print(data.embedding) # list of float of len 4096 ### Suggest a potential alternative/fix # This can be easily fixed by explicitly passing encoding_format='float'. #Requesting the team to change the example...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 400} Which is due to base64 encoding. # Erreneous code : from openai import OpenAI #Modify OpenAI's API key and API base to use vLLM's API server openai_api_key = "EMPTY" openai_api_base = "http://localhost:8000/v1" cli...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ways give error when someone is trying for first time to access embeding model hosted over vllm through openai api : https://docs.vllm.ai/en/latest/getting_started/examples/openai_embedding_client.html # Error BadReques...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: test/getting_started/examples/openai_embedding_client.html # Error BadRequestError: Error code: 400 - {'object': 'error', 'message': 'base64 encoding is not currently supported', 'type': 'BadRequestError', 'param': None...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ng model hosted over vllm through openai api : https://docs.vllm.ai/en/latest/getting_started/examples/openai_embedding_client.html # Error BadRequestError: Error code: 400 - {'object': 'error', 'message': 'base64 encod...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
