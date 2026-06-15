# vllm-project/vllm#21772: [RFC]: Support KV Cache sparse with common framework

| 字段 | 值 |
| --- | --- |
| Issue | [#21772](https://github.com/vllm-project/vllm/issues/21772) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Support KV Cache sparse with common framework

### Issue 正文摘录

### Motivation. With the increase of model size, the KV cache became larger and sparser, especially for long sequence requests. To reduce the GPU memory used, offload full KV to external storage and only keep partial or compressed KV in GPU memory became the popular direction. This can also reduce the GPU calculation, increase the sequence length and batch size of decoding. Sparse KV cache have many different choices. Recently paper point out that there is no common way can fit all scenarios and all models. So better to build a common framework then different sparse algorithms can be plugin to it like KV connector for PC. ### Proposed Change. All gray boxes are current classes in 0.9.2. Green boxes are proposed to add. Light green ones show out the future sub classes base on this framework. SpareKVBase is the base class of different algorithms. Just like KV connector design, it will hook few places of scheduler and layer.py to allow sparse algorithms do additional load, dump and calculate sparse KV blocks. SparseKVManager provide different KV block allocation methods for different algorithms. To keep all implementation under SpareKVBase, it will call SparseKVBase and real implemen...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: [RFC]: Support KV Cache sparse with common framework RFC;stale ### Motivation. With the increase of model size, the KV cache became larger and sparser, especially for long sequence requests. To reduce the GPU memory use...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC]: Support KV Cache sparse with common framework RFC;stale ### Motivation. With the increase of model size, the KV cache became larger and sparser, especially for long sequence requests. To reduce the GPU memory use...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: the increase of model size, the KV cache became larger and sparser, especially for long sequence requests. To reduce the GPU memory used, offload full KV to external storage and only keep partial or compressed KV in GPU...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: allow sparse algorithms do additional load, dump and calculate sparse KV blocks. SparseKVManager provide different KV block allocation methods for different algorithms. To keep all implementation under SpareKVBase, it w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
