# vllm-project/vllm#10138: [Bug]: Outlines w/ Mistral - 'MistralTokenizer' object has no attribute 'eos_token'

| 字段 | 值 |
| --- | --- |
| Issue | [#10138](https://github.com/vllm-project/vllm/issues/10138) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization |
| 子分类 | install |
| Operator 关键词 | fp8;gemm |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Outlines w/ Mistral - 'MistralTokenizer' object has no attribute 'eos_token'

### Issue 正文摘录

### Your current environment ### Model Input Dumps ```log INFO: 172.17.0.1:51966 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error ERROR: Exception in ASGI application Traceback (most recent call last): File "/usr/local/lib/python3.12/dist-packages/uvicorn/protocols/http/httptools_impl.py", line 401, in run_asgi result = await app( # type: ignore[func-returns-value] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__ return await self.app(scope, receive, send) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/fastapi/applications.py", line 1054, in __call__ await super().__call__(scope, receive, send) File "/usr/local/lib/python3.12/dist-packages/starlette/applications.py", line 113, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.12/dist-packages/starlette/middleware/errors.py", line 187, in __call__ raise exc File "/usr/local/lib/python3.12/dist-packages/starlette/middleware/errors.py", line 165, in __call__ await self.app(scope, receive, _send) File "/usr/local/lib/python3.12/dist-packages/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: /python3.12/dist-packages/vllm/engine/async_llm_engine.py", line 528, in build_guided_decoding_logits_processor_async processor = await get_guided_decoding_logits_processor( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ F...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization fp8;gemm crash dtype;env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ct has no attribute 'eos_token' bug ### Your current environment ### Model Input Dumps ```log INFO: 172.17.0.1:51966 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error ERROR: Exception in ASGI application...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/outlines/fsm/guide.py", line 272, in __init__ self.terminal_regexps["$END"] = tokenizer.eos_token ^^^^^^^^^^^^^^^^^^^ AttributeError: 'MistralTokenizer' objec...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ceive, sender) File "/usr/local/lib/python3.12/dist-packages/starlette/routing.py", line 715, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.12/dist-packages/starlette/routing...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
