# vllm-project/vllm#24916: [Feature]: Make FP8 Attention fast for GPT-OSS w/ FA3 on Hopper

| 字段 | 值 |
| --- | --- |
| Issue | [#24916](https://github.com/vllm-project/vllm/issues/24916) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Make FP8 Attention fast for GPT-OSS w/ FA3 on Hopper

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When using `kv_cache_dtype="fp8` on Hopper, we are using FA3 FP8 backend. This means we are quantizing Keys, Values, and Queries and are using the complete FP8 forward pass of FA3. Whilst this saves KV cache space and leads to TTFT speedups it currently leads to slowdowns in ITL which are quite considerable (see below) The biggest issue are that quantizing the queries and the K, V causes overheads. Furthermore FP8 path of FA3 is very bad for decoding for GPT-OSS (head_dim=64). To adress this we propose 3 optimizations: 1/ [merged] Only quantize the full attention layers and leave the sliding window layers in BF16 --> ~#24912~ https://github.com/vllm-project/vllm/pull/33695 (specific to GPT-OSS architecture) 2/ [merged] Add an environment flag such that for static scales torch.compile can fuse the quantization of the queries into previous operations --> #24914 (applies generally) 3/ [merged] Optimize the tiling configuration for head_dim 64 of FA3 --> https://github.com/vllm-project/flash-attention/pull/91 We run `bench serve` with 25k and 1k inputs to illustrate the overheads during decoding (always running with `"cudagraph_mode": "FULL_AND_...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Feature]: Make FP8 Attention fast for GPT-OSS w/ FA3 on Hopper feature request;stale ### 🚀 The feature, motivation and pitch When using `kv_cache_dtype="fp8` on Hopper, we are using FA3 FP8 backend. This means we are q...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Feature]: Make FP8 Attention fast for GPT-OSS w/ FA3 on Hopper feature request;stale ### 🚀 The feature, motivation and pitch When using `kv_cache_dtype="fp8` on Hopper, we are using FA3 FP8 backend. This means we are q...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Make FP8 Attention fast for GPT-OSS w/ FA3 on Hopper feature request;stale ### 🚀 The feature, motivation and pitch When using `kv_cache_dtype="fp8` on Hopper, we are using FA3 FP8 backend. This means we are q...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: layers quantization, we quantize less than normally. We also checked the accuracy via gpt-oss evals and are within the usual variations. | model | applied optimization | input | output | median ITL [ms] | median ttft [m...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Feature]: Make FP8 Attention fast for GPT-OSS w/ FA3 on Hopper feature request;stale ### 🚀 The feature, motivation and pitch When using `kv_cache_dtype="fp8` on Hopper, we are using FA3 FP8 backend. This means we are q...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
