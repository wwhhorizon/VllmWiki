# vllm-project/vllm#33962: [Bug]: Realtime transcription completes but server never sends transcription.done when final commit is received during slow streaming

| 字段 | 值 |
| --- | --- |
| Issue | [#33962](https://github.com/vllm-project/vllm/issues/33962) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Realtime transcription completes but server never sends transcription.done when final commit is received during slow streaming

### Issue 正文摘录

### Your current environment ``` Collecting environment information... uv is set ============================== System Info ============================== OS : Ubuntu 24.04.1 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : 18.1.3 (1ubuntu1) CMake version : Could not collect Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.9.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Feb 4 2025, 14:48:35) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.12.63-84.121.amzn2023.x86_64-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.93 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA L40S Nvidia driver version : 580.105.08 cuDNN version : Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.8.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.8.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ========= OS : Ubuntu 24.04.1 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : 18.1.3 (1ubuntu1) CMake version : Could not collect Libc version : glibc-2.39 ==============
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: streaming bug ### Your current environment ``` Collecting environment information... uv is set ============================== System Info ============================== OS : Ubuntu 24.04.1 LTS (x86_64) GCC version : (Ub...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Mitigation; Sa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.9.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (m...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.2 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
