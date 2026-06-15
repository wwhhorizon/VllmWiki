# vllm-project/vllm#19477: [Bug]: Internal Server Error when processing short video

| 字段 | 值 |
| --- | --- |
| Issue | [#19477](https://github.com/vllm-project/vllm/issues/19477) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Internal Server Error when processing short video

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug - #17775 had mentioned this bug before and #17791 seems to solve it. - However, I still got the error when inferencing with short videos (num_frames=26, 32). **Server code** ```bash vllm serve /pretrained/Qwen/Qwen2.5-VL-72B-Instruct --host 0.0.0.0 --port 8000 --served-model-name Qwen2.5-VL-72B-Instruct --tensor-parallel-size 4 --max-num-seqs 1 --trust-remote-code --max_num_batched_tokens 32678 --max-model-len 32768 --gpu-memory-utilization 0.95 ``` **Server log** ``` [2025-06-11 15:02:55] INFO: 10.1.4.196:60344 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error [2025-06-11 15:02:55] ERROR: Exception in ASGI application [2025-06-11 15:02:55] Traceback (most recent call last): [2025-06-11 15:02:55] File "/usr/local/lib/python3.12/dist-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi [2025-06-11 15:02:55] result = await app( # type: ignore[func-returns-value] [2025-06-11 15:02:55] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [2025-06-11 15:02:55] File "/usr/local/lib/python3.12/dist-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__ [2025-06-11 15:02:55] return await self.ap...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: s (num_frames=26, 32). **Server code** ```bash vllm serve /pretrained/Qwen/Qwen2.5-VL-72B-Instruct --host 0.0.0.0 --port 8000 --served-model-name Qwen2.5-VL-72B-Instruct --tensor-parallel-size 4 --max-num-seqs 1 --trust...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: d #17791 seems to solve it. - However, I still got the error when inferencing with short videos (num_frames=26, 32). **Server code** ```bash vllm serve /pretrained/Qwen/Qwen2.5-VL-72B-Instruct --host 0.0.0.0 --port 8000...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 6-11 15:02:55] File "/usr/local/lib/python3.12/dist-packages/starlette/routing.py", line 714, in __call__ [2025-06-11 15:02:55] await self.middleware_stack(scope, receive, send) [2025-06-11 15:02:55] File "/usr/local/li...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: in app [2025-06-11 15:02:55] await wrap_app_handling_exceptions(app, request)(scope, receive, send) [2025-06-11 15:02:55] File "/usr/local/lib/python3.12/dist-packages/starlette/_exception_handler.py", line 53, in wrapp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
