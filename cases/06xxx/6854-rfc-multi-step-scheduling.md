# vllm-project/vllm#6854: [RFC]: Multi-Step Scheduling

| 字段 | 值 |
| --- | --- |
| Issue | [#6854](https://github.com/vllm-project/vllm/issues/6854) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;kernel;sampling |
| 症状 | slowdown |
| 根因提示 | env_dependency;memory_layout;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Multi-Step Scheduling

### Issue 正文摘录

### Motivation. TLDR; There is high CPU overhead associated with each decode batch due to the processing and generation of input/output. Multi-step decoding will be able to amortize all these overheads over n-steps at a time. - Transfer of the sampled token from GPU to CPU for de-tokenization and response to client - Generation of output for user - Pythonization of tensors into python objects - CPU preparation and generation of next step’s input metadata - vLLM scheduler Result is that GPU is often idle, waiting for CPU operations (5-13ms of GPU bubble) Multi-step is when multiple decode passes are performed before performing a GPU-CPU sync in order to invoke vLLM scheduler and process sampled tokens. Currently the GPU->CPU memory transfer for sampled tokens is also synchronous with each decode step causing bubbles on the GPU. With multi-step, this memory transfer can happen in a separate CUDA stream and is essentially free as the CPU runs ahead of GPU. **See below for the source of performance improvement.** - Both screenshots are about 200ms in duration. Top row is the CUDA kernels and bottom contains the python trace. - Each highlighted redbox is about 4ms of GPU bubble for bot...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 9: [RFC]: Multi-Step Scheduling RFC;stale ### Motivation. TLDR; There is high CPU overhead associated with each decode batch due to the processing and generation of input/output. Multi-step decoding will be able to amortiz...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: nto python objects - CPU preparation and generation of next step’s input metadata - vLLM scheduler Result is that GPU is often idle, waiting for CPU operations (5-13ms of GPU bubble) Multi-step is when multiple decode p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: eline (Req/s) | MS-8 (Req/s) | MS-16 (Req/s) -- | -- | -- | -- A10G 8B Llama | 5.20 | 5.89 | - H100 8B Llama | 20.66 | 40.06 | 43.31 H100 30B Llama | 9.23 | 13.09 | 13.23 ### Proposed Change. Extend `ExecuteModelRequest...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: heduling RFC;stale ### Motivation. TLDR; There is high CPU overhead associated with each decode batch due to the processing and generation of input/output. Multi-step decoding will be able to amortize all these overhead...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: the GPU. With multi-step, this memory transfer can happen in a separate CUDA stream and is essentially free as the CPU runs ahead of GPU. **See below for the source of performance improvement.** - Both screenshots are a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
