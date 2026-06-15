# vllm-project/vllm#15012: [Usage]: Transcription "Maximum clip duration (30s) exceeded

| 字段 | 值 |
| --- | --- |
| Issue | [#15012](https://github.com/vllm-project/vllm/issues/15012) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Transcription "Maximum clip duration (30s) exceeded

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Rocky Linux 9.4 (Blue Onyx) (x86_64) GCC version: (GCC) 11.5.0 20240719 (Red Hat 11.5.0-2) Clang version: Could not collect CMake version: version 3.26.5 Libc version: glibc-2.34 Python version: 3.12.9 | packaged by Anaconda, Inc. | (main, Feb 6 2025, 18:56:27) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.14.0-427.37.1.el9_4.x86_64-x86_64-with-glibc2.34 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 3060 GPU 1: NVIDIA GeForce RTX 3060 Nvidia driver version: 560.35.03 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture : x86_64 Mode(s) opératoire(s) des processeurs : 32-bit, 64-bit Tailles des adresses: 48 bits physical, 48 bits virtual Boutisme : Little Endian Processeur(s) : 24 Liste de processeur(s) en ligne : 0-23 Identifiant constructeur : AuthenticAMD Identifiant constructeur du BIOS : Adv...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: t environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Rocky Linux 9.4 (Blue Onyx) (x86_64...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: n collect_env.py` ``` PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Rocky Linux 9.4 (Blue Onyx) (x86_64) GCC version: (GCC) 11.5.0 20240719 (Red...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 3060 GPU 1: NVIDIA GeForce RTX 3060 Nvidia driver version: 560.35.03 cuDNN version: Could not c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: noinvd arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca fsrm d...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dio==2.5.1 [pip3] torchvision==0.20.1 [pip3] transformers==4.49.0 [pip3] triton==3.1.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.4.5.8 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.4.127

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
