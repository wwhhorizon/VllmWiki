# vllm-project/vllm#42873: [Bug]: Forked workers retain stale CUDA primary contexts from parent process

| 字段 | 值 |
| --- | --- |
| Issue | [#42873](https://github.com/vllm-project/vllm/issues/42873) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Forked workers retain stale CUDA primary contexts from parent process

### Issue 正文摘录

## Your current environment vLLM main (latest) and v0.8.5.post1, tested on H100 multi-GPU (tp=2). ## How would you like to use vllm I'm working on integrating NVIDIA's `cuda-checkpoint` tool with vLLM for near-zero cold starts (related to RFC #34303). During multi-GPU testing, I discovered that forked worker processes retain the parent's CUDA primary context for GPU 0, even when the worker is assigned to GPU 1. ## Before submitting a new issue... - [x] I have searched existing issues - [x] I have read the relevant documentation ## Describe the bug When vLLM uses the `fork` multiprocessing method (the default on Linux), child worker processes inherit the parent's active CUDA primary contexts for **all** devices. A worker assigned to GPU 1 ends up with **two** active primary contexts: GPU 0 (inherited from parent) and GPU 1 (its own). This causes two problems: 1. **Wasted GPU memory** - the stale GPU 0 context in the GPU 1 worker holds driver-level allocations that never get freed 2. **NVIDIA cuda-checkpoint failures** - `cuda-checkpoint --action restore` fails with "invalid argument" because it tries to restore both contexts in the worker process, but the GPU 0 context is stale and...

## 现有链接修复摘要

#42874 Release stale CUDA primary contexts inherited by forked workers

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Forked workers retain stale CUDA primary contexts from parent process ## Your current environment vLLM main (latest) and v0.8.5.post1, tested on H100 multi-GPU (tp=2). ## How would you like to use vllm I'm workin...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Reproduction ```python # In a forked worker process assigned to GPU 1: import ctypes, torch libcuda = ctypes.CDLL("libcuda.so.1") libcuda.cuInit(0) for dev_id in range(torch.cuda.device_count()): dev = ctypes.c_int() li...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: y contexts from parent process ## Your current environment vLLM main (latest) and v0.8.5.post1, tested on H100 multi-GPU (tp=2). ## How would you like to use vllm I'm working on integrating NVIDIA's `cuda-checkpoint` to...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: rom parent) and GPU 1 (its own). This causes two problems: 1. **Wasted GPU memory** - the stale GPU 0 context in the GPU 1 worker holds driver-level allocations that never get freed 2. **NVIDIA cuda-checkpoint failures*...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Forked workers retain stale CUDA primary contexts from parent process ## Your current environment vLLM main (latest) and v0.8.5.post1, tested on H100 multi-GPU (tp=2). ## How would you like to use vllm I'm workin...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42874](https://github.com/vllm-project/vllm/pull/42874) | closes_keyword | 0.95 | Release stale CUDA primary contexts inherited by forked workers | Fixes #42873 ## Context Discovered while integrating NVIDIA cuda-checkpoint with vLLM for multi-GPU cold start optimization (related to RFC #34303). The stale inherited contexts |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
