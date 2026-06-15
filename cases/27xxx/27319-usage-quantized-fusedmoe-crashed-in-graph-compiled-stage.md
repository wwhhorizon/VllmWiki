# vllm-project/vllm#27319: [Usage]:  Quantized FusedMoE crashed in graph compiled stage

| 字段 | 值 |
| --- | --- |
| Issue | [#27319](https://github.com/vllm-project/vllm/issues/27319) |
| 状态 | closed |
| 标签 | rocm;usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]:  Quantized FusedMoE crashed in graph compiled stage

### Issue 正文摘录

### Your current environment ```text ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : 19.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-6.4.3 25224 d366fa84f3fdcbd4b10847ebd5db572ae12a34fb) CMake version : version 3.31.6 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+rocm6.4 Is debug build : False CUDA used to build PyTorch : N/A ROCM used to build PyTorch : 6.4.43482-0f2d60242 ============================== Python Environment ============================== Python version : 3.12.11 | packaged by conda-forge | (main, Jun 4 2025, 14:45:31) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.8.0-79-generic-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : AMD Radeon PRO W7900 Dual Slot (gfx1100) Nvidia driver version : Could not collect cuDNN version : Could not collect HIP runtime versi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Usage]: Quantized FusedMoE crashed in graph compiled stage rocm;usage ### Your current environment ```text ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Usage]: Quantized FusedMoE crashed in graph compiled stage rocm;usage ### Your current environment ```text ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: pb_ret arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif x2avic v_spec_ctrl vnmi avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqd...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Usage]: Quantized FusedMoE crashed in graph compiled stage rocm;usage ### Your current environment ```text ============================== System Info ============================== OS : Ubuntu
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: ch version : 2.8.0+rocm6.4 Is debug build : False CUDA used to build PyTorch : N/A ROCM used to build PyTorch : 6.4.43482-0f2d60242 ============================== Python Environment ============================== Python...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
