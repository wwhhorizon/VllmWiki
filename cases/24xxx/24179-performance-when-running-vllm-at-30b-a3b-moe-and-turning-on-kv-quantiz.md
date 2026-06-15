# vllm-project/vllm#24179: [Performance]:When running vllm at 30b-a3b MOE and turning on kv quantization, the decoding speed of 40K input drops significantly from 100t to 40t.

| 字段 | 值 |
| --- | --- |
| Issue | [#24179](https://github.com/vllm-project/vllm/issues/24179) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]:When running vllm at 30b-a3b MOE and turning on kv quantization, the decoding speed of 40K input drops significantly from 100t to 40t.

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression CUDA_VISIBLE_DEVICES=0 \ VLLM_USE_V1=0 \ VLLM_ATTENTION_BACKEND=FLASHINFER \ vllm serve \ /root/Qwen3-Coder-30B-A3B-Instruct-Int4-W4A16 \ --served-model vllm \ --dtype=bfloat16 \ --max-num-seqs 64 \ --enable-chunked-prefill \ --max-model-len 250k \ --enable-auto-tool-choice \ --tool-call-parser qwen3_coder \ --trust-remote-code \ --max-num-seqs=100 \ --kv-cache-dtype fp8 \ --calculate-kv-scales \ --gpu-memory-utilization=0.95 \ --port 8099 \ --host 0.0.0.0 \ --block-size 32 (APIServer pid=765923) INFO: 192.168.2.83:9221 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO 09-03 12:57:57 [metrics.py:386] Avg prompt throughput: 5195.0 tokens/s, Avg generation throughput: 8.8 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 18.1%, CPU KV cache usage: 0.0%. INFO 09-03 12:58:03 [metrics.py:386] Avg prompt throughput: 4151.5 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 18.1%, CPU KV cache usage: 0.0%. INFO 09-03 12:58:08 [metrics.py:386] Avg prompt throughput: 388.4 tokens/s, Avg generation throu...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Performance]:When running vllm at 30b-a3b MOE and turning on kv quantization, the decoding speed of 40K input drops significantly from 100t to 40t. performance;stale ### Proposal to improve performance _No response_ ##...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: roposal to improve performance _No response_ ### Report of performance regression CUDA_VISIBLE_DEVICES=0 \ VLLM_USE_V1=0 \ VLLM_ATTENTION_BACKEND=FLASHINFER \ vllm serve \ /root/Qwen3-Coder-30B-A3B-Instruct-Int4-W4A16 \...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ance regression CUDA_VISIBLE_DEVICES=0 \ VLLM_USE_V1=0 \ VLLM_ATTENTION_BACKEND=FLASHINFER \ vllm serve \ /root/Qwen3-Coder-30B-A3B-Instruct-Int4-W4A16 \ --served-model vllm \ --dtype=bfloat16 \ --max-num-seqs 64 \ --en...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: mprove performance _No response_ ### Report of performance regression CUDA_VISIBLE_DEVICES=0 \ VLLM_USE_V1=0 \ VLLM_ATTENTION_BACKEND=FLASHINFER \ vllm serve \ /root/Qwen3-Coder-30B-A3B-Instruct-Int4-W4A16 \ --served-mo...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: -parser qwen3_coder \ --trust-remote-code \ --max-num-seqs=100 \ --kv-cache-dtype fp8 \ --calculate-kv-scales \ --gpu-memory-utilization=0.95 \ --port 8099 \ --host 0.0.0.0 \ --block-size 32 (APIServer pid=765923) INFO:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
