# vllm-project/vllm#42058: [Performance]: Quantized KV Cache Throughput/TTFT/TPOT slower?

| 字段 | 值 |
| --- | --- |
| Issue | [#42058](https://github.com/vllm-project/vllm/issues/42058) |
| 状态 | open |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Quantized KV Cache Throughput/TTFT/TPOT slower?

### Issue 正文摘录

### Proposal to improve performance hardware: 4090 vllm: 0.20.0 prefill: 10240 tokens decode: 1024 tokens guidellm mode: input tokens/s and output tokens/s is throughput; TTFT and TPOT is synchronous - base server: python3 -m vllm.entrypoints.openai.api_server --tensor-parallel-size=4 --model=/home/jessiew/models/Qwen3-32B --no-enable-prefix-caching - no calibration server: python3 -m vllm.entrypoints.openai.api_server --tensor-parallel-size=4 --no-calculate-kv-scales --kv-cache-dtype=fp8 --model=/home/jessiew/models/Qwen3-32B --no-enable-prefix-caching - random token calibration server: python3 -m vllm.entrypoints.openai.api_server --tensor-parallel-size=4 --kv-cache-dtype=fp8 --model=/home/jessiew/models/Qwen3-32B --no-enable-prefix-caching --calculate-kv-scales guidellm results: | Server | KV cache size | input tokens/s | output tokens/s | TTFT ms | TPOT ms | |--------|--------|--------|--------|--------|--------| | base | 72,288 | 23092.3 | 118.7 | 3295.1 | 22.6 | | no calibration | 115,328 | 20311.7 | 143.9 | 3311.8 | 21.6 | | random token calibration | 109,664 | 20161.6 | 132.3 | 3290.9 | 21.7 | Is it expected that a quantized KV cache would show degradation in Throughput, T...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Performance]: Quantized KV Cache Throughput/TTFT/TPOT slower? performance ### Proposal to improve performance hardware: 4090 vllm: 0.20.0 prefill: 10240 tokens decode: 1024 tokens guidellm mode: input tokens/s and outp...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Performance]: Quantized KV Cache Throughput/TTFT/TPOT slower? performance ### Proposal to improve performance hardware: 4090 vllm: 0.20.0 prefill: 10240 tokens decode: 1024 tokens guidellm mode: input tokens/s and outp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: python3 -m vllm.entrypoints.openai.api_server --tensor-parallel-size=4 --model=/home/jessiew/models/Qwen3-32B --no-enable-prefix-caching - no calibration server: python3 -m vllm.entrypoints.openai.api_server --tensor-pa...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Performance]: Quantized KV Cache Throughput/TTFT/TPOT slower? performance ### Proposal to improve performance hardware: 4090 vllm: 0.20.0 prefill: 10240 tokens decode: 1024 tokens guidellm mode: input tokens/s and outp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ormance ### Proposal to improve performance hardware: 4090 vllm: 0.20.0 prefill: 10240 tokens decode: 1024 tokens guidellm mode: input tokens/s and output tokens/s is throughput; TTFT and TPOT is synchronous - base serv...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
