# vllm-project/vllm#5751: [RFC]: Support sparse KV cache framework

| 字段 | 值 |
| --- | --- |
| Issue | [#5751](https://github.com/vllm-project/vllm/issues/5751) |
| 状态 | open |
| 标签 | RFC;keep-open |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Support sparse KV cache framework

### Issue 正文摘录

### Motivation For current large model inference, KV cache occupies a significant portion of GPU memory, so reducing the size of KV cache is an important direction for improvement. Recently, several papers have approached this issue from different angles, detailed comparison in the table, including: - FastDecode: This method offloads all computation of KV cache to the CPU. The computation and storage of KV cache occurs on CPU. - Compression methods based on quantization (GEAR, Mixed Precision): By applying various quantization techniques, the size of individual token KV caches is reduced without decreasing the number of tokens stored in the KV cache. This method may also result in corresponding residual and outlier matrices, which need to be stored in memory but not in the KV cache. It may also involve quantizing unimportant token KV caches to reduce the memory footprint of the KV cache. - Partial KV cache eviction (H2O, SnapKV, LESS, Adaptive Compression, Scissorhands, Dynamic Memory Compression, StreamingLLM): By removing some relatively useless KV cache entries, the memory footprint of the KV cache is reduced. Essentially, this reduces the number of tokens stored in the KV cach...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 6: [RFC]: Support sparse KV cache framework RFC;keep-open ### Motivation For current large model inference, KV cache occupies a significant portion of GPU memory, so reducing the size of KV cache is an important direction...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: inference, KV cache occupies a significant portion of GPU memory, so reducing the size of KV cache is an important direction for improvement. Recently, several papers have approached this issue from different angles, de...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ssary, based on the priority ranking of tokens, one or more new KV cache blocks will be allocated, modifying the position information of input positions. The block manager will then manage the transfer of corresponding...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: parse KV cache framework RFC;keep-open ### Motivation For current large model inference, KV cache occupies a significant portion of GPU memory, so reducing the size of KV cache is an important direction for improvement....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: om different angles, detailed comparison in the table, including: - FastDecode: This method offloads all computation of KV cache to the CPU. The computation and storage of KV cache occurs on CPU. - Compression methods b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
