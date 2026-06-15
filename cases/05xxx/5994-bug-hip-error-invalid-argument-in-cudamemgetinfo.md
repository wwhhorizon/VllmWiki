# vllm-project/vllm#5994: [Bug]: HIP error: invalid argument  in cudaMemGetInfo

| 字段 | 值 |
| --- | --- |
| Issue | [#5994](https://github.com/vllm-project/vllm/issues/5994) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;import_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: HIP error: invalid argument  in cudaMemGetInfo

### Issue 正文摘录

### Your current environment ```text Collecting environment information... There was a problem when trying to write in your cache folder (/root/.cache/huggingface/hub). You should set the environment variable TRANSFORMERS_CACHE to a writable directory. WARNING 06-30 12:42:35 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch version: 2.5.0.dev20240613+rocm6.1 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.1.40091-a8dbc0c19 OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.5 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.0-113-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: AMD Instinct MI100 (gfx908:sramecc+:xnack-) Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime version: 6.1.40091 MIOpen runtime version: 3.1.0 Is XNNPACK available: True CPU: Architecture: x86_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: writable directory. WARNING 06-30 12:42:35 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch version: 2.5.0.dev20240613+rocm6.1 Is debug build: False CUDA use...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: HIP error: invalid argument in cudaMemGetInfo bug;rocm ### Your current environment ```text Collecting environment information... There was a problem when trying to write in your cache folder (/root/.cache/huggin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: bug;rocm ### Your current environment ```text Collecting environment information... There was a problem when trying to write in your cache folder (/root/.cache/huggingface/hub). You should set the environment variable T...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: d_ppin arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip rdpid overflow_recov succor smca sme sev sev_es Virtualization: A...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: libraries: [pip3] libtorch==1.2.0.1 [pip3] numpy==1.26.4 [pip3] pytorch-triton-rocm==3.0.0+01cbe5045a [pip3] torch==2.5.0.dev20240613+rocm6.1 [pip3] torchaudio==2.4.0.dev20240614+rocm6.1 [pip3] torchvision==0.19.0.dev20...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
