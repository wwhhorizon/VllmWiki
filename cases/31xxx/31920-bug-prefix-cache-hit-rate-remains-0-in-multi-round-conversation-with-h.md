# vllm-project/vllm#31920: [Bug]: Prefix cache hit rate remains 0 in multi-round conversation with history of identical prompts.

| 字段 | 值 |
| --- | --- |
| Issue | [#31920](https://github.com/vllm-project/vllm/issues/31920) |
| 状态 | open |
| 标签 | bug;rocm;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | cache;cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Prefix cache hit rate remains 0 in multi-round conversation with history of identical prompts.

### Issue 正文摘录

### Your current environment ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : 20.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-7.0.2 25385 0dda3adf56766e0aac0d03173ced3759e1ffecbc) CMake version : version 3.31.6 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+gitd02b22b Is debug build : False CUDA used to build PyTorch : N/A ROCM used to build PyTorch : 7.0.51831-7c9236b16 ============================== Python Environment ============================== Python version : 3.12.3 (main, Aug 14 2025, 17:47:21) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.14.0-36-generic-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : AMD Radeon Graphics (gfx1100) Nvidia driver version : Could not collect cuDNN version : Could not collect HIP runtime version : 7.0.51831 MIOpen runtime version : 3.5...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ========= OS : Ubuntu 24.04.3 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : 20.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-7.0.2 25385 0dda3adf56766e0aac0d03173ced375...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ins 0 in multi-round conversation with history of identical prompts. bug;rocm;stale ### Your current environment ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (x86_64)...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: Prefix cache hit rate remains 0 in multi-round conversation with history of identical prompts. bug;rocm;stale ### Your current environment ============================== System Info =============================
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: sion : Could not collect CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : AMD Radeon Graphics (gfx1100) Nvidia driver version : Could not collect cuDNN version : Could not collect HIP runtime version : 7...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: in multi-round conversation with history of identical prompts. bug;rocm;stale ### Your current environment ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (x86_64) GCC v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
