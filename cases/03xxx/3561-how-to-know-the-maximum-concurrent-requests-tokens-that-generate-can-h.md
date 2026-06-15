# vllm-project/vllm#3561: How to know the maximum concurrent requests /tokens that generate can handle at the same time?

| 字段 | 值 |
| --- | --- |
| Issue | [#3561](https://github.com/vllm-project/vllm/issues/3561) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to know the maximum concurrent requests /tokens that generate can handle at the same time?

### Issue 正文摘录

### Your current environment I am wondering how to know or configure the number of concurrent requests (number of tokens). I can see from logs these values: `INFO 03-18 12:34:52 llm_engine.py:706] Avg prompt throughput: 209.6 tokens/s, Avg generation throughput: 567.4 tokens/s, Running: 36 reqs, Swapped: 0 reqs, Pending: 78 reqs, GPU KV cache usage: 99.1%, CPU KV cache usage: 0.0% ` 1. i don't know when the request would be in the pending and what is the meaning of running request? 2. does all of them are enter in the model at the same time (same batch)? 3. What the effect of `max_tokens` in `SamplingParams,` if I set it to 1024 but I receive response of 1027 tokens!! In the `EngineArgs`: 4. Is this `--max-model-len` will limit the single request tokens? or only has affect on the pre-reserved GPU memory for the llm? 5. what is eager mode? 6. how dynamic batching is performed? if we send N requests do they will be in a queue based on what? what is the max batch size to be entered to the model? 7. Is this `max_context_len_to_capture` has affect on the total number of tokens can the model handle? 8. Also I didn't understand well what are these args? how they affect the batching or nu...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: 567.4 tokens/s, Running: 36 reqs, Swapped: 0 reqs, Pending: 78 reqs, GPU KV cache usage: 99.1%, CPU KV cache usage: 0.0% ` 1. i don't know when the request would be in the pending and what is the meaning of running requ...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: me time? bug ### Your current environment I am wondering how to know or configure the number of concurrent requests (number of tokens). I can see from logs these values: `INFO 03-18 12:34:52 llm_engine.py:706] Avg promp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: How to know the maximum concurrent requests /tokens that generate can handle at the same time? bug ### Your current environment I am wondering how to know or configure the number of concurrent requests (number of tokens...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ints. Thanks ### 🐛 Describe the bug For both, openllm start with vllm backend or even vllm on ray.
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: m logs these values: `INFO 03-18 12:34:52 llm_engine.py:706] Avg prompt throughput: 209.6 tokens/s, Avg generation throughput: 567.4 tokens/s, Running: 36 reqs, Swapped: 0 reqs, Pending: 78 reqs, GPU KV cache usage: 99....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
