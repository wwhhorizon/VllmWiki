# vllm-project/vllm#36830: [Bug]: delta_text and delta_token_ids get out of sync when stop sequences are used.

| 字段 | 值 |
| --- | --- |
| Issue | [#36830](https://github.com/vllm-project/vllm/issues/36830) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: delta_text and delta_token_ids get out of sync when stop sequences are used.

### Issue 正文摘录

### Your current environment ``` ============================== System Info ============================== OS : Fedora Linux 42 (Workstation Edition) (x86_64) GCC version : (GCC) 15.2.1 20260123 (Red Hat 15.2.1-7) Clang version : 20.1.8 (Fedora 20.1.8-4.fc42) CMake version : version 3.31.6 Libc version : glibc-2.41 ============================== PyTorch Info ============================== PyTorch version : 2.9.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.7 (main, Nov 15 2024, 10:20:47) [GCC 13.3.1 20240522 (Red Hat 13.3.1-1)] (64-bit runtime) Python platform : Linux-6.18.8-100.fc42.x86_64-x86_64-with-glibc2.41 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA GeForce RTX 4060 Ti Nvidia driver version : 590.48.01 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU I...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: : Fedora Linux 42 (Workstation Edition) (x86_64) GCC version : (GCC) 15.2.1 20260123 (Red Hat 15.2.1-7) Clang version : 20.1.8 (Fedora 20.1.8-4.fc42) CMake version : version 3.31.6 Libc version : glibc-2.41 ==
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.9.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.7 (m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: d cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic vgif x2avic v_spec_ctrl vnmi avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni av...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.2 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: version : Could not collect CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA GeForce RTX 4060 Ti Nvidia driver version : 590.48.01 cuDNN version : Could not collect HIP runtime version : N/A MIO...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
