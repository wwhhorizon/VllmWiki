# vllm-project/vllm#20748: [Bug]: sm_120 support appears to be missing in pre-built whl for 0.9.2

| 字段 | 值 |
| --- | --- |
| Issue | [#20748](https://github.com/vllm-project/vllm/issues/20748) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: sm_120 support appears to be missing in pre-built whl for 0.9.2

### Issue 正文摘录

### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 | packaged by Anaconda, Inc. | (main, Jun 5 2025, 13:09:17) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-6.8.0-60-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.61 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA GeForce RTX 5090 Nvidia driver version : 575.57.08 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info =======...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 =================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: sm_120 support appears to be missing in pre-built whl for 0.9.2 bug;stale ### Your current environment Collecting environment information... ============================== System Info ===========================
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: r 0.9.2 bug;stale ### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 12.3....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ug]: sm_120 support appears to be missing in pre-built whl for 0.9.2 bug;stale ### Your current environment Collecting environment information... ============================== System Info ==============================...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: aves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local user_shstk avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd cppc amd_ibpb_ret arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pau...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
