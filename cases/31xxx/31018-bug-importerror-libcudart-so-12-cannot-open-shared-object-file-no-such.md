# vllm-project/vllm#31018: [Bug]: ImportError: libcudart.so.12: cannot open shared object file: No such file or directory

| 字段 | 值 |
| --- | --- |
| Issue | [#31018](https://github.com/vllm-project/vllm/issues/31018) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ImportError: libcudart.so.12: cannot open shared object file: No such file or directory

### Issue 正文摘录

### Your current environment ``` Collecting environment information... uv is set ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 3.28.3 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.9.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Nov 6 2025, 13:44:16) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.14.0-37-generic-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 13.0.48 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition GPU 1: NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition Nvidia driver version : 580.95.05 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Bug]: ImportError: libcudart.so.12: cannot open shared object file: No such file or directory bug ### Your current environment ``` Collecting environment information... uv is set ============================== System
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Bug]: ImportError: libcudart.so.12: cannot open shared object file: No such file or directory bug ### Your current environment ``` Collecting environment information... uv is set ============================== System I...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: directory bug ### Your current environment ``` Collecting environment information... uv is set ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (x86_64) GCC version : (Ub...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.5.3 [pip3] numpy==2.2.6 [pip3] nvidia-cublas==13.0.0.19 [pip3] nvidia-cuda-cupti==13.0.48 [pip3] nvidia-cuda-nvrtc==13.0.48 [...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: n cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif x2avic v_spec_ctrl vnmi avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqd...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
