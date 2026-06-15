# vllm-project/vllm#24752: [Bug]: Some Bert models no longer compatible for BertForSequenceClassification

| 字段 | 值 |
| --- | --- |
| Issue | [#24752](https://github.com/vllm-project/vllm/issues/24752) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Some Bert models no longer compatible for BertForSequenceClassification

### Issue 正文摘录

### Your current environment ``` Collecting environment information... uv is set ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.1+rocm6.3 Is debug build : False CUDA used to build PyTorch : N/A ROCM used to build PyTorch : 6.3.42131-fa1d09cbd ============================== Python Environment ============================== Python version : 3.13.3 (main, Apr 9 2025, 04:03:52) [Clang 20.1.0 ] (64-bit runtime) Python platform : Linux-6.8.0-79-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.6.85 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : AMD Radeon PRO W7900 (gfx1100) Nvidia driver version : Could not collect cuDNN version : Could not collect HIP runtime version : 6.3.42131 MIOpen runtime version : 3.3.0 Is XNNPACK available : True ===========================...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 ===============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: e Bert models no longer compatible for BertForSequenceClassification bug;rocm ### Your current environment ``` Collecting environment information... uv is set ============================== System Info =================...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Some Bert models no longer compatible for BertForSequenceClassification bug;rocm ### Your current environment ``` Collecting environment information... uv is set ============================== System Info =======...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: eerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca sev sev_es Virtualization: AMD-V L1d cache: 192 KiB (6...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: -nvjitlink-cu12==12.6.85 [pip3] nvidia-nvtx-cu12==12.6.77 [pip3] pytorch-triton-rocm==3.3.1 [pip3] pytorch-warmup==0.2.0 [pip3] pyzmq==27.0.0 [pip3] torch==2.7.1+rocm6.3 [pip3] torchaudio==2.7.1 [pip3] torchvision==0.22...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
