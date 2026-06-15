# vllm-project/vllm#19713: [Bug]: Audio transcription cannot load `preprocessor_config.json` when using runai streamer

| 字段 | 值 |
| --- | --- |
| Issue | [#19713](https://github.com/vllm-project/vllm/issues/19713) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Audio transcription cannot load `preprocessor_config.json` when using runai streamer

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm server is unable to find the `preprocessor_config.json` after loading the transcription model using RunAI... The server loads up successfully but fails on any request. I'm assuming the fix is to load this file at startup time since it's looking at tmp files. INFO: 10.244.6.250:34490 - "POST /v1/audio/transcriptions HTTP/1.1" 500 Internal Server Error ERROR: Exception in ASGI application Traceback (most recent call last): File "/usr/local/lib/python3.12/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi result = await app( # type: ignore[func-returns-value] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__ return await self.app(scope, receive, send) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/site-packages/fastapi/applications.py", line 1054, in __call__ await super().__call__(scope, receive, send) File "/usr/local/lib/python3.12/site-packages/starlette/applications.py", line 112, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.12/...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Audio transcription cannot load `preprocessor_config.json` when using runai streamer bug;stale ### Your current environment ### 🐛 Describe the bug vllm server is unable to find the `preprocessor_config.json` afte...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampli...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ion cannot load `preprocessor_config.json` when using runai streamer bug;stale ### Your current environment ### 🐛 Describe the bug vllm server is unable to find the `preprocessor_config.json` after loading the transcrip...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ceive, sender) File "/usr/local/lib/python3.12/site-packages/starlette/routing.py", line 715, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.12/site-packages/starlette/routing...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ile ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
