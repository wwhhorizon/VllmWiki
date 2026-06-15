# vllm-project/vllm#10900: [Bug]: tool_chat_template_mistral_parallel.jinja does not trim tool_call_id to 9 digits when using async stream

| 字段 | 值 |
| --- | --- |
| Issue | [#10900](https://github.com/vllm-project/vllm/issues/10900) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: tool_chat_template_mistral_parallel.jinja does not trim tool_call_id to 9 digits when using async stream

### Issue 正文摘录

### Your current environment image: vllm/vllm-openai:v0.6.4.post1 command: "--model /model --served-model-name mistral-large-123b --tensor-parallel-size 4 --port 8081 --tokenizer_mode mistral --load_format safetensors --config_format mistral --chat-template templates/extended_tool_chat_template_mistral_parallel.jinja --enable-auto-tool-choice --tool-call-parser mistral" ### Model Input Dumps Traceback (most recent call last): File "/usr/local/lib/python3.12/dist-packages/uvicorn/protocols/http/httptools_impl.py", line 401, in run_asgi result = await app( # type: ignore[func-returns-value] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__ return await self.app(scope, receive, send) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/fastapi/applications.py", line 1054, in __call__ await super().__call__(scope, receive, send) File "/usr/local/lib/python3.12/dist-packages/starlette/applications.py", line 113, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.12/dist-packages/starlette/middleware/errors.py", line...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ur current environment image: vllm/vllm-openai:v0.6.4.post1 command: "--model /model --served-model-name mistral-large-123b --tensor-parallel-size 4 --port 8081 --tokenizer_mode mistral --load_format safetensors --confi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: tte/middleware/base.py", line 187, in __call__ response = await self.dispatch_func(request, call_next) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lse ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: stream_mode="values"), which does call the API with stream mode set to False ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom righ...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ceive, sender) File "/usr/local/lib/python3.12/dist-packages/starlette/routing.py", line 715, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.12/dist-packages/starlette/routing...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
