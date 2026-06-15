# vllm-project/vllm#5434: [Feature]: PagedAttention for CPU-memory constraned environments?

| 字段 | 值 |
| --- | --- |
| Issue | [#5434](https://github.com/vllm-project/vllm/issues/5434) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: PagedAttention for CPU-memory constraned environments?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I was wondering if it were possible to implement PagedAttention in an environment where the model params won't fit in CPU memory. As I understand from the original paper (and a cursory read of the source), the engine swaps relevant blocks from the CPU memory to the GPU memory. In a resource constrained environment, I'm imaging we "replace" the GPU memory with the CPU memory (ram) and the CPU memory with disk/flash storage. What would it take to extend vLLM for something like this? ### Alternatives Not sure if any alternatives exist. But there are some related techniques (published and otherwise) * [PowerInfer](https://arxiv.org/abs/2312.12456) * [LLM in a Flash](https://arxiv.org/abs/2312.11514) ### Additional context (I'd like to take a stab at implementing this.)

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Feature]: PagedAttention for CPU-memory constraned environments? feature request;stale ### 🚀 The feature, motivation and pitch I was wondering if it were possible to implement PagedAttention in an environment where the...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: the source), the engine swaps relevant blocks from the CPU memory to the GPU memory. In a resource constrained environment, I'm imaging we "replace" the GPU memory with the CPU memory (ram) and the CPU memory with disk/...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: inal paper (and a cursory read of the source), the engine swaps relevant blocks from the CPU memory to the GPU memory. In a resource constrained environment, I'm imaging we "replace" the GPU memory with the CPU memory (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: it were possible to implement PagedAttention in an environment where the model params won't fit in CPU memory. As I understand from the original paper (and a cursory read of the source), the engine swaps relevant blocks...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
