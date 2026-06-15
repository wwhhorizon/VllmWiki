# vllm-project/vllm#20445: [Bug]: quantization我看是有nvfp4的，为什么0.9.1中告诉我没有这个量化方式可选

| 字段 | 值 |
| --- | --- |
| Issue | [#20445](https://github.com/vllm-project/vllm/issues/20445) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: quantization我看是有nvfp4的，为什么0.9.1中告诉我没有这个量化方式可选

### Issue 正文摘录

### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.28.6 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.11 (main, Dec 11 2024, 16:28:39) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-6.6.87.2-microsoft-standard-WSL2-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.4.99 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA GeForce RTX 3060 Nvidia driver version : 572.16 cuDNN version : Probably one of the following: /usr/local/cuda-12.4/targets/x86_64-linux/lib/libcudnn.so.8.9.6 /usr/local/cuda-12.4/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.28.6 Libc version : glibc-2.35 =================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.7.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.11 (...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: quantization我看是有nvfp4的，为什么0.9.1中告诉我没有这个量化方式可选 bug ### Your current environment Collecting environment information... ============================== System Info ============================== OS
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: 告诉我没有这个量化方式可选 bug ### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4....
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: arlin', 'bitblas', 'bitsandbytes', 'compressed-tensors', 'deepspeedfp', 'experts_int8', 'fbgemm_fp8', 'fp8', 'gguf', 'gptq', 'gptq_bitblas', 'gptq_marlin', 'gptq_marlin_24', 'hqq', 'ipex', 'marlin', 'modelopt', 'modelop...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
