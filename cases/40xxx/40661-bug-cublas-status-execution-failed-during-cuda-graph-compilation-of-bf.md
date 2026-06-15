# vllm-project/vllm#40661: [Bug]: CUBLAS_STATUS_EXECUTION_FAILED during CUDA graph compilation of BF16 vision encoder on NVIDIA Jetson AGX Thor (vLLM 0.19.0 regression)

| 字段 | 值 |
| --- | --- |
| Issue | [#40661](https://github.com/vllm-project/vllm/issues/40661) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | cold_start |
| Operator 关键词 | cuda;fp8;gemm;moe |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUBLAS_STATUS_EXECUTION_FAILED during CUDA graph compilation of BF16 vision encoder on NVIDIA Jetson AGX Thor (vLLM 0.19.0 regression)

### Issue 正文摘录

## Your current environment **Container image**: `ghcr.io/nvidia-ai-iot/vllm:latest-jetson-thor` (tag `r38.2.arm64-sbsa-cu130-24.04`) **vLLM version**: 0.19.0 **Hardware**: NVIDIA Jetson AGX Thor — Blackwell GPU (SM 90+), 122 GB unified LPDDR5x memory, CUDA 13.0 **OS**: Ubuntu 24.04 (ARM64 SBSA) **Model**: `Qwen/Qwen3.6-35B-A3B-FP8` (`qwen3_5_moe` architecture with vision encoder) **Python**: 3.12.12 ## 🐛 Describe the bug vLLM 0.19.0 (Jetson Thor container) crashes with `CUBLAS_STATUS_EXECUTION_FAILED` during CUDA graph compilation of the vision encoder when loading `Qwen3.6-35B-A3B-FP8`. This is a **regression** — the same model, same hardware, and same launch flags work correctly on the previous image (`ghcr.io/nvidia-ai-iot/vllm:0.16.0-g15d76f74e-r38.2-arm64-sbsa-cu130-24.04`, vLLM 0.16.0rc2). The crash occurs **after** model weights are fully loaded, during the CUDA graph compilation phase (`Compiling a graph for compile range (1, 2048)`). The failing operation is a BF16 GEMM (`cublasGemmEx` with `CUDA_R_16BF`) called from the inductor-compiled vision encoder graph. ## Reproduction steps ```bash docker run --runtime nvidia \ -v /path/to/Qwen3.6-35B-A3B-FP8:/model:ro \ -p 8001:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: iot/vllm:latest-jetson-thor` (tag `r38.2.arm64-sbsa-cu130-24.04`) **vLLM version**: 0.19.0 **Hardware**: NVIDIA Jetson AGX Thor — Blackwell GPU (SM 90+), 122 GB unified LPDDR5x memory, CUDA 13.0 **OS**: Ubuntu 24.04 (AR...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: CUBLAS_STATUS_EXECUTION_FAILED during CUDA graph compilation of BF16 vision encoder on NVIDIA Jetson AGX Thor (vLLM 0.19.0 regression) ## Your current environment **Container image**: `ghcr.io/nvidia-ai-iot/vllm:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: CUBLAS_STATUS_EXECUTION_FAILED during CUDA graph compilation of BF16 vision encoder on NVIDIA Jetson AGX Thor (vLLM 0.19.0 regression) ## Your current environment **Container image**: `ghcr.io/nvidia-ai-iot/vllm:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: ompilation of BF16 vision encoder on NVIDIA Jetson AGX Thor (vLLM 0.19.0 regression) ## Your current environment **Container image**: `ghcr.io/nvidia-ai-iot/vllm:latest-jetson-thor` (tag `r38.2.arm64-sbsa-cu130-24.04`)...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: GB unified LPDDR5x memory, CUDA 13.0 **OS**: Ubuntu 24.04 (ARM64 SBSA) **Model**: `Qwen/Qwen3.6-35B-A3B-FP8` (`qwen3_5_moe` architecture with vision encoder) **Python**: 3.12.12 ## 🐛 Describe the bug vLLM 0.19.0 (Jetson...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
