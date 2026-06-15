# vllm-project/vllm#34583: [Bug] Missing Vocabulary Validation for MTP and Eagle Speculative Methods leads to potential OOB Access

| 字段 | 值 |
| --- | --- |
| Issue | [#34583](https://github.com/vllm-project/vllm/issues/34583) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] Missing Vocabulary Validation for MTP and Eagle Speculative Methods leads to potential OOB Access

### Issue 正文摘录

### Your current environment ``` Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : Could not collect CMake version : version 3.31.10 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.9.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.12 (main, Oct 10 2025, 08:52:57) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-6.6.105+-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.93 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: Tesla T4 Nvidia driver version : 580.82.07 cuDNN version : Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.8.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.8.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.8.0 /usr/lib/x86_64-linux-gnu/li...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : Could not collect CMake version : version 3.31.10 Libc version : glibc-2.35 ==============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.9.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.12 (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ess bug;stale ### Your current environment ``` Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.1 [pip3] numpy==2.0.2 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cccl-cu12==12.9.27 [pip3] nvidia-cuda-cupti-cu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug] Missing Vocabulary Validation for MTP and Eagle Speculative Methods leads to potential OOB Access bug;stale ### Your current environment ``` Collecting environment information... ============================== Sys...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
