# vllm-project/vllm#36095: [Feature]: Add fused MoE kernel tuning configs for NVIDIA GeForce RTX 5090 (int4_w4a16)

| 字段 | 值 |
| --- | --- |
| Issue | [#36095](https://github.com/vllm-project/vllm/issues/36095) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization |
| 子分类 | throughput |
| Operator 关键词 | cache;fp8;kernel;moe;quantization |
| 症状 | slowdown |
| 根因提示 | dtype |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Add fused MoE kernel tuning configs for NVIDIA GeForce RTX 5090 (int4_w4a16)

### Issue 正文摘录

### Motivation Running `Qwen/Qwen3.5-35B-A3B-GPTQ-Int4` on 2x RTX 5090 (SM 12.0, Blackwell) with `--quantization moe_wna16` produces this warning: ``` WARNING [fused_moe.py:1093] Using default MoE config. Performance might be sub-optimal! Config file not found at .../fused_moe/configs/E=128,N=512,device_name=NVIDIA_GeForce_RTX_5090,dtype=int4_w4a16.json ``` The result is ~47 tok/s single-request throughput and ~1556 tok/s peak aggregate — roughly **half** the speed of the same model quantized as AWQ 4-bit using `compressed-tensors` (Marlin MoE kernels), which achieves ~87 tok/s single-request and ~2032 tok/s peak on the same hardware. ### Hardware - 2x NVIDIA GeForce RTX 5090 (32GB each, SM 12.0 / Blackwell) - TP=2, EP=2, FP8 KV cache - vLLM v0.16.1rc1 nightly ### Current state The `fused_moe/configs/` directory contains **no RTX 5090 configs** for any dtype. The only Blackwell configs are for RTX PRO 6000 (fp8_w8a8 only). The only int4_w4a16 config is for AMD Radeon 8060S. ### Request Add tuned fused MoE kernel configs for `NVIDIA_GeForce_RTX_5090` with at minimum: - `E=128,N=512,dtype=int4_w4a16` (Qwen3.5 35B MoE GPTQ-Int4) - `E=256,N=128,dtype=int4_w4a16` (other MoE architectur...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ature]: Add fused MoE kernel tuning configs for NVIDIA GeForce RTX 5090 (int4_w4a16) ### Motivation Running `Qwen/Qwen3.5-35B-A3B-GPTQ-Int4` on 2x RTX 5090 (SM 12.0, Blackwell) with `--quantization moe_wna16` produces t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Feature]: Add fused MoE kernel tuning configs for NVIDIA GeForce RTX 5090 (int4_w4a16) ### Motivation Running `Qwen/Qwen3.5-35B-A3B-GPTQ-Int4` on 2x RTX 5090 (SM 12.0, Blackwell) with `--quantization moe_wna16` produce...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Add fused MoE kernel tuning configs for NVIDIA GeForce RTX 5090 (int4_w4a16) ### Motivation Running `Qwen/Qwen3.5-35B-A3B-GPTQ-Int4` on 2x RTX 5090 (SM 12.0, Blackwell) with `--quantization moe_wna16` produce...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: X_5090,dtype=int4_w4a16.json ``` The result is ~47 tok/s single-request throughput and ~1556 tok/s peak aggregate — roughly **half** the speed of the same model quantized as AWQ 4-bit using `compressed-tensors` (Marlin...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: IDIA GeForce RTX 5090 (32GB each, SM 12.0 / Blackwell) - TP=2, EP=2, FP8 KV cache - vLLM v0.16.1rc1 nightly ### Current state The `fused_moe/configs/` directory contains **no RTX 5090 configs** for any dtype. The only B...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
