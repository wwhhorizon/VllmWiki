# vllm-project/vllm#24971: [Bug]: Donut model inference, CUDA out of memory

| 字段 | 值 |
| --- | --- |
| Issue | [#24971](https://github.com/vllm-project/vllm/issues/24971) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 36; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;operator |
| 症状 | oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Donut model inference, CUDA out of memory

### Issue 正文摘录

### 🐛 Describe the bug I have tried to deploy donut model with vllm==v0.10.2 but I face memory error on gpu, while the model is quite small ( Command : vllm serve naver-clova-ix/donut-base-finetuned-docvqa --served-model-name naver-clova-ix--donut-base-finetuned-docvqa --hf_overrides '{"architectures": ["DonutForConditionalGeneration"]}' ```text torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 56.25 GiB. GPU 0 has a total capacity of 79.33 GiB of which 15.06 GiB is free. Process 58550 has 64.26 GiB memory in use. Of the allocated memory 63.77 GiB is allocated by PyTorch, and 8.42 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation. See documentation for Memory Management (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables) [rank0]:[W916 17:41:16.152602779 ProcessGroupNCCL.cpp:1538] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator())` ``` ### Before submitting a new issue... -...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Donut model inference, CUDA out of memory bug;stale ### 🐛 Describe the bug I have tried to deploy donut model with vllm==v0.10.2 but I face memory error on gpu, while the model is quite small ( Command : vllm ser...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: : CUDA out of memory. Tried to allocate 56.25 GiB. GPU 0 has a total capacity of 79.33 GiB of which 15.06 GiB is free. Process 58550 has 64.26 GiB memory in use. Of the allocated memory 63.77 GiB is allocated by PyTorch...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Donut model inference, CUDA out of memory bug;stale ### 🐛 Describe the bug I have tried to deploy donut model with vllm==v0.10.2 but I face memory error on gpu, while the model is quite small ( Command : vllm ser...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Donut model inference, CUDA out of memory bug;stale ### 🐛 Describe the bug I have tried to deploy donut model with vllm==v0.10.2 but I face memory error on gpu, while the model is quite small ( Command : vllm ser...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: rmance distributed_parallel;model_support;scheduler_memory cuda;operator oom env_dependency 🐛 Describe the bug

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
