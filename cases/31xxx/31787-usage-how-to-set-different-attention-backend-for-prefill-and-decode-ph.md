# vllm-project/vllm#31787: [Usage]: How to set different attention backend for prefill and decode phases?

| 字段 | 值 |
| --- | --- |
| Issue | [#31787](https://github.com/vllm-project/vllm/issues/31787) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting |
| 子分类 |  |
| Operator 关键词 | attention;cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to set different attention backend for prefill and decode phases?

### Issue 正文摘录

### Your current environment ```text Collecting environment information... ============================== System Info ============================== OS : Alibaba Cloud Linux 3 (Soaring Falcon) (x86_64) GCC version : (GCC) 10.2.1 20200825 (Alibaba 10.2.1-3.8 2.32) Clang version : Could not collect CMake version : version 3.31.2 Libc version : glibc-2.32 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.16 (main, Dec 11 2024, 16:24:50) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-5.10.134-16.3.al8.x86_64-x86_64-with-glibc2.32 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.61 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA H20 GPU 1: NVIDIA H20 GPU 2: NVIDIA H20 GPU 3: NVIDIA H20 GPU 4: NVIDIA H20 GPU 5: NVIDIA H20 GPU 6: NVIDIA H20 GPU 7: NVIDIA H20 Nvidia driver version : 535.183.06 cuDNN version : Probably one of th...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: : Alibaba Cloud Linux 3 (Soaring Falcon) (x86_64) GCC version : (GCC) 10.2.1 20200825 (Alibaba 10.2.1-3.8 2.32) Clang version : Could not collect CMake version : version 3.31.2 Libc version : glibc-2.32 =======
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: [Usage]: How to set different attention backend for prefill and decode phases? usage;stale ### Your current environment ```text Collecting environment information... ============================== System Info ==========...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.16 (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: age;stale ### Your current environment ```text Collecting environment information... ============================== System Info ============================== OS : Alibaba Cloud Linux 3 (Soaring Falcon) (x86_64) GCC ver...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: How to set different attention backend for prefill and decode phases? usage;stale ### Your current environment ```text Collecting environment information... ============================== System Info ==========...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
