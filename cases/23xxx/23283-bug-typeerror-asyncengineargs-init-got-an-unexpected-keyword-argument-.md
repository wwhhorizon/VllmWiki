# vllm-project/vllm#23283: [Bug]: TypeError: AsyncEngineArgs.__init__() got an unexpected keyword argument 'disable_log_requests'

| 字段 | 值 |
| --- | --- |
| Issue | [#23283](https://github.com/vllm-project/vllm/issues/23283) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TypeError: AsyncEngineArgs.__init__() got an unexpected keyword argument 'disable_log_requests'

### Issue 正文摘录

### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.3 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.1+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.7 | packaged by conda-forge | (main, Dec 23 2023, 14:43:09) [GCC 12.3.0] (64-bit runtime) Python platform : Linux-5.15.0-1038-oracle-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : False CUDA runtime version : No CUDA CUDA_MODULE_LOADING set to : N/A GPU models and configuration : No CUDA Nvidia driver version : No CUDA cuDNN version : No CUDA HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info ============================== Architect...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 22.04.3 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ==============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.7.1+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.7 |...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: quests' bug;stale ### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.3 LTS (x86_64) GCC version : (Ubuntu 11.4....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: yncEngineArgs.__init__() got an unexpected keyword argument 'disable_log_requests' bug;stale ### Your current environment Collecting environment information... ============================== System Info ================...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd amd_ppin cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefil...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
