# vllm-project/vllm#29148: [Usage]: Deployment of the embedding models

| 字段 | 值 |
| --- | --- |
| Issue | [#29148](https://github.com/vllm-project/vllm/issues/29148) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Deployment of the embedding models

### Issue 正文摘录

### Your current environment ```text ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.16 (main, Dec 11 2024, 16:24:50) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-5.15.0-161-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.61 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA GeForce RTX 5090 GPU 1: NVIDIA GeForce RTX 5090 GPU 2: NVIDIA GeForce RTX 5090 GPU 3: NVIDIA GeForce RTX 5090 GPU 4: NVIDIA GeForce RTX 5090 GPU 5: NVIDIA GeForce RTX 5090 GPU 6: NVIDIA GeForce RTX 5090 GPU 7: NVIDIA GeForce RTX 5090 Nvidia driver version : 570.172.08 cuDN...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.16 (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Deployment of the embedding models usage ### Your current environment ```text ==============================
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: to use vllm When deploying the embedding model, I found that the actual GPU memory usage included not only the model itself but also kv_cache. Is this a reasonable phenomenon? In version v0.9.0, the GPU memory usage was...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: orch version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
