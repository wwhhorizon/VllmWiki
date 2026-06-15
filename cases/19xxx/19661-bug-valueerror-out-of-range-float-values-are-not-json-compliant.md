# vllm-project/vllm#19661: [Bug]: ValueError  out of range float values are not json compliant

| 字段 | 值 |
| --- | --- |
| Issue | [#19661](https://github.com/vllm-project/vllm/issues/19661) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ValueError  out of range float values are not json compliant

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Run the following command using vllm 0.9 version： nohup vllm serve iic/gme-Qwen2-VL-2B-Instruct --task embed --trust-remote-code --dtype auto --gpu-memory-utilization 0.9 --max-model-len 8192 --served-model-name gme-qwen2-vl-2b --chat-template /vllm-workspace/vllm/examples/template_dse_qwen2_vl.jinja --port 8012 & When initiating an image embedding inference request, an error occurs as follows： INFO 06-15 10:06:17 [engine.py:316] Added request embd-8fae471b374f49fba02a237a2e9da04e-0. INFO 06-15 10:06:19 [metrics.py:486] Avg prompt throughput: 143.4 tokens/s, Avg generation throughput: 0.1 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0%. INFO: 127.0.0.1:55978 - "POST /v1/embeddings HTTP/1.1" 500 Internal Server Error ERROR: Exception in ASGI application Traceback (most recent call last): File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asg i result = await app( # type: ignore[func-returns-value] File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvicorn/middleware/proxy_headers.py", line 6...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: n the following command using vllm 0.9 version： nohup vllm serve iic/gme-Qwen2-VL-2B-Instruct --task embed --trust-remote-code --dtype auto --gpu-memory-utilization 0.9 --max-model-len 8192 --served-model-name gme-qwen2...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: ValueError out of range float values are not json compliant bug;stale ### Your current environment ### 🐛 Describe the bug Run the following command using vllm 0.9 version： nohup vllm serve iic/gme-Qwen2-VL-2B-Ins...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: f49fba02a237a2e9da04e-0. INFO 06-15 10:06:19 [metrics.py:486] Avg prompt throughput: 143.4 tokens/s, Avg generation throughput: 0.1 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: File "/usr/local/python3.10.17/lib/python3.10/site-packages/starlette/routing.py", line 714, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/python3.10.17/lib/python3.10/site-packages/star...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ent ### 🐛 Describe the bug Run the following command using vllm 0.9 version： nohup vllm serve iic/gme-Qwen2-VL-2B-Instruct --task embed --trust-remote-code --dtype auto --gpu-memory-utilization 0.9 --max-model-len 8192...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
