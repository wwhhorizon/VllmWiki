# vllm-project/vllm#5731: [Bug]: RuntimeError: CUDA error: CUBLAS_STATUS_EXECUTION_FAILED when calling cublasLtMatmul with transpose_mat1 t transpose_mat2 n m 9216 n 3398 k 7168 mat1_ld 7168 mat2_ld 7168 result_ld 9216 computeType 68 scaleType 0

| 字段 | 值 |
| --- | --- |
| Issue | [#5731](https://github.com/vllm-project/vllm/issues/5731) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: CUDA error: CUBLAS_STATUS_EXECUTION_FAILED when calling cublasLtMatmul with transpose_mat1 t transpose_mat2 n m 9216 n 3398 k 7168 mat1_ld 7168 mat2_ld 7168 result_ld 9216 computeType 68 scaleType 0

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04 LTS (x86_64) GCC version: (Ubuntu 11.2.0-19ubuntu1) 11.2.0 Clang version: Could not collect CMake version: version 3.29.5 Libc version: glibc-2.35 Python version: 3.10.14 (main, May 6 2024, 19:42:50) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-101-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L40 GPU 1: NVIDIA L40 GPU 2: NVIDIA L40 GPU 3: NVIDIA L40 GPU 4: NVIDIA L40 GPU 5: NVIDIA L40 GPU 6: NVIDIA L40 GPU 7: NVIDIA L40 Nvidia driver version: 535.161.07 cuDNN version: Probably one of the following: /usr/local/cuda-12.2/targets/x86_64-linux/lib/libcudnn.so.8 /usr/local/cuda-12.2/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8 /usr/local/cuda-12.2/targets/x86_64-linux/lib/libcudnn_adv_train.so.8 /usr/local/cuda-12.2/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8 /usr/local/cuda-12.2/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8 /usr/local/cuda...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: rrent environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04 LTS (x86_64) GCC versi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: 16 n 3398 k 7168 mat1_ld 7168 mat2_ld 7168 result_ld 9216 computeType 68 scaleType 0 bug;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: Fals...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: RuntimeError: CUDA error: CUBLAS_STATUS_EXECUTION_FAILED when calling cublasLtMatmul with transpose_mat1 t transpose_mat2 n m 9216 n 3398 k 7168 mat1_ld 7168 mat2_ld 7168 result_ld 9216 computeType 68 scaleType 0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: bug;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04 L...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: nvironment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04 LTS (x86_64) GCC version: (Ubuntu 11.2.0-19ubuntu1) 11.2.0 C...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
