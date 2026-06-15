# vllm-project/vllm#18805: [Usage]: NCCL error when using tow AMD GPUs ( gfx1100 )

| 字段 | 值 |
| --- | --- |
| Issue | [#18805](https://github.com/vllm-project/vllm/issues/18805) |
| 状态 | closed |
| 标签 | rocm;usage |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: NCCL error when using tow AMD GPUs ( gfx1100 )

### Issue 正文摘录

### Your current environment ```text INFO 05-28 12:36:52 [__init__.py:243] Automatically detected platform rocm. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 4.0.2 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.8.0.dev20250526+rocm6.4 Is debug build : False CUDA used to build PyTorch : N/A ROCM used to build PyTorch : 6.4.43482-0f2d60242 ============================== Python Environment ============================== Python version : 3.12.3 (main, Feb 4 2025, 14:48:35) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.11.0-26-generic-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : AMD Radeon RX 7900 XTX (gfx1100) Nvidia driver version : Could not collect cuDNN version : Could not collect HIP runtime version : 6.4.434...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 4.0.2 Libc version : glibc-2.39 ==================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Usage]: NCCL error when using tow AMD GPUs ( gfx1100 ) rocm;usage ### Your current environment ```text INFO 05-28 12:36:52 [__init__.py:243] Automatically detected platform rocm. Collecting environment information... =...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: _.py:243] Automatically detected platform rocm. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: d_ppin arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip rdpid overflow_recov succor smca sev sev_es Virtualization: AMD-V...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: aries ============================== [pip3] numpy==1.26.4 [pip3] pytorch-triton-rocm==3.3.1+gitc8757738 [pip3] pyzmq==26.4.0 [pip3] torch==2.8.0.dev20250526+rocm6.4 [pip3] torchaudio==2.6.0.dev20250526+rocm6.4 [pip3] to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
