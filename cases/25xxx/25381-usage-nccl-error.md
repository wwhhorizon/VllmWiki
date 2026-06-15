# vllm-project/vllm#25381: [Usage]: NCCL ERROR

| 字段 | 值 |
| --- | --- |
| Issue | [#25381](https://github.com/vllm-project/vllm/issues/25381) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: NCCL ERROR

### Issue 正文摘录

### Your current environment ```text ### environment warnings.warn( ============================== System Info ============================== OS : CentOS Linux 7 (Core) (x86_64) GCC version : (GCC) 4.8.5 20150623 (Red Hat 4.8.5-44) Clang version : Could not collect CMake version : version 2.8.12.2 Libc version : glibc-2.17 ============================== PyTorch Info ============================== PyTorch version : 2.6.0+cu124 Is debug build : False CUDA used to build PyTorch : 12.4 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.13 | packaged by conda-forge | (main, Dec 23 2023, 15:36:39) [GCC 12.3.0] (64-bit runtime) Python platform : Linux-3.10.0-1160.119.1.el7.x86_64-x86_64-with-glibc2.17 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.4.99 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA GeForce RTX 3090 GPU 1: NVIDIA GeForce RTX 3090 GPU 2: NVIDIA GeForce RTX 3090 GPU 3: NVIDIA GeForce RTX 3090 Nvidia driver version : 550.107.02 cuDNN version : Could not collect HIP runtime versio...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ====== OS : CentOS Linux 7 (Core) (x86_64) GCC version : (GCC) 4.8.5 20150623 (Red Hat 4.8.5-44) Clang version : Could not collect CMake version : version 2.8.12.2 Libc version : glibc-2.17 =============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.6.0+cu124 Is debug build : False CUDA used to build PyTorch : 12.4 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.13 |...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: untime version : 12.4.99 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA GeForce RTX 3090 GPU 1: NVIDIA GeForce RTX 3090 GPU 2: NVIDIA GeForce RTX 3090 GPU 3: NVIDIA GeForce RTX 3090 Nvidi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: transformers==4.52.4 [pip3] transformers-stream-generator==0.0.5 [pip3] triton==3.1.0 [conda] cuda-version 12.9 3 nvidia [conda] libopenvino-pytorch-frontend 2025.2.0 hecca717_1 conda-forge [conda] nccl 2.27.7
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: orch version : 2.6.0+cu124 Is debug build : False CUDA used to build PyTorch : 12.4 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
