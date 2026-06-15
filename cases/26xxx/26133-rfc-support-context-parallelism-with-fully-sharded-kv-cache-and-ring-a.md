# vllm-project/vllm#26133: [RFC]: Support Context Parallelism with Fully Sharded KV Cache and Ring Attention

| 字段 | 值 |
| --- | --- |
| Issue | [#26133](https://github.com/vllm-project/vllm/issues/26133) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Support Context Parallelism with Fully Sharded KV Cache and Ring Attention

### Issue 正文摘录

### Motivation. Context parallelism introduces an additional degree of parallelism to LLM inference. While tensor parallelism and pipeline parallelism focus on distributing model weights and layers across devices, context parallelism specifically targets the parallel processing of multiple input contexts or sequences. By combining context parallelism with parallelisms, systems can achieve more scalable and efficient inference, leveraging all forms of parallelism to maximize hardware utilization and reduce latency. Context parallelism improves performance as the context length grows by distributing both computation and the KV cache across multiple GPUs. This approach effectively lowers processing latency and can also decrease the memory required per GPU potentially, especially when dealing with extremely large KV caches (such as sequence lengths on the order of 1 million tokens). ### Proposed Change. Within the model, attention is the only component that has dependency on the sequence dimension, since each token must attend to all previous tokens in the same sequence. In contrast, FFN and element-wise operations are performed independently for each token. For a more in-depth unders...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: t Context Parallelism with Fully Sharded KV Cache and Ring Attention RFC;stale ### Motivation. Context parallelism introduces an additional degree of parallelism to LLM inference. While tensor parallelism and pipeline p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ributing model weights and layers across devices, context parallelism specifically targets the parallel processing of multiple input contexts or sequences. By combining context parallelism with parallelisms, systems can...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [RFC]: Support Context Parallelism with Fully Sharded KV Cache and Ring Attention RFC;stale ### Motivation. Context parallelism introduces an additional degree of parallelism to LLM inference. While tensor parallelism a...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [RFC]: Support Context Parallelism with Fully Sharded KV Cache and Ring Attention RFC;stale ### Motivation. Context parallelism introduces an additional degree of parallelism to LLM inference. While tensor parallelism a...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: The provided figure demonstrates the decoding process with cp=2. ## Block Table When tokens are distributed across context parallel (CP) ranks, gaps may appear in the block table. After compaction, tokens that are store...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
