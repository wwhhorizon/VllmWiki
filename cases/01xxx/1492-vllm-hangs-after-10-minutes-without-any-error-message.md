# vllm-project/vllm#1492: vLLM hangs after 10 minutes without any error message

| 字段 | 值 |
| --- | --- |
| Issue | [#1492](https://github.com/vllm-project/vllm/issues/1492) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vLLM hangs after 10 minutes without any error message

### Issue 正文摘录

Hi vLLM team, I started a vLLM server (OpenAI API) to serve LLaMA-7b and had multiple processes sending requests to it simultaneously to saturate the GPU (I tried both 1xA100 40G and 1xA40 40G). However, after 5-10 minutes, the vLLM server will hang there (no more new requests get handled) forever without error messages. Most recent stats show that "INFO 10-27 20:44:35 llm_engine.py:624] Avg prompt throughput: 642.0 tokens/s, Avg generation throughput: 61.0 tokens/s, Running: 2 reqs, Swapped: 0 reqs, Pending: 20 reqs, GPU KV cache u sage: 98.7%, CPU KV cache usage: 0.0%". After hanging happens, `v1/models` endpoint still works (give correct responses), but chat completion and completion requests will receive `openai.error.APIError: Invalid response object from API: 'Internal Server Error' (HTTP response code was 500).` and there were NO error messages from the vLLM side. Any idea what might cause this? Is it because there are too many requests to be handled? Thanks!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ror message Hi vLLM team, I started a vLLM server (OpenAI API) to serve LLaMA-7b and had multiple processes sending requests to it simultaneously to saturate the GPU (I tried both 1xA100 40G and 1xA40 40G). However, aft...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ending requests to it simultaneously to saturate the GPU (I tried both 1xA100 40G and 1xA40 40G). However, after 5-10 minutes, the vLLM server will hang there (no more new requests get handled) forever without error mes...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: : 61.0 tokens/s, Running: 2 reqs, Swapped: 0 reqs, Pending: 20 reqs, GPU KV cache u sage: 98.7%, CPU KV cache usage: 0.0%". After hanging happens, `v1/models` endpoint still works (give correct responses), but chat comp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: server (OpenAI API) to serve LLaMA-7b and had multiple processes sending requests to it simultaneously to saturate the GPU (I tried both 1xA100 40G and 1xA40 40G). However, after 5-10 minutes, the vLLM server will hang...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ecent stats show that "INFO 10-27 20:44:35 llm_engine.py:624] Avg prompt throughput: 642.0 tokens/s, Avg generation throughput: 61.0 tokens/s, Running: 2 reqs, Swapped: 0 reqs, Pending: 20 reqs, GPU KV cache u sage: 98....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
