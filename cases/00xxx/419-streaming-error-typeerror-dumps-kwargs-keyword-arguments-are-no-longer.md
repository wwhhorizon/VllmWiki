# vllm-project/vllm#419: Streaming Error: TypeError: `dumps_kwargs` keyword arguments are no longer supported.

| 字段 | 值 |
| --- | --- |
| Issue | [#419](https://github.com/vllm-project/vllm/issues/419) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Streaming Error: TypeError: `dumps_kwargs` keyword arguments are no longer supported.

### Issue 正文摘录

Receiving the following when attempting to enable streaming on the server. The model returns successfully without streaming (ie stream key removed)! This worked in the past but vllm 0.1.2 RTXA6000 Docker startup script ``` bash -c 'pip install --upgrade huggingface_hub && huggingface-cli login --token $HUGGINGFACE_TOKEN && pip install vllm && python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8000 --model my_model --tokenizer hf-internal-testing/llama-tokenizer' ``` Prompt ``` { "model": "my_model", "prompt": "###System: You are world class assistant. Answer the question, provide solutions, and justify your reasoning step by step. \n ###Human: Hello. \n ###Assistant:", "max_tokens": 1000, "temperature": 0.7, "user": "test-user-id", "stream": true } ``` Error ``` 2023-07-10T20:53:51.940730783Z ERROR: Exception in ASGI application 2023-07-10T20:53:51.940756172Z Traceback (most recent call last): 2023-07-10T20:53:51.940758164Z File "/usr/local/lib/python3.10/dist-packages/uvicorn/protocols/http/h11_impl.py", line 428, in run_asgi 2023-07-10T20:53:51.940760457Z result = await app( # type: ignore[func-returns-value] 2023-07-10T20:53:51.940762539Z File "/usr/local/lib/py...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ng the following when attempting to enable streaming on the server. The model returns successfully without streaming (ie stream key removed)! This worked in the past but vllm 0.1.2 RTXA6000 Docker startup script ``` bas...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: tream key removed)! This worked in the past but vllm 0.1.2 RTXA6000 Docker startup script ``` bash -c 'pip install --upgrade huggingface_hub && huggingface-cli login --token $HUGGINGFACE_TOKEN && pip install vllm && pyt...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: :51.940799902Z File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 718, in __call__ 2023-07-10T20:53:51.940801419Z await route.handle(scope, receive, send) 2023-07-10T20:53:51.940802971Z File "/usr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ming (ie stream key removed)! This worked in the past but vllm 0.1.2 RTXA6000 Docker startup script ``` bash -c 'pip install --upgrade huggingface_hub && huggingface-cli login --token $HUGGINGFACE_TOKEN && pip install v...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: -10T20:53:51.940836571Z response_json = response.json(ensure_ascii=False) 2023-07-10T20:53:51.940838017Z File "/usr/local/lib/python3.10/dist-packages/typing_extensions.py", line 2562, in wrapper 2023-07-10T20:53:51.940...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
