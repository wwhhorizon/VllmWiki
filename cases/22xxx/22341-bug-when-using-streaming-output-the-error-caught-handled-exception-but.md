# vllm-project/vllm#22341: [Bug]: When using streaming output, the error 'Caught handled exception, but response already started' occurs.

| 字段 | 值 |
| --- | --- |
| Issue | [#22341](https://github.com/vllm-project/vllm/issues/22341) |
| 状态 | closed |
| 标签 | bug;stale;gpt-oss |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When using streaming output, the error 'Caught handled exception, but response already started' occurs.

### Issue 正文摘录

### Your current environment vllm 0.10.1+gptoss ### 🐛 Describe the bug def get_resp_stream(self, message_list, top_p=-1, temperature=-1): temperature = self.temperature request_data = { "model": self.model, "input": message_list, "reasoning": {"effort": "high"}, "max_output_tokens": self.max_tokens, "temperature": temperature, "stream": True, } final = '' reasoning = '' for i in range(50): try: response = requests.post( "http://localhost:8080/v1/responses", json=request_data, headers={"Content-Type": "application/json"}, timeout=120, stream=True, ) for chunk in response.iter_lines(decode_unicode=False): chunk = chunk.decode("utf-8") if chunk and chunk.startswith("data:"): if chunk == "data: [DONE]": break data = json.loads(chunk[5:].strip("\n")) if data["type"] == "response.reasoning_text.delta": reasoning += data["delta"] elif data["type"] == "response.reasoning_text.done": if reasoning != data["text"]: reasoning = data["text"] elif data["type"] == "response.output_text.delta": final += data["delta"] elif data["type"] == "response.output_text.done": if final != data["text"]: final = data["text"] break except Exception as e: print(f"Exception: {e}\nTraceback: {traceback.format_exc...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ror 'Caught handled exception, but response already started' occurs. bug;stale;gpt-oss ### Your current environment vllm 0.10.1+gptoss ### 🐛 Describe the bug def get_resp_stream(self, message_list, top_p=-1, temperature...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: aught handled exception, but response already started' occurs. bug;stale;gpt-oss ### Your current environment vllm 0.10.1+gptoss ### 🐛 Describe the bug def get_resp_stream(self, message_list, top_p=-1, temperature=-1):...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rver pid=388) | File "/usr/local/lib/python3.12/dist-packages/anyio/_backends/_asyncio.py", line 772, in __aexit__ (APIServer pid=388) | raise BaseExceptionGroup( (APIServer pid=388) | ExceptionGroup: unhandled errors i...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ration throughput: 569.9 tokens/s, Running: 3 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.4%, Prefix cache hit rate: 77.7% (APIServer pid=388) ERROR: Exception in ASGI application (APIServer pid=388) + Exception Group...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ver pid=388) INFO 08-06 01:27:23 [loggers.py:123] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 569.9 tokens/s, Running: 3 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.4%, Prefix cache hit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
