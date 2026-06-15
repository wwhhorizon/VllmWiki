# vllm-project/vllm#9874: [Bug]: Function calling with Qwen & Streaming ('NoneType' object has no attribute 'get')

| 字段 | 值 |
| --- | --- |
| Issue | [#9874](https://github.com/vllm-project/vllm/issues/9874) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Function calling with Qwen & Streaming ('NoneType' object has no attribute 'get')

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug # vLLM Version `v0.6.3.post1` # Model `Qwen2.5-7B-Instruct` # Docker command for vLLM `command: --host 0.0.0.0 --model /hf/Qwen-Qwen2.5-7B-Instruct --max-model-len 32768 --gpu_memory_utilization 0.9 --enable-auto-tool-choice --tool-call-parser hermes` # Parsing from my own fastapi ``` async def stream_response(payload: dict, log: RequestLogger) -> AsyncGenerator[str, None]: """Handle streaming response from vLLM.""" async with httpx.AsyncClient() as client: try: async with client.stream( 'POST', VLLM_API_BASE, json=payload, headers={"Content-Type": "application/json"}, timeout=30.0 ) as response: if response.status_code != 200: error_msg = f"vLLM API error: {response.status_code}" log(error_msg, level='error') yield f"data: {json.dumps({'error': error_msg})}\n\n" return async for line in response.aiter_lines(): if not line or not line.startswith('data: '): continue line = line.removeprefix('data: ') if line.strip() == '[DONE]': log("Stream completed") yield 'data: [DONE]\n\n' break try: parsed = json.loads(line) log("Streaming chunk", parsed) # Handle tool calls in streaming response if 'choice...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Function calling with Qwen & Streaming ('NoneType' object has no attribute 'get') bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug # vLLM Version `v0.6.3.post1` #...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ing with Qwen & Streaming ('NoneType' object has no attribute 'get') bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug # vLLM Version `v0.6.3.post1` # Model `Qwen2.5-7B-In...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ### Model Input Dumps _No response_ ### 🐛 Describe the bug # vLLM Version `v0.6.3.post1` # Model `Qwen2.5-7B-Instruct` # Docker command for vLLM `command: --host 0.0.0.0 --model /hf/Qwen-Qwen2.5-7B-Instruct --max-model-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: " return async for line in response.aiter_lines(): if not line or not line.startswith('data: '): continue line = line.removeprefix('data: ') if lin
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: el. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
