# vllm-project/vllm#1359: Qwen-7B-Chat  vllm failed

| 字段 | 值 |
| --- | --- |
| Issue | [#1359](https://github.com/vllm-project/vllm/issues/1359) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Qwen-7B-Chat  vllm failed

### Issue 正文摘录

torch.distributed.DistBackendError: NCCL error in: ../torch/csrc/distributed/c10d/NCCLUtils.hpp:121, unhandled cuda error (run with NCCL_DEBUG=INFO for details), NCCL version 2.18.1 ncclUnhandledCudaError: Call to CUDA function failed. Last error: Cuda failure 'CUDA driver version is insufficient for CUDA runtime version'

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: p:121, unhandled cuda error (run with NCCL_DEBUG=INFO for details), NCCL version 2.18.1 ncclUnhandledCudaError: Call to CUDA function failed. Last error: Cuda failure 'CUDA driver version is insufficient for CUDA runtim...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: Qwen-7B-Chat vllm failed torch.distributed.DistBackendError: NCCL error in: ../torch/csrc/distributed/c10d/NCCLUtils.hpp:121, unhandled cuda error (run with NCCL_DEBUG=INFO for details), NCCL version 2.18.1 ncclUnhandle...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: CL error in: ../torch/csrc/distributed/c10d/NCCLUtils.hpp:121, unhandled cuda error (run with NCCL_DEBUG=INFO for details), NCCL version 2.18.1 ncclUnhandledCudaError: Call to CUDA function failed. Last error: Cuda fail...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Qwen-7B-Chat vllm failed torch.distributed.DistBackendError: NCCL error in: ../torch/csrc/distributed/c10d/NCCLUtils.hpp:121, unhandled cuda error (run with NCCL_DEBUG=INFO for details), NCCL version 2.18.1 ncclUnhandle

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
