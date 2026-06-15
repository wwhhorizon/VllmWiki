# vllm-project/vllm#40920: [Bug]: RuntimeError: flashinfer_fp8_blockscale_gemm fails on H100 NVL MIG 3g.47gb with Qwen3.6-35B-A3B-FP8

| 字段 | 值 |
| --- | --- |
| Issue | [#40920](https://github.com/vllm-project/vllm/issues/40920) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;model_support;quantization;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | cache;cuda;fp8;operator;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: flashinfer_fp8_blockscale_gemm fails on H100 NVL MIG 3g.47gb with Qwen3.6-35B-A3B-FP8

### Issue 正文摘录

### Your current environment Environment: - vLLM version: v0.19.1 - GPU: NVIDIA H100 NVL, MIG slice 3g.47gb (47 GB) - Model: Qwen/Qwen3.6-35B-A3B-FP8 - quantization: fp8, kv-cache-dtype: fp8 Error: RuntimeError: NVML_SUCCESS == r INTERNAL ASSERT FAILED at "/pytorch/c10/cuda/CUDACachingAllocator.cpp":1154 Stacktrace: torch.ops.vllm.flashinfer_fp8_blockscale_gemm.default(...) → run_deepgemm → torch.empty → CUDA allocator assert Reproducible: Yes, consistently on MIG slice. enforce-eager does not help. ### 🐛 Describe the bug vLLM fails to start with Qwen3.6-35B-A3B-FP8 on H100 NVL MIG slice (3g.47gb, 47 GB) with RuntimeError in flashinfer_fp8_blockscale_gemm during profile_run(). Startup command: python3 -m vllm.entrypoints.openai.api_server \ --model /models/qwen36-35b-a3b-fp8 \ --quantization fp8 \ --kv-cache-dtype fp8 \ --max-model-len 65536 \ --gpu-memory-utilization 0.90 \ --enforce-eager Error: RuntimeError: NVML_SUCCESS == r INTERNAL ASSERT FAILED at "/pytorch/c10/cuda/CUDACachingAllocator.cpp":1154 Full traceback ends at: torch.ops.vllm.flashinfer_fp8_blockscale_gemm.default(buf15, arg12_1, arg13_1, 128, True) → _flashinfer_fp8_blockscale_gemm_impl → torch.cond → run_deepgemm...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: wen3.6-35B-A3B-FP8 bug ### Your current environment Environment: - vLLM version: v0.19.1 - GPU: NVIDIA H100 NVL, MIG slice 3g.47gb (47 GB) - Model: Qwen/Qwen3.6-35B-A3B-FP8 - quantization: fp8, kv-cache-dtype: fp8 Error...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: RuntimeError: flashinfer_fp8_blockscale_gemm fails on H100 NVL MIG 3g.47gb with Qwen3.6-35B-A3B-FP8 bug ### Your current environment Environment: - vLLM version: v0.19.1 - GPU: NVIDIA H100 NVL, MIG slice 3g.47gb...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: RuntimeError: flashinfer_fp8_blockscale_gemm fails on H100 NVL MIG 3g.47gb with Qwen3.6-35B-A3B-FP8 bug ### Your current environment Environment: - vLLM version: v0.19.1 - GPU: NVIDIA H100 NVL, MIG slice 3g.47gb...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: 47gb, 47 GB) with RuntimeError in flashinfer_fp8_blockscale_gemm during profile_run(). Startup command: python3 -m vllm.entrypoints.openai.api_server \ --model /models/qwen36-35b-a3b-fp8 \ --quantization fp8 \ --kv-cach...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: e 3g.47gb (47 GB) - Model: Qwen/Qwen3.6-35B-A3B-FP8 - quantization: fp8, kv-cache-dtype: fp8 Error: RuntimeError: NVML_SUCCESS == r INTERNAL ASSERT FAILED at "/pytorch/c10/cuda/CUDACachingAllocator.cpp":1154 Stacktrace:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
