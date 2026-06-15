# vllm-project/vllm#13031: [Bug]: Discrepancy in reported throughput metrics (vllm:avg_generation_throughput_toks_per_s) vs. measured performance

| 字段 | 值 |
| --- | --- |
| Issue | [#13031](https://github.com/vllm-project/vllm/issues/13031) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Discrepancy in reported throughput metrics (vllm:avg_generation_throughput_toks_per_s) vs. measured performance

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I’m seeing a large discrepancy between the throughput metrics reported by vLLM’s /metrics endpoint (specifically vllm:avg_prompt_throughput_toks_per_s and vllm:avg_generation_throughput_toks_per_s) and the actual average tokens/s I calculate at the request level. Here’s a snippet of logs from the /metrics endpoint: ``` vllm:avg_prompt_throughput_toks_per_s{model_name="meta-llama/Llama-3.1-8B-Instruct"} 214.0542980674801 vllm:avg_generation_throughput_toks_per_s{model_name="meta-llama/Llama-3.1-8B-Instruct"} 1432.7474079409526 ``` Meanwhile, by measuring each request’s round-trip time and counting the returned tokens (completion_tokens in the usage field), I see numbers significantly lower (often ~20x lower). For example, vLLM reported ~1432 tokens/s generation throughput, whereas the request-level measurement was closer to ~55 tokens/s. Below is a relevant snippet from one of my benchmark logs: ``` H100X2,meta-llama/Llama-3.1-8B-Instruct,26.90,1182.84,28.80,0.00,0.00,6.46,0.00,29.5691,251,444.79,41.20 ``` And a line of logging from vLLM: ``` INFO 02-10 08:16:47 metrics.py:396] Avg prompt throughput: 214.1 tokens/s, Avg generation...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: (vllm:avg_generation_throughput_toks_per_s) vs. measured performance bug;stale ### Your current environment ### 🐛 Describe the bug I’m seeing a large discrepancy between the throughput metrics reported by vLLM’s /metric...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: Discrepancy in reported throughput metrics (vllm:avg_generation_throughput_toks_per_s) vs. measured performance bug;stale ### Your current environment ### 🐛 Describe the bug I’m seeing a large discrepancy between...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: okens/s. Below is a relevant snippet from one of my benchmark logs: ``` H100X2,meta-llama/Llama-3.1-8B-Instruct,26.90,1182.84,28.80,0.00,0.00,6.46,0.00,29.5691,251,444.79,41.20 ``` And a line of logging from vLLM: ``` I...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: 1432.9 tokens/s, Running: 30 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 1.9%, CPU KV cache usage: 0.0%. ``` Error messages / logs No explicit Python traceback. The main issue is the mismatch between: vL...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: s from the /metrics endpoint: ``` vllm:avg_prompt_throughput_toks_per_s{model_name="meta-llama/Llama-3.1-8B-Instruct"} 214.0542980674801 vllm:avg_generation_throughput_toks_per_s{model_name="meta-llama/Llama-3.1-8B-Inst...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
