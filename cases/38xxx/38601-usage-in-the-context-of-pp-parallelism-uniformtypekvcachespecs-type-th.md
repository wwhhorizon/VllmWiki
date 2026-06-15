# vllm-project/vllm#38601: [Usage]: In the context of pp parallelism, UniformTypeKVCacheSpecs type, the calculation of page size considers all the layers， not only the layerss of one pp rank ?

| 字段 | 值 |
| --- | --- |
| Issue | [#38601](https://github.com/vllm-project/vllm/issues/38601) |
| 状态 | open |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: In the context of pp parallelism, UniformTypeKVCacheSpecs type, the calculation of page size considers all the layers， not only the layerss of one pp rank ?

### Issue 正文摘录

### Your current environment class UniformTypeKVCacheSpecs(KVCacheSpec): """ A KV cache spec for multiple layers with the same type of attention. Here, same types means always need the same number of token slots. For example, sliding window attentions with different window sizes are not the same type and should not be merged into one UniformTypeKVCacheSpecs. """ kv_cache_specs: dict[str, KVCacheSpec] @property def page_size_bytes(self) -> int: return sum(spec.page_size_bytes for spec in self.kv_cache_specs.values()) ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: text of pp parallelism, UniformTypeKVCacheSpecs type, the calculation of page size considers all the layers， not only the layerss of one pp rank ? usage ### Your current environment class UniformTypeKVCacheSpecs(KVCache...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: )) ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: In the context of pp parallelism, UniformTypeKVCacheSpecs type, the calculation of page size considers all the layers， not only the layerss of one pp rank ? usage ### Your current environment class UniformTypeK...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: t environment class UniformTypeKVCacheSpecs(KVCacheSpec): """ A KV cache spec for multiple layers with the same type of attention. Here, same types means always need the same number of token slots. For example, sliding...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for re...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
