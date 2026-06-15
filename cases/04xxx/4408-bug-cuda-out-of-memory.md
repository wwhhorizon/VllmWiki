# vllm-project/vllm#4408: [Bug]: CUDA out of memory

| 字段 | 值 |
| --- | --- |
| Issue | [#4408](https://github.com/vllm-project/vllm/issues/4408) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA out of memory

### Issue 正文摘录

### Your current environment ```text A100 80GB ``` ### 🐛 Describe the bug Command: ```python3 -m vllm.entrypoints.openai.api_server --model alpindale/WizardLM-2-8x22B --dtype auto --max-model-len 8192 --gpu-memory-utilization 0.50 --enforce-eager --api-key token-abc123``` Error: ``` return func(*args, **kwargs) torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 1.50 GiB. GPU 0 has a total capacity of 79.15 GiB of which 147.75 MiB is free. Process 483452 has 78.98 GiB memory in use. Of the allocated memory 78.17 GiB is allocated by PyTorch, and 13.03 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation. See documentation for Memory Management (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables) ``` I get the same error for other models too, and I do not think gpu-memory-utilization does anything.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: r: CUDA out of memory. Tried to allocate 1.50 GiB. GPU 0 has a total capacity of 79.15 GiB of which 147.75 MiB is free. Process 483452 has 78.98 GiB memory in use. Of the allocated memory 78.17 GiB is allocated by PyTor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: CUDA out of memory bug ### Your current environment ```text A100 80GB ``` ### 🐛 Describe the bug Command: ```python3 -m vllm.entrypoints.openai.api_server --model alpindale/WizardLM-2-8x22B --dtype auto --max-mod...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: vllm.entrypoints.openai.api_server --model alpindale/WizardLM-2-8x22B --dtype auto --max-model-len 8192 --gpu-memory-utilization 0.50 --enforce-eager --api-key token-abc123``` Error: ``` return func(*args, **kwargs) tor...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: s anything. performance frontend_api;model_support;scheduler_memory cuda oom dtype;env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ibe the bug Command: ```python3 -m vllm.entrypoints.openai.api_server --model alpindale/WizardLM-2-8x22B --dtype auto --max-model-len 8192 --gpu-memory-utilization 0.50 --enforce-eager --api-key token-abc123``` Error: `...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
