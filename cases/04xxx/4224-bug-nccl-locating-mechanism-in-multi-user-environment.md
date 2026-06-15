# vllm-project/vllm#4224: [Bug]: NCCL locating mechanism in multi-user environment

| 字段 | 值 |
| --- | --- |
| Issue | [#4224](https://github.com/vllm-project/vllm/issues/4224) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: NCCL locating mechanism in multi-user environment

### Issue 正文摘录

### Your current environment - 18-node cluster running Ubuntu 20.04 LTS. - AMD Rome/Milan/Genoa CPUs. Mutliple GPUs on each node: A100/RTX 3090/RTX 3060. - Conda environment on shared NFS drive. vLLM 0.4.0.post1 + PyTorch 2.2 + CUDA 12.1 environment. - Job dispatched by Slurm. ### 🐛 Describe the bug It seems that vLLM's NCCL detection mechanism is written with single user in mind. The vLLM-managed NCCL .so file is only installed for the user who installed vLLM. [`find_nccl_library`](https://github.com/vllm-project/vllm/blob/e8cc7967ff8a6f8432747a9e87ab451d36e1ff57/vllm/utils.py#L545-L570) is written such that if `VLLM_NCCL_SO_PATH` is not specified nor is the vLLM-managed version of NCCL found, it defaults to a hard-coded NCCL filename `so_file`, then reports to the user "Found nccl from library {so_file}". I see two problems here: 1. [`find_nccl_library`] reports "Found nccl..." even when it has not. Perhaps it should say instead "Attempting to load nccl..."? 2. The vLLM-managed NCCL .so file is only installed to the home directory of the user who installed vLLM, meaning that it is inaccessible to other users. Why is it not installed along the package, which is accessible to all...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: NCCL locating mechanism in multi-user environment bug;stale ### Your current environment - 18-node cluster running Ubuntu 20.04 LTS. - AMD Rome/Milan/Genoa CPUs. Mutliple GPUs on each node: A100/RTX 3090/RTX 3060...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: written with single user in mind. The vLLM-managed NCCL .so file is only installed for the user who installed vLLM. [`find_nccl_library`](https://github.com/vllm-project/vllm/blob/e8cc7967ff8a6f8432747a9e87ab451d36e1ff5...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: NFS drive. vLLM 0.4.0.post1 + PyTorch 2.2 + CUDA 12.1 environment. - Job dispatched by Slurm. ### 🐛 Describe the bug It seems that vLLM's NCCL detection mechanism is written with single user in mind. The vLLM-managed NC...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: NCCL locating mechanism in multi-user environment bug;stale ### Your current environment - 18-node cluster running Ubuntu 20.04 LTS. - AMD Rome/Milan/Genoa CPUs. Mutliple GPUs on each node: A100/RTX 3090/RTX 3060...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
