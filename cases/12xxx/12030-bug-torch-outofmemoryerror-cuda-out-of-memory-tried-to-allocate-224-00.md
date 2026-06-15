# vllm-project/vllm#12030: [Bug]: torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 224.00 MiB. GPU 0 has a total capacity of 11.53 GiB of which 187.75 MiB is free. Including non-PyTorch memory, this process has 11.34 GiB memory in use.

| 字段 | 值 |
| --- | --- |
| Issue | [#12030](https://github.com/vllm-project/vllm/issues/12030) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 224.00 MiB. GPU 0 has a total capacity of 11.53 GiB of which 187.75 MiB is free. Including non-PyTorch memory, this process has 11.34 GiB memory in use.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hi. I tried to follow https://docs.vllm.ai/en/stable/serving/openai_compatible_server.html to start my vLLM server. With: "vllm serve NousResearch/Meta-Llama-3-8B-Instruct --dtype auto --api-key token-abc123" I obtain the errors: `ERROR 01-14 08:35:50 engine.py:366] return func(*args, **kwargs) ERROR 01-14 08:35:50 engine.py:366] ^^^^^^^^^^^^^^^^^^^^^ ERROR 01-14 08:35:50 engine.py:366] torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 224.00 MiB. GPU 0 has a total capacity of 11.53 GiB of which 187.75 MiB is free. Including non-PyTorch memory, this process has 11.34 GiB memory in use. Of the allocated memory 11.22 GiB is allocated by PyTorch, and 19.61 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation. See documentation for Memory Management (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables) Process SpawnProcess-1: Traceback (most recent call last): File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap self.run() ` I...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: CUDA out of memory. Tried to allocate 224.00 MiB. GPU 0 has a total capacity of 11.53 GiB of which 187.75 MiB is free. Including non-PyTorch memory, this process has 11.34 GiB memory in use. bug;stale ### Your current e...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: luding non-PyTorch memory, this process has 11.34 GiB memory in use. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hi. I tried to follow https://docs.vllm.ai/en/stable...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 224.00 MiB. GPU 0 has a total capacity of 11.53 GiB of which 187.75 MiB is free. Including non-PyTorch memory, this process has 11.34 GiB memory in us...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 11.34 GiB memory in use. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hi. I tried to follow https://docs.vllm.ai/en/stable/serving/openai_compatible_server.html to st...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;scheduler_memory;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf;oom dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
