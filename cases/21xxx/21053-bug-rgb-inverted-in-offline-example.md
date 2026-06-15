# vllm-project/vllm#21053: [Bug]: RGB inverted in offline example?

| 字段 | 值 |
| --- | --- |
| Issue | [#21053](https://github.com/vllm-project/vllm/issues/21053) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RGB inverted in offline example?

### Issue 正文摘录

### Your current environment ============================== System Info ============================== OS : Rocky Linux 9.5 (Blue Onyx) (x86_64) GCC version : (GCC) 12.3.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.34 ============================== PyTorch Info ============================== PyTorch version : 2.5.1+cu121 Is debug build : False CUDA used to build PyTorch : 12.1 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.3 (main, Jun 25 2023, 13:17:30) [GCC 12.3.0] (64-bit runtime) Python platform : Linux-5.14.0-503.40.1.el9_5.x86_64-x86_64-with-glibc2.34 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.2.91 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA A100-SXM4-40GB GPU 1: NVIDIA A100-SXM4-40GB GPU 2: NVIDIA A100-SXM4-40GB GPU 3: NVIDIA A100-SXM4-40GB Nvidia driver version : 570.133.20 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ==============================...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: OS : Rocky Linux 9.5 (Blue Onyx) (x86_64) GCC version : (GCC) 12.3.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.34 ============================== P
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.5.1+cu121 Is debug build : False CUDA used to build PyTorch : 12.1 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.3 (m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: untime version : 12.2.91 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA A100-SXM4-40GB GPU 1: NVIDIA A100-SXM4-40GB GPU 2: NVIDIA A100-SXM4-40GB GPU 3: NVIDIA A100-SXM4-40GB Nvidia driver...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: d_ppin arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip rdpid overflow_recov succor smca sev sev_es L1d cache: 1.5 MiB (4...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [pip3] torchvision==0.20.1+cu121 [pip3] transformers==4.50.0.dev0 [pip3] triton==3.1.0 [conda] Could not collect ============================== vLLM Info ============================== ROCM Version : Could not collect N...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
