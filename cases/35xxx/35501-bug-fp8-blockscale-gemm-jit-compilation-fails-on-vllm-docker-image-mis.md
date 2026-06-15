# vllm-project/vllm#35501: [Bug]: fp8_blockscale_gemm JIT compilation fails on vLLM Docker image — missing cublasLt.h, nvrtc.h, and -lnvrtc

| 字段 | 值 |
| --- | --- |
| Issue | [#35501](https://github.com/vllm-project/vllm/issues/35501) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: fp8_blockscale_gemm JIT compilation fails on vLLM Docker image — missing cublasLt.h, nvrtc.h, and -lnvrtc

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Description FlashInfer's fp8_blockscale_gemm JIT compilation fails when running inside the official vLLM 0.16.0 Docker image with VLLM_BLOCKSCALE_FP8_GEMM_FLASHINFER=1. The build fails in three successive stages due to missing headers and libraries: 1. fatal error: cublasLt.h: No such file or directory 2. fatal error: nvrtc.h: No such file or directory 3. /usr/bin/ld: cannot find -lnvrtc: No such file or directory ### Root Cause The vLLM Docker image installs CUDA libraries via pip packages (nvidia-cublas-cu12, nvidia-cuda-nvrtc-cu12, etc.) rather than the full CUDA toolkit. These packages place headers and libraries in non-standard paths: - Headers: /usr/local/lib/python3.12/dist-packages/nvidia/cublas/include/, .../cuda_nvrtc/include/, etc. - Libraries: /usr/local/lib/python3.12/dist-packages/nvidia/cuda_nvrtc/lib/, etc. FlashInfer's JIT build for fp8_blockscale_gemm (in cached_ops/fp8_blockscale_gemm_90/) hardcodes -L/usr/local/cuda/lib64 and relies on standard include paths (/usr/local/cuda/include), which don't contain these files in the pip-based installation. Other FlashInfer JIT targets (e.g., attention kernels) appea...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Bug]: fp8_blockscale_gemm JIT compilation fails on vLLM Docker image — missing cublasLt.h, nvrtc.h, and -lnvrtc bug ### Your current environment ### 🐛 Describe the bug ### Description FlashInfer's fp8_blockscale_gemm J...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: fp8_blockscale_gemm JIT compilation fails on vLLM Docker image — missing cublasLt.h, nvrtc.h, and -lnvrtc bug ### Your current environment ### 🐛 Describe the bug ### Description FlashInfer's fp8_blockscale_gemm J...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ## Your current environment ### 🐛 Describe the bug ### Description FlashInfer's fp8_blockscale_gemm JIT compilation fails when running inside the official vLLM 0.16.0 Docker image with VLLM_BLOCKSCALE_FP8_GEMM_FLASHINFE...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: o such file or directory ### Root Cause The vLLM Docker image installs CUDA libraries via pip packages (nvidia-cublas-cu12, nvidia-cuda-nvrtc-cu12, etc.) rather than the full CUDA toolkit. These packages place headers a...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: Container: Official vLLM 0.16.0 Docker image (Kubernetes) ### Steps to Reproduce * Inside the vllm 0.16.0 Docker image VLLM_BLOCKSCALE_FP8_GEMM_FLASHINFER=1 vllm serve \ --kv-cache-dtype fp8 \ --tensor-parallel-size 4 T...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
