# vllm-project/vllm#25314: [Draft][RFC]: KVCache support nonuniform page size

| 字段 | 值 |
| --- | --- |
| Issue | [#25314](https://github.com/vllm-project/vllm/issues/25314) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Draft][RFC]: KVCache support nonuniform page size

### Issue 正文摘录

### Motivation. Currently, to ensure high utilization of the kv_cache in hybrid attention model scenarios, vLLM aligns the kv_cache block's page size across different layers and allows layers with different `kv_cache_spec` to use the same `kv_cache_tensor`. However, this approach prevents vLLM from supporting scenarios where kv_cache blocks of different layers use nonuniform page sizes, such as in cases where kv_cache quantization is applied to certain layers of a single attention model. ### Proposed Change. We would like to support the case when model has only single `kv_cache_spec` but with different page sizes from different layers. This will result in the following changes: 1. Add a branch in func `get_kv_cache_groups` to support the case with uniform `kv_cache_spec` and different page size, and the new branch only needs to modify the code of calculating `num_blocks` based on `available_memory`. ```python has_uniform_page_size = is_kv_cache_page_size_uniform(kv_cache_spec) if is_kv_cache_type_attention_free(kv_cache_spec): # This returns an empty list to allow for the KVCacheManager to handle # attention free models. return [] elif is_kv_cache_spec_uniform(kv_cache_spec): # KV...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: [Draft][RFC]: KVCache support nonuniform page size RFC ### Motivation. Currently, to ensure high utilization of the kv_cache in hybrid attention model scenarios, vLLM aligns the kv_cache block's page size across differe...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: of the kv_cache in hybrid attention model scenarios, vLLM aligns the kv_cache block's page size across different layers and allows layers with different `kv_cache_spec` to use the same `kv_cache_tensor`. However, this a...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ferent layers use nonuniform page sizes, such as in cases where kv_cache quantization is applied to certain layers of a single attention model. ### Proposed Change. We would like to support the case when model has only...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: urrently, to ensure high utilization of the kv_cache in hybrid attention model scenarios, vLLM aligns the kv_cache block's page size across different layers and allows layers with different `kv_cache_spec` to use the sa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
