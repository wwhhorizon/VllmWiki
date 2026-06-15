# vllm-project/vllm#27479: [Bug]: Low GPU utilization with Embedding Model

| 字段 | 值 |
| --- | --- |
| Issue | [#27479](https://github.com/vllm-project/vllm/issues/27479) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Low GPU utilization with Embedding Model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Initializing LLM(model="Qwen/Qwen3-Embedding-0.6B", task="embed") on a single B200 (180 GB) immediately reserves ~80% GPU memory (likely PagedAttention KV block pre-allocation). During embedding, GPU-Util stays 80% utilization and memory use on the same box. Is heavy KV Cache pre-allocation expected for task="embed" (prefill-only)? And is there any method to improve the GPU-Util? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: alizing LLM(model="Qwen/Qwen3-Embedding-0.6B", task="embed") on a single B200 (180 GB) immediately reserves ~80% GPU memory (likely PagedAttention KV block pre-allocation). During embedding, GPU-Util stays 80% utilizati...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: 0.6B", task="embed") on a single B200 (180 GB) immediately reserves ~80% GPU memory (likely PagedAttention KV block pre-allocation). During embedding, GPU-Util stays 80% utilization and memory use on the same box. Is he...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Low GPU utilization with Embedding Model bug;stale ### Your current environment ### 🐛 Describe the bug Initializing LLM(model="Qwen/Qwen3-Embedding-0.6B", task="embed") on a single B200 (180 GB) immediately reser...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Low GPU utilization with Embedding Model bug;stale ### Your current environment ### 🐛 Describe the bug Initializing LLM(model="Qwen/Qwen3-Embedding-0.6B", task="embed") on a single B200 (180 GB) immediately reser...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: (180 GB) immediately reserves ~80% GPU memory (likely PagedAttention KV block pre-allocation). During embedding, GPU-Util stays 80% utilization and memory use on the same box. Is heavy KV Cache pre-allocation expected f...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
