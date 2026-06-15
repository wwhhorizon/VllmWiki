# vllm-project/vllm#39049: [Bug]: Gemma 4 FP8 dynamic quantization = gibberish output

| 字段 | 值 |
| --- | --- |
| Issue | [#39049](https://github.com/vllm-project/vllm/issues/39049) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma 4 FP8 dynamic quantization = gibberish output

### Issue 正文摘录

### Your current environment Collecting environment information... ============================== System Info ============================== OS : Debian GNU/Linux 13 (trixie) (x86_64) GCC version : (Debian 14.2.0-19) 14.2.0 Clang version : Could not collect CMake version : version 3.31.6 Libc version : glibc-2.41 ============================== PyTorch Info ============================== PyTorch version : 2.10.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.13.5 (main, Jun 25 2025, 18:55:22) [GCC 14.2.0] (64-bit runtime) Python platform : Linux-6.12.74+deb13+1-amd64-x86_64-with-glibc2.41 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 13.1.115 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA GeForce RTX 3090 GPU 1: NVIDIA GeForce RTX 3090 GPU 2: NVIDIA GeForce RTX 3090 GPU 3: NVIDIA GeForce RTX 3090 Nvidia driver version : 595.45.04 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK av...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: OS : Debian GNU/Linux 13 (trixie) (x86_64) GCC version : (Debian 14.2.0-19) 14.2.0 Clang version : Could not collect CMake version : version 3.31.6 Libc version : glibc-2.41 =============================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.10.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.13.5 (...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: Gemma 4 FP8 dynamic quantization = gibberish output bug ### Your current environment Collecting environment information... ============================== System Info ============================== OS
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Gemma 4 FP8 dynamic quantization = gibberish output bug ### Your current environment Collecting environment information... ============================== System Info ============================== OS
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: d cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic vgif x2avic v_spec_ctrl vnmi avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni av...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
