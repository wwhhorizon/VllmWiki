# vllm-project/vllm#20397: [Bug]: Regression- due to hiding of model_executor, can no longer destroy model_executor and free up memory

| 字段 | 值 |
| --- | --- |
| Issue | [#20397](https://github.com/vllm-project/vllm/issues/20397) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Regression- due to hiding of model_executor, can no longer destroy model_executor and free up memory

### Issue 正文摘录

### Your current environment INFO 07-02 14:59:37 [__init__.py:244] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.13 (main, Jun 5 2025, 13:12:00) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-6.8.0-60-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.4.131 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA RTX A5000 GPU 1: NVIDIA RTX A5000 GPU 2: NVIDIA RTX A5000 GPU 3: NVIDIA RTX A5000 Nvidia driver version : 570.153.02 cuDNN version : Could not collect HIP runtime versio...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 =================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: t INFO 07-02 14:59:37 [__init__.py:244] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Regression- due to hiding of model_executor, can no longer destroy model_executor and free up memory bug;stale ### Your current environment INFO 07-02 14:59:37 [__init__.py:244] Automatically detected platform cu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: el_executor, can no longer destroy model_executor and free up memory bug;stale ### Your current environment INFO 07-02 14:59:37 [__init__.py:244] Automatically detected platform cuda. Collecting environment information....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: veerptr rdpru wbnoinvd amd_ppin brs arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid over...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
