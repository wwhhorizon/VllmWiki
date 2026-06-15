# vllm-project/vllm#751: LLama 2 70b 2 x H100s OOM Error

| 字段 | 值 |
| --- | --- |
| Issue | [#751](https://github.com/vllm-project/vllm/issues/751) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
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

> LLama 2 70b 2 x H100s OOM Error

### Issue 正文摘录

I am trying to infer llama 2 70 based [model](https://huggingface.co/stabilityai/StableBeluga2) using 2*H100s. But still gets an OOM error. ## Code ``` MODEL = "stabilityai/StableBeluga2" model = llm = LLM(model=MODEL,tensor_parallel_size=2) ``` ## Error trace ``` torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 448.00 MiB. GPU 0 has a total capacty of 79.11 GiB of which 391.12 MiB is free. Process 247516 has 50.52 GiB memory in use. Process 477367 has 28.19 GiB memory in use. Of the allocated memory 27.48 GiB is allocated by PyTorch, and 1.98 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting max_split_size_mb to avoid fragmentation. See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF ``` ## GPU

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: LLama 2 70b 2 x H100s OOM Error I am trying to infer llama 2 70 based [model](https://huggingface.co/stabilityai/StableBeluga2) using 2*H100s. But still gets an OOM error. ## Code ``` MODEL = "stabilityai/StableBeluga2
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: LLama 2 70b 2 x H100s OOM Error I am trying to infer llama 2 70 based [model](https://huggingface.co/stabilityai/StableBeluga2) using 2*H100s. But still gets an OOM error. ## Code ``` MODEL = "stabilityai/StableBeluga2"...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: CONF ``` ## GPU performance model_support;scheduler_memory cuda oom env_dependency I am trying to infer llama 2 70 based [model](https://huggingface.co/stabilityai/StableBeluga2) using 2*H100s. But still gets an OOM err...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: LLama 2 70b 2 x H100s OOM Error I am trying to infer llama 2 70 based [model](https://huggingface.co/stabilityai/StableBeluga2) using 2*H100s. But still gets an OOM error. ## Code ``` MODEL = "stabilityai/StableBeluga2"...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: gement and PYTORCH_CUDA_ALLOC_CONF ``` ## GPU performance model_support;scheduler_memory cuda oom env_dependency I am trying to infer llama 2 70 based [model](https://huggingface.co/stabilityai/StableBeluga2) using 2*H1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
