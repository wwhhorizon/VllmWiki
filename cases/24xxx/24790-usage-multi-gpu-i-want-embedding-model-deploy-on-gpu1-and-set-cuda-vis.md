# vllm-project/vllm#24790: [Usage]: multi-gpu，I want embedding model deploy on GPU1, and set CUDA_VISIBLE_DEVICES=1, in vllm start script file， but vllm service still malloc memory of GPU 0 。

| 字段 | 值 |
| --- | --- |
| Issue | [#24790](https://github.com/vllm-project/vllm/issues/24790) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: multi-gpu，I want embedding model deploy on GPU1, and set CUDA_VISIBLE_DEVICES=1, in vllm start script file， but vllm service still malloc memory of GPU 0 。

### Issue 正文摘录

### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.1+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 | packaged by conda-forge | (main, Jun 4 2025, 14:45:31) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.8.0-65-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.4.131 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA GeForce RTX 4090 GPU 1: NVIDIA GeForce RTX 4090 Nvidia driver version : 570.133.20 cuDNN version : Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.8.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Usage]: multi-gpu，I want embedding model deploy on GPU1, and set CUDA_VISIBLE_DEVICES=1, in vllm start script file， but vllm service still malloc memory of GPU 0 。 usage;stale ### Your current environment Collecting en...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: multi-gpu，I want embedding model deploy on GPU1, and set CUDA_VISIBLE_DEVICES=1, in vllm start script file， but vllm service still malloc memory of GPU 0 。 usage;stale ### Your current environment Collecting en...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: start script file， but vllm service still malloc memory of GPU 0 。 usage;stale ### Your current environment Collecting environment information... ============================== System Info ==============================...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 2.7.1 [pip3] torchvision==0.22.1 [pip3] transformers==4.57.0.dev0 [pip3] triton==3.3.1 [conda] _anaconda_depends 2024.10 py312_mkl_0 defaults [conda] blas 1.0 mkl defaults [conda] mkl 2023.1.0

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
