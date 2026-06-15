# vllm-project/vllm#3048: how to shat out the log which is unnecessary print per 10s

| 字段 | 值 |
| --- | --- |
| Issue | [#3048](https://github.com/vllm-project/vllm/issues/3048) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> how to shat out the log which is unnecessary print per 10s

### Issue 正文摘录

hi when i use openai.api_server.py to run server，print a lot of unnecessary log print per 10s，how to shat out the log。 run: CUDA_VISIBLE_DEVICES=3 python -m vllm.entrypoints.openai.api_server --model /Qwen-14B-Chat --host 0.0.0.0 --port 8884 --served-model-name qwen-14b log: INFO 02-27 14:34:54 metrics.py:161] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0% INFO 02-27 14:35:04 metrics.py:161] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0% INFO 02-27 14:35:14 metrics.py:161] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0% INFO 02-27 14:35:24 metrics.py:161] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0% INFO 02-27 14:35:34 metrics.py:161] Avg prompt throughput:...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: : CUDA_VISIBLE_DEVICES=3 python -m vllm.entrypoints.openai.api_server --model /Qwen-14B-Chat --host 0.0.0.0 --port 8884 --served-model-name qwen-14b log: INFO 02-27 14:34:54 metrics.py:161] Avg prompt throughput: 0.0 to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lot of unnecessary log print per 10s，how to shat out the log。 run: CUDA_VISIBLE_DEVICES=3 python -m vllm.entrypoints.openai.api_server --model /Qwen-14B-Chat --host 0.0.0.0 --port 8884 --served-model-name qwen-14b log:...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ut: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0% INFO 02-27 14:35:04 metrics.py:161] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: odel-name qwen-14b log: INFO 02-27 14:34:54 metrics.py:161] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
