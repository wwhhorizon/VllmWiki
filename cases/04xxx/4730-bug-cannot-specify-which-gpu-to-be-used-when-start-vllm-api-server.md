# vllm-project/vllm#4730: [Bug]: cannot specify which gpu to be used when start vllm api server 

| 字段 | 值 |
| --- | --- |
| Issue | [#4730](https://github.com/vllm-project/vllm/issues/4730) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: cannot specify which gpu to be used when start vllm api server 

### Issue 正文摘录

### Your current environment ```text vllm ==0.3.3 ``` ### 🐛 Describe the bug On a 800 * 8 gpu server gpu 0,1,2 were occupied I tried to run vllm api server on gpu 6 using following: ``` export CUDA_VISIBLE_DEVICES=6 python -m vllm.entrypoints.openai.api_server --model /gpu/nfs/raymodel/qwen/Qwen1.5-72B-Chat ``` and got error message: ``` torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 768.00 MiB. GPU 0 has a total capacty of 79.32 GiB of which 519.56 MiB is free. Process 1903743 has 50.95 GiB memory in use. Including non-PyTorch memory, this process has 27.85 GiB memory in use. Of the allocated memory 27.20 GiB is allocated by PyTorch, and 12.78 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting max_split_size_mb to avoid fragmentation. See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF ``` api server was still trying allocate model in gpu 0

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: cannot specify which gpu to be used when start vllm api server bug ### Your current environment ```text vllm ==0.3.3 ``` ### 🐛 Describe the bug On a 800 * 8 gpu server gpu 0,1,2 were occupied I tried to run vllm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rt CUDA_VISIBLE_DEVICES=6 python -m vllm.entrypoints.openai.api_server --model /gpu/nfs/raymodel/qwen/Qwen1.5-72B-Chat ``` and got error message: ``` torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 76...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed I tried to run vllm api server on gpu 6 using following: ``` export CUDA_VISIBLE_DEVICES=6 python -m vllm.entrypoints.openai.api_server --model /gpu/nfs/raymodel/qwen/Qwen1.5-72B-Chat ``` and got error message: ``` t...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: el in gpu 0 performance frontend_api;model_support;scheduler_memory cuda oom env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ll trying allocate model in gpu 0 performance frontend_api;model_support;scheduler_memory cuda oom env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
