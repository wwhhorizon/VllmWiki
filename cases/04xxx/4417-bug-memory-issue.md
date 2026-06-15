# vllm-project/vllm#4417: [Bug]: Memory Issue

| 字段 | 值 |
| --- | --- |
| Issue | [#4417](https://github.com/vllm-project/vllm/issues/4417) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Memory Issue

### Issue 正文摘录

### Your current environment ```text 8x RTX A6000 289.0 TFLOPS 383.9 GB GPU RAM ``` ### 🐛 Describe the bug I get error ```torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 1.50 GiB. GPU 0 has a total capacity of 47.54 GiB of which 1.38 GiB is free. Process 876965 has 46.14 GiB memory in use. Of the allocated memory 45.52 GiB is allocated by PyTorch, and 5.85 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation. See documentation for Memory Management (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)``` However, I have enough ram on all my gpus. I don't think vllm is using all the gpus.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: r: CUDA out of memory. Tried to allocate 1.50 GiB. GPU 0 has a total capacity of 47.54 GiB of which 1.38 GiB is free. Process 876965 has 46.14 GiB memory in use. Of the allocated memory 45.52 GiB is allocated by PyTorch...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Memory Issue bug ### Your current environment ```text 8x RTX A6000 289.0 TFLOPS 383.9 GB GPU RAM ``` ### 🐛 Describe the bug I get error ```torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 1.50 G...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: on't think vllm is using all the gpus. performance scheduler_memory cuda oom env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: am on all my gpus. I don't think vllm is using all the gpus. performance scheduler_memory cuda oom env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
