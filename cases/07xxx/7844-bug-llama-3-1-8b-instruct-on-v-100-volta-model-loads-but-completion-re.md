# vllm-project/vllm#7844: [Bug]: Llama 3.1 8b-instruct on V-100 (Volta): model loads, but completion request fails

| 字段 | 值 |
| --- | --- |
| Issue | [#7844](https://github.com/vllm-project/vllm/issues/7844) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Llama 3.1 8b-instruct on V-100 (Volta): model loads, but completion request fails

### Issue 正文摘录

### 🐛 Describe the bug I'm trying to tun Llama 3.1-8b-instruct on V-100 (Volta). Model loads fine with the following settings: ``` command: > --host 0.0.0.0 --dtype=half --tensor-parallel-size 8 --enforce-eager --num-scheduler-steps 8 --gpu_memory_utilization 0.95 --enable-chunked-prefill=false --max-model-len=4096 --trust-remote-code --served-model-name Llama-3.1-8b --model /models/meta-llama/Meta-Llama-3.1-8B-Instruct ``` Any chat completion request crashes: ```python ama-8b-1 | llama-8b-1 | During handling of the above exception, another exception occurred: llama-8b-1 | llama-8b-1 | Traceback (most recent call last): llama-8b-1 | File "/usr/local/lib/python3.10/dist-packages/uvicorn/protocols/http/httptools_impl.py", line 401, in run_asgi llama-8b-1 | result = await app( # type: ignore[func-returns-value] llama-8b-1 | File "/usr/local/lib/python3.10/dist-packages/uvicorn/middleware/proxy_headers.py", line 70, in __call__ llama-8b-1 | return await self.app(scope, receive, send) llama-8b-1 | File "/usr/local/lib/python3.10/dist-packages/fastapi/applications.py", line 1054, in __call__ llama-8b-1 | await super().__call__(scope, receive, send) llama-8b-1 | File "/usr/local/lib/pyth...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: /base.py", line 191, in __call__ llama-8b-1 | response = await self.dispatch_func(request, call_next) llama-8b-1 | File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/api_server.py", line 361, in authe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ug]: Llama 3.1 8b-instruct on V-100 (Volta): model loads, but completion request fails bug ### 🐛 Describe the bug I'm trying to tun Llama 3.1-8b-instruct on V-100 (Volta). Model loads fine with the following settings: `...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: s 8 --gpu_memory_utilization 0.95 --enable-chunked-prefill=false --max-model-len=4096 --trust-remote-code --served-model-name Llama-3.1-8b --model /models/meta-llama/Meta-Llama-3.1-8B-Instruct ``` Any chat completion re...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Llama 3.1 8b-instruct on V-100 (Volta): model loads, but completion request fails bug ### 🐛 Describe the bug I'm trying to tun Llama 3.1-8b-instruct on V-100 (Volta). Model loads fine with the following settings:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ils.py:226] llama-8b-1 | INFO 08-25 00:36:27 metrics.py:351] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.1 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
