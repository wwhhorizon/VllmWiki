# vllm-project/vllm#372: [MPT-30B] OutOfMemoryError: CUDA out of memory

| 字段 | 值 |
| --- | --- |
| Issue | [#372](https://github.com/vllm-project/vllm/issues/372) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [MPT-30B] OutOfMemoryError: CUDA out of memory

### Issue 正文摘录

Hi vllm dev team, is vllm supposed to work with MPT-30B ? I tried loading it on AWS SageMaker using a `ml.g5.12xlarge` and even a `ml.g5.48xlarge` instance. ```py from vllm import LLM, SamplingParams llm = LLM(model="mosaicml/mpt-30b") ``` However in both cases I run into this error: ``` OutOfMemoryError: CUDA out of memory. Tried to allocate 294.00 MiB (GPU 0; 22.19 GiB total capacity; 21.35 GiB already allocated; 46.50 MiB free; 21.35 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation. See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: `ml.g5.12xlarge` and even a `ml.g5.48xlarge` instance. ```py from vllm import LLM, SamplingParams llm = LLM(model="mosaicml/mpt-30b") ``` However in both cases I run into this error: ``` OutOfMemoryError: CUDA out of me...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [MPT-30B] OutOfMemoryError: CUDA out of memory bug Hi vllm dev team, is vllm supposed to work with MPT-30B ? I tried loading it on AWS SageMaker using a `ml.g5.12xlarge` and even a `ml.g5.48xlarge` instance. ```py from...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ORCH_CUDA_ALLOC_CONF ``` performance model_support;scheduler_memory cuda oom Hi vllm dev team,
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: xlarge` instance. ```py from vllm import LLM, SamplingParams llm = LLM(model="mosaicml/mpt-30b") ``` However in both cases I run into this error: ``` OutOfMemoryError: CUDA out of memory. Tried to allocate 294.00 MiB (G...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ory Management and PYTORCH_CUDA_ALLOC_CONF ``` performance model_support;scheduler_memory cuda oom Hi vllm dev team,

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
