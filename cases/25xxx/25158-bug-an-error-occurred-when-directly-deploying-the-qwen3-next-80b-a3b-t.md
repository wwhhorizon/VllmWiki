# vllm-project/vllm#25158: [Bug]: An error occurred when directly deploying the Qwen3-Next 80B-A3B-Thinking model saved by the save_pretrained of transformers using vllm. However, directly deploying the original model was normal

| 字段 | 值 |
| --- | --- |
| Issue | [#25158](https://github.com/vllm-project/vllm/issues/25158) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: An error occurred when directly deploying the Qwen3-Next 80B-A3B-Thinking model saved by the save_pretrained of transformers using vllm. However, directly deploying the original model was normal

### Issue 正文摘录

### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.4 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.28.3 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.14 (main, May 6 2024, 19:42:50) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-5.4.0-42-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.4.99 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA A800-SXM4-80GB GPU 1: NVIDIA A800-SXM4-80GB GPU 2: NVIDIA A800-SXM4-80GB GPU 3: NVIDIA A800-SXM4-80GB GPU 4: NVIDIA A800-SXM4-80GB GPU 5: NVIDIA A800-SXM4-80GB GPU 6: NVIDIA A800-SXM4-80GB GPU 7: NVIDIA A800-SXM4-80GB Nvidia driver version : 570....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 22.04.4 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.28.3 Libc version : glibc-2.35 =================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.14 (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: An error occurred when directly deploying the Qwen3-Next 80B-A3B-Thinking model saved by the save_pretrained of transformers using vllm. However, directly deploying the original model was normal bug;stale ### You...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: sing vllm. However, directly deploying the original model was normal bug;stale ### Your current environment Collecting environment information... ============================== System Info ==============================...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: === Versions of relevant libraries ============================== [pip3] flashinfer==0.1.6+cu124torch2.4 [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu11==11.10.3.66 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
