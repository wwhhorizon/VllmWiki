# vllm-project/vllm#10566: [Doc]: Docker+vllm+fastchat deploys multimodal large model Qwen2-vl-7b-instruct(docker+vllm+fastchat部署多模态大模型Qwen2-vl-7b-instruct)

| 字段 | 值 |
| --- | --- |
| Issue | [#10566](https://github.com/vllm-project/vllm/issues/10566) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Docker+vllm+fastchat deploys multimodal large model Qwen2-vl-7b-instruct(docker+vllm+fastchat部署多模态大模型Qwen2-vl-7b-instruct)

### Issue 正文摘录

### 📚 The doc issue When testing using the following method, an error is reported, and the terminal log results are shown as follows: curl -X POST http:(base) root@lxing:~# curl -X POST http://127.0.0.1:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "Qwen2-VL-7B-Instruct", "messages": [{"role": "user", "content": "你好！"}], "temperature": 1.0, "max_tokens": 100 }' {"object":"error","message":"Internal Server Error","code":50001} 2024-11-22 02:50:27 | INFO | stdout | INFO: 127.0.0.1:55822 - "POST /model_details HTTP/1.1" 200 OK 2024-11-22 02:50:27 | INFO | stdout | INFO: 127.0.0.1:55838 - "POST /count_token HTTP/1.1" 200 OK 2024-11-22 02:50:27 | INFO | stdout | INFO: 127.0.0.1:55844 - "POST /worker_generate HTTP/1.1" 500 Internal Server Error 2024-11-22 02:50:27 | ERROR | stderr | ERROR: Exception in ASGI application 2024-11-22 02:50:27 | ERROR | stderr | Traceback (most recent call last): 2024-11-22 02:50:27 | ERROR | stderr | File "/app/miniconda3/envs/vllm/lib/python3.12/site-packages/uvicorn/protocols/http/httptools_impl.py", line 401, in run_asgi 2024-11-22 02:50:27 | ERROR | stderr | result = await app( # type: ignore[func-returns-value] 2024-11...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Doc]: Docker+vllm+fastchat deploys multimodal large model Qwen2-vl-7b-instruct(docker+vllm+fastchat部署多模态大模型Qwen2-vl-7b-instruct) documentation;stale ### 📚 The doc issue When testing using the following method, an error...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: instruct(docker+vllm+fastchat部署多模态大模型Qwen2-vl-7b-instruct) documentation;stale ### 📚 The doc issue When testing using the following method, an error is reported, and the terminal log results are shown as follows: curl -...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: File "/app/miniconda3/envs/vllm/lib/python3.12/site-packages/starlette/routing.py", line 715, in __call__ 2024-11-22 02:50:27 | ERROR | stderr | await self.middleware_stack(scope, receive, send) 2024-11-22 02:50:27 | ER...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Doc]: Docker+vllm+fastchat deploys multimodal large model Qwen2-vl-7b-instruct(docker+vllm+fastchat部署多模态大模型Qwen2-vl-7b-instruct) documentation;stale ### 📚 The doc issue When testing using the following method, an error...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 27 | ERROR | stderr | TypeError: Unexpected keyword argument 'use_beam_search' ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
