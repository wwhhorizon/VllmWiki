# vllm-project/vllm#10646: [RFC]: Support KV Cache Compaction

| 字段 | 值 |
| --- | --- |
| Issue | [#10646](https://github.com/vllm-project/vllm/issues/10646) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Support KV Cache Compaction

### Issue 正文摘录

### Motivation. KV cache compaction (i.e., token dropping) can significantly reduce memory footprint in llm serving (especially for long generation and large batch size workloads). The plan is to support the latest KV compaction methods, such as [FastGen](https://arxiv.org/pdf/2310.01801) and [DuoAttetnion](https://https://arxiv.org/abs/2410.10819), and also support a flexible interface for developers to add their own compaction methods. ### Proposed Change. To support KV Cache compaction, we need: 1. Expose intermediate logits (i.e. attetnion weights) from attention kernels as a lot of token dropping decisions depend on attention weights. 2. Support `free_and_reallocate` functionality to reduce memory fragmentation after memory compaction. A workaround is to use `block_size=1`. 3. Support non-uniform memory layout. Currently, vllm assumes kv cache across different heads and layers have the same layout. However, some compaction methods require dropping different tokens (i.e., their KV cache) at different heads and layers. A prototype is available at https://github.com/LMCache/LMCache/blob/compaction/examples/compactor/README.md . Feel free to share any thoughts and comments!! ###...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: e memory fragmentation after memory compaction. A workaround is to use `block_size=1`. 3. Support non-uniform memory layout. Currently, vllm assumes kv cache across different heads and layers have the same layout. Howev...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: dropping) can significantly reduce memory footprint in llm serving (especially for long generation and large batch size workloads). The plan is to support the latest KV compaction methods, such as [FastGen](https://arxi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [RFC]: Support KV Cache Compaction RFC;stale ### Motivation. KV cache compaction (i.e., token dropping) can significantly reduce memory footprint in llm serving (especially for long generation and large batch size workl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [RFC]: Support KV Cache Compaction RFC;stale ### Motivation. KV cache compaction (i.e., token dropping) can significantly reduce memory footprint in llm serving (especially for long generation and large batch size workl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
