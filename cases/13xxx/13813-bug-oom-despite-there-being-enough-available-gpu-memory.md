# vllm-project/vllm#13813: [Bug]: OOM despite there being enough available GPU memory

| 字段 | 值 |
| --- | --- |
| Issue | [#13813](https://github.com/vllm-project/vllm/issues/13813) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OOM despite there being enough available GPU memory

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When attempting to run vllm I encounter a nonsensical OOM error. The error is nonsensical because the amount of memory that torch is trying to allocate is significantly less than the available amount. The following minimal code snippet is sufficient to induce the behaviour. ``` from vllm import LLM llm = LLM(model="facebook/opt-125m") ``` The following is indicative of the errors I obtain: ``` torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 1.74 GiB. GPU 0 has a total capacity of 23.99 GiB of which 5.05 GiB is free. Including non-PyTorch memory, this process has 17179869184.00 GiB memory in use. Of the allocated memory 17.60 GiB is allocated by PyTorch, and 34.80 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation. See documentation for Memory Management (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables) ``` As you can see, 5.05 > 1.74, but I get an OOM anyway. Some insight into why this is occurring would be very much appreciated. ### Before submitting a new issue... - [x] Mak...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ss than the available amount. The following minimal code snippet is sufficient to induce the behaviour. ``` from vllm import LLM llm = LLM(model="facebook/opt-125m") ``` The following is indicative of the errors I obtai...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: wing is indicative of the errors I obtain: ``` torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 1.74 GiB. GPU 0 has a total capacity of 23.99 GiB of which 5.05 GiB is free. Including non-PyTorch memory, thi...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: OOM despite there being enough available GPU memory bug ### Your current environment ### 🐛 Describe the bug When attempting to run vllm I encounter a nonsensical OOM error. The error is nonsensical because the am...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: uild;distributed_parallel;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf;oom env_dependency Your current environment
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;scheduler_memory;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf;oom env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
