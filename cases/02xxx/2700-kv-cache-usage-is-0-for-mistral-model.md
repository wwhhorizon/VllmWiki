# vllm-project/vllm#2700: KV Cache usage is 0% for mistral model 

| 字段 | 值 |
| --- | --- |
| Issue | [#2700](https://github.com/vllm-project/vllm/issues/2700) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> KV Cache usage is 0% for mistral model 

### Issue 正文摘录

### Issue I loaded the merged finetuned mistral model and trying to run the Triton Server with the vLLM backend following: https://github.com/triton-inference-server/vllm_backend. When I start the server and run the inference however I see these log statements showing that no GPU or CPU KV cache is being utilized? How is that possible? ``` INFO 01-31 22:08:42 llm_engine.py:649] Avg prompt throughput: 85.9 tokens/s, Avg generation throughput: 45.5 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0% INFO 01-31 22:08:47 llm_engine.py:649] Avg prompt throughput: 82.3 tokens/s, Avg generation throughput: 46.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0% INFO 01-31 22:08:52 llm_engine.py:649] Avg prompt throughput: 84.3 tokens/s, Avg generation throughput: 45.7 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0% INFO 01-31 22:08:57 llm_engine.py:649] Avg prompt throughput: 82.3 tokens/s, Avg generation throughput: 45.7 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: KV Cache usage is 0% for mistral model ### Issue I loaded the merged finetuned mistral model and trying to run the Triton Server with the vLLM backend following: https://github.com/triton-inference-server/vllm_backend....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: Issue I loaded the merged finetuned mistral model and trying to run the Triton Server with the vLLM backend following: https://github.com/triton-inference-server/vllm_backend. When I start the server and run the inferen...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: "disable_log_requests": "true", "gpu_memory_utilization": 0.95, "dtype": "float16", "max_model_len": 128, "tensor_parallel_size": 8, "max_num_seqs": 32, "swap_space": 4, "tokenizer": "mistralai/Mistral-7B-v0.1" } ``` My...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: is that possible? ``` INFO 01-31 22:08:42 llm_engine.py:649] Avg prompt throughput: 85.9 tokens/s, Avg generation throughput: 45.5 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, C...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: KV Cache usage is 0% for mistral model ### Issue I loaded the merged finetuned mistral model and trying to run the Triton Server with the vLLM backend following: https://github.com/triton-inference-server/vllm_backend.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
