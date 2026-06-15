# vllm-project/vllm#28629: [Usage]: TPOT per request information was not collected by vllm bench serve

| 字段 | 值 |
| --- | --- |
| Issue | [#28629](https://github.com/vllm-project/vllm/issues/28629) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: TPOT per request information was not collected by vllm bench serve

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 4.1.0 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+xpu Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Aug 14 2025, 17:47:21) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.14.0-1006-intel-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : False CUDA runtime version : No CUDA CUDA_MODULE_LOADING set to : N/A GPU models and configuration : No CUDA Nvidia driver version : No CUDA cuDNN version : No CUDA HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info =============================...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ========= OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 4.1.0 Libc version : glibc-2.39 ==================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ch version : 2.8.0+xpu Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: TPOT per request information was not collected by vllm bench serve usage;stale ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... ==================...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: cqm_mbm_total cqm_mbm_local split_lock_detect user_shstk avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts hwp hwp_act_window hwp_epp hwp_pkg_req vnmi avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmul...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: TPOT per request information was not collected by vllm bench serve usage;stale ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... ==================...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
