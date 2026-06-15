# vllm-project/vllm#36668: [RFC]: Support Registry Mechanism for KVCacheSpec

| 字段 | 值 |
| --- | --- |
| Issue | [#36668](https://github.com/vllm-project/vllm/issues/36668) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Support Registry Mechanism for KVCacheSpec

### Issue 正文摘录

### Motivation. 1. Currently the `KVCacheSpec` is not very decoupling, when adding a new type of `KVCacheSpec`, we need to do the following things: - implement a subclass of `KVCacheSpec`. - implement a `SingleTypeKVCacheManager` for the `KVCacheSpec` or specify an existed `SingleTypeKVCacheManager` for it. - map the `KVCacheSpec` and `SingleTypeKVCacheManager` in `spec_manager_map` - add a new branch for it in `UniformTypeKVCacheSpecs.is_uniform_type` 2. Different alignment sizes or some hardware-customed pads are required by different hardware backends. For example: - page_size_padded is introduced to ensure compatibility of TPU/RPA in https://github.com/vllm-project/vllm/pull/31635. - GPU need to align with 256 for performance https://github.com/vllm-project/vllm/pull/36359 - vLLM-Ascend requires a page size larger than that of MLAAttentionSpec but smaller than that of FullAttentionSpec for deepseek v3.2, but it could only choose the later to make it functionally work. The tight coupling makes it impossible for out-of-tree platforms to extend KV cache behavior without patching vLLM, which is not a long-term solution for evolution. ### Proposed Change. please read the details in...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: stomed pads are required by different hardware backends. For example: - page_size_padded is introduced to ensure compatibility of TPU/RPA in https://github.com/vllm-project/vllm/pull/31635. - GPU need to align with 256...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: o change the pad or the calculation of page_size when enabling different quantization methods, e.g., fp8_ds_mla in `MLAAttentionSpec`. In this case, we don’t need to change the definition of `KVCacheSpec` in layers, but...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [RFC]: Support Registry Mechanism for KVCacheSpec RFC ### Motivation. 1. Currently the `KVCacheSpec` is not very decoupling, when adding a new type of `KVCacheSpec`, we need to do the following things: - implement a sub...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sizes or some hardware-customed pads are required by different hardware backends. For example: - page_size_padded is introduced to ensure compatibility of TPU/RPA in https://github.com/vllm-project/vllm/pull/31635. - GP...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: c`. - implement a `SingleTypeKVCacheManager` for the `KVCacheSpec` or specify an existed `SingleTypeKVCacheManager` for it. - map the `KVCacheSpec` and `SingleTypeKVCacheManager` in `spec_manager_map` - add a new branch...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
