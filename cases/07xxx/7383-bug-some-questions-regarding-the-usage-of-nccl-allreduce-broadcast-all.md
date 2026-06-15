# vllm-project/vllm#7383: [Bug]:  some questions regarding the usage of NCCL allreduce/broadcast/allgather/send/recv in VLLM using pycomm and torch's distributed.

| 字段 | 值 |
| --- | --- |
| Issue | [#7383](https://github.com/vllm-project/vllm/issues/7383) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  some questions regarding the usage of NCCL allreduce/broadcast/allgather/send/recv in VLLM using pycomm and torch's distributed.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hello VLLM expert, While reading the VLLM code, I noticed that the `pynccl.py` file only wraps `allreduce`, `send/recv`, and does not wrap the `allgather` and `broadcast` operations. When the `class GroupCoordinator` calls `allreduce`, `send/recv`, it attempts to call the `pynccl` comm's `allreduce`, `send/recv` (if `pynccl`'s `disable` is false; does this only take effect during CUDA graph capture?). However, when calling `allgather` and `broadcast` operations, it directly calls `torch.distributed.broadcast` and `torch.distributed.allgather`. From reading this code, I have the following three questions: 1. Why does `pynccl` not wrap `allgather` and `broadcast`? Is there a specific consideration behind this? Are the `nccl_comm` in `pynccl` and the `nccl_comm` in `torch.distributed` the same? 2. When is `pynccl` called? From the code, it seems that `pynccl` comm can only be called when using CUDA graphs. Please confirm this. Additionally, if we completely use PyTorch's operations during CUDA graph capture, is that not feasible? Why do we need to wrap an additional `pynccl` comm? 3. If a model has `allreduce`, `broadcast`, `allgath...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 1. Why does `pynccl` not wrap `allgather` and `broadcast`? Is there a specific consideration behind this? Are the `nccl_comm` in `pynccl` and the `nccl_comm` in `torch.distributed` the same? 2. When is `pynccl` called?...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: cv` (if `pynccl`'s `disable` is false; does this only take effect during CUDA graph capture?). However, when calling `allgather` and `broadcast` operations, it directly calls `torch.distributed.broadcast` and `torch.dis...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: e `pynccl` comm's `allreduce`, `send/recv` (if `pynccl`'s `disable` is false; does this only take effect during CUDA graph capture?). However, when calling `allgather` and `broadcast` operations, it directly calls `torc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: t feasible? Why do we need to wrap an additional `pynccl` comm? 3. If a model has `allreduce`, `broadcast`, `allgather`, `send/recv`, then during CUDA graph capture, it effectively uses NCCL operations from two differen...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: bug ### Your current environment ### 🐛 Describe the bug Hello VLLM expert, While reading the VLLM code, I noticed that the `pynccl.py` file only wraps `allreduce`, `send/recv`, and does not wrap the `allgather` and `bro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
