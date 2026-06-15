# vllm-project/vllm#2363: OutOfMemoryError

| 字段 | 值 |
| --- | --- |
| Issue | [#2363](https://github.com/vllm-project/vllm/issues/2363) |
| 状态 | closed |
| 标签 |  |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> OutOfMemoryError

### Issue 正文摘录

Hello! New(old) problem 🙂 torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 112.00 MiB. GPU 0 has a total capacty of 39.39 GiB of which 17.94 MiB is free. Including non-PyTorch memory, this process has 39.36 GiB memory in use. Of the allocated memory 38.72 GiB is allocated by PyTorch, and 12.91 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting max_split_size_mb to avoid fragmentation. See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF Command: python -m vllm.entrypoints.openai.api_server \ --model mistralai/Mixtral-8x7B-v0.1 Any tips?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: -v0.1 Any tips? performance model_support;scheduler_memory cuda oom env_dependency Hello! New(old) problem 🙂
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: OutOfMemoryError Hello! New(old) problem 🙂 torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 112.00 MiB. GPU 0 has a total capacty of 39.39 GiB of which 17.94 MiB is free. Including non-PyTorch memory,...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ral-8x7B-v0.1 Any tips? performance model_support;scheduler_memory cuda oom env_dependency Hello! New(old) problem 🙂
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: DA_ALLOC_CONF Command: python -m vllm.entrypoints.openai.api_server \ --model mistralai/Mixtral-8x7B-v0.1 Any tips? performance model_support;scheduler_memory cuda oom env_dependency Hello! New(old) problem 🙂
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: --model mistralai/Mixtral-8x7B-v0.1 Any tips? performance model_support;scheduler_memory cuda oom env_dependency Hello! New(old) problem 🙂

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
