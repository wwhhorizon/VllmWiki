# vllm-project/vllm#25127: [Bug]: vLLM server won’t exit; process stuck in R state and GPU becomes unusable (H100 80GB, gpu_memory_utilization=0.6)

| 字段 | 值 |
| --- | --- |
| Issue | [#25127](https://github.com/vllm-project/vllm/issues/25127) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda;kernel;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM server won’t exit; process stuck in R state and GPU becomes unusable (H100 80GB, gpu_memory_utilization=0.6)

### Issue 正文摘录

### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 18.04.6 LTS (x86_64) GCC version : (Ubuntu 10.3.0-1ubuntu1~18.04~1) 10.3.0 Clang version : Could not collect CMake version : version 3.10.2 Libc version : glibc-2.28 ============================== PyTorch Info ============================== PyTorch version : 2.7.1+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.13 (main, Jun 5 2025, 13:12:00) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-5.4.0-150-generic-x86_64-with-glibc2.28 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 9.1.85 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA H100 PCIe GPU 1: NVIDIA H100 PCIe Nvidia driver version : 530.41.03 cuDNN version : Probably one of the following: /usr/local/cuda-12.1/targets/x86_64-linux/lib/libcudnn.so.8 /usr/local/cuda-12.1/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 18.04.6 LTS (x86_64) GCC version : (Ubuntu 10.3.0-1ubuntu1~18.04~1) 10.3.0 Clang version : Could not collect CMake version : version 3.10.2 Libc version : glibc-2.28 ===============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: LM server won’t exit; process stuck in R state and GPU becomes unusable (H100 80GB, gpu_memory_utilization=0.6) bug;stale ### Your current environment Collecting environment information... ==============================...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: on=0.6) bug;stale ### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 18.04.6 LTS (x86_64) GCC version : (Ubuntu 10.3....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dio==2.7.1 [pip3] torchvision==0.22.1 [pip3] transformers==4.56.1 [pip3] triton==3.3.1 [conda] blas 1.0 mkl [conda] cuda-cudart 12.1.105 0 nvidia [conda] cuda-cupti 12.1.1
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: nference. The machine has a single NVIDIA H100 (80GB). I set the maximum GPU memory utilization to 0.6 (60%). The vLLM server often fails to exit cleanly. After I try to stop it, the entire GPU gets wedged: ps shows a p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
