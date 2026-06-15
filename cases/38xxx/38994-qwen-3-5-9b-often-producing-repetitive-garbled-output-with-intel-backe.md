# vllm-project/vllm#38994: Qwen-3.5 9B often producing repetitive/garbled output with Intel Backend

| 字段 | 值 |
| --- | --- |
| Issue | [#38994](https://github.com/vllm-project/vllm/issues/38994) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Qwen-3.5 9B often producing repetitive/garbled output with Intel Backend

### Issue 正文摘录

### Your current environment This was the output from running python collect_env.py (running in docker image) ============================== System Info ============================== OS : Ubuntu 24.04.4 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 Clang version : Could not collect CMake version : version 4.3.1 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.10.0+xpu Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Mar 3 2026, 12:15:18) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.17.0-20-generic-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : False CUDA runtime version : No CUDA CUDA_MODULE_LOADING set to : N/A GPU models and configuration : No CUDA Nvidia driver version : No CUDA cuDNN version : No CUDA HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info ==============================...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 11: Qwen-3.5 9B often producing repetitive/garbled output with Intel Backend bug ### Your current environment This was the output from running python collect_env.py (running in docker image) ============================== S...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: h version : 2.10.0+xpu Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: noinvd arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip rdpid overflow_recov succor smca sev sev_es Virtualization: AMD-V...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ro irperf xsaveerptr rdpru wbnoinvd arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip rdpid overflow_recov succor smca sev...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: Qwen-3.5 9B often producing repetitive/garbled output with Intel Backend bug ### Your current environment This was the output from running python collect_env.py (running in docker image) ==============================

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
