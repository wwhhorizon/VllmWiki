# vllm-project/vllm#9106: [Usage]: chat 接口有问题，completion接口正常

| 字段 | 值 |
| --- | --- |
| Issue | [#9106](https://github.com/vllm-project/vllm/issues/9106) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: chat 接口有问题，completion接口正常

### Issue 正文摘录

### Your current environment ```text vllm serve /mnt/workspace/hx/Models/Llama-3.1-8B-Instruct --chat-template /mnt/workspace/hx/Models/Llama-3.1-8B-Instruct/llama31.jinja --served-model-name llama3.1-8b-instruct ``` ### How would you like to use vllm 按照官方文档调用，用completion方式就没问题，用chat方式就有问题 这是chat方式的，报错了 ```from openai import OpenAI # Set OpenAI's API key and API base to use vLLM's API server. openai_api_key = "EMPTY" openai_api_base = "http://localhost:8000/v1" client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) chat_response = client.chat.completions.create( model="llama3.1-8b-instruct", messages=[ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Tell me a joke."}, ] ) print("Chat response:", chat_response) ``` ``` Traceback (most recent call last): File " ", line 11, in File "/mnt/workspace/hx/anaconda3/envs/coling/lib/python3.10/site-packages/openai/_utils/_utils.py", line 274, in wrapper return func(*args, **kwargs) File "/mnt/workspace/hx/anaconda3/envs/coling/lib/python3.10/site-packages/openai/resources/chat/completions.py", line 668, in create return self._post( File "/mnt/workspace/hx/anaconda3/envs/coling/lib/py...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: m 按照官方文档调用，用completion方式就没问题，用chat方式就有问题 这是chat方式的，报错了 ```from openai import OpenAI # Set OpenAI's API key and API base to use vLLM's API server. openai_api_key = "EMPTY" openai_api_base = "http://localhost:8000/v1" cli...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: usage ### Your current environment ```text vllm serve /mnt/workspace/hx/Models/Llama-3.1-8B-Instruct --chat-template /mnt/workspace/hx/Models/Llama-3.1-8B-Instruct/llama31.jinja --served-model-name llama3.1-8b-instruct...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nai/_base_client.py", line 1260, in post return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls)) File "/mnt/workspace/hx/anaconda3/envs/coling/lib/python3.10/site-packages/openai/_base_...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
