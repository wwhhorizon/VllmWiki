# vllm-project/vllm#13951: [Bug]: AttributeError: 'TokenizeChatRequest' object has no attribute 'mm_processor_kwargs'

| 字段 | 值 |
| --- | --- |
| Issue | [#13951](https://github.com/vllm-project/vllm/issues/13951) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'TokenizeChatRequest' object has no attribute 'mm_processor_kwargs'

### Issue 正文摘录

### Issue with OpenAI Tokenization Endpoint, v0.7.3 Hello, I am encountering an error when using OpenAI's tokenization endpoint. - It works correctly when the input is a string. - However, when I provide a message, it returns an error. Could you help me resolve this issue? Thanks! `vllm serve llm --tensor-parallel-size 2 --max-num-seqs 16 --gpu-memory-utilization 0.99` **cURL :** `curl -X POST \ 'http://localhost:8000/tokenize' \ --header 'Accept: */*' \ --header 'Content-Type: application/json' \ --data-raw '{ "model": "llm", "messages": [ { "role": "user", "content": "beşi beş kuruştan beş yumurta kaç kuruş eder? detaylı açıkla." } ] } '` ### 🐛 Describe the bug `ERROR: Exception in ASGI application Traceback (most recent call last): File "/home/103801/venv_vectoryllm_deneme/lib64/python3.9/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi result = await app( # type: ignore[func-returns-value] File "/home/103801/venv_vectoryllm_deneme/lib64/python3.9/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__ return await self.app(scope, receive, send) File "/home/103801/venv_vectoryllm_deneme/lib64/python3.9/site-packages/fastapi/applica...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: AttributeError: 'TokenizeChatRequest' object has no attribute 'mm_processor_kwargs' bug;stale ### Issue with OpenAI Tokenization Endpoint, v0.7.3 Hello, I am encountering an error when using OpenAI's tokenization...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: me/103801/venv_vectoryllm_deneme/lib64/python3.9/site-packages/starlette/routing.py", line 756, in __call__ await self.middleware_stack(scope, receive, send) File "/home/103801/venv_vectoryllm_deneme/lib64/python3.9/sit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s'` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: t: */*' \ --header 'Content-Type: application/json' \ --data-raw '{ "model": "llm", "messages": [ { "role": "user", "content": "beşi beş kuruştan beş yumurta kaç kuruş eder? detaylı açıkla." } ] } '` ### 🐛 Describe the...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: me/103801/venv_vectoryllm_deneme/lib64/python3.9/site-packages/starlette/routing.py", line 756, in __call__ await self.middleware_stack(scope, receive, send) File "/home/103801/venv_vectoryllm_deneme/lib64/python3.9/sit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
