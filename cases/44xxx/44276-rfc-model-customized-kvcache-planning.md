# vllm-project/vllm#44276: [RFC]: Model customized KVCache Planning

| 字段 | 值 |
| --- | --- |
| Issue | [#44276](https://github.com/vllm-project/vllm/issues/44276) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Model customized KVCache Planning

### Issue 正文摘录

### Motivation. ### Current KVCache planning Currently all the KVCache planning strategies are covered by the `kv_cache_utils.py`. It is treated as a global feature for each model. The core steps including: - merge the kv cache specs from each worker - group the kv cache specs - maybe override num_blocks - auto-fix max model len - create `KVCacheTensor` and then `KVCacheConfig` according to the group The most important but also heavy work is grouping the kv cache specs. There’re 5 branches in the general scenarios: number of kvcache | grouping method | number of groups -- | -- | -- / | use unified kv cache specs | 1 0 | no grouping | 0 1 | uniform kv cache specs | 1 usually 2 (sizes differ between layers) | uniform type kv cache specs | 1 usually 2 (types and sizes differ) | hybrid kv cache grouping: align the page size between different type of specs; determine a group size for sharing the same buffer; group the kv cache specs by `KVCacheGroupSepcs` | num_layers/group_size With the hybrid attention models growing, HMA plays an important role in kv cahce planning. Taking advantage of HMA, when the attention types in the model are within 2, we could handle it with a uniform logic....

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [RFC]: Model customized KVCache Planning RFC ### Motivation. ### Current KVCache planning Currently all the KVCache planning strategies are covered by the `kv_cache_utils.py`. It is treated as a global feature for each...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: KVCacheTensor` and then `KVCacheConfig` according to the group The most important but also heavy work is grouping the kv cache specs. There’re 5 branches in the general scenarios: number of kvcache | grouping method | n...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: e specs from each worker - group the kv cache specs - maybe override num_blocks - auto-fix max model len - create `KVCacheTensor` and then `KVCacheConfig` according to the group The most important but also heavy work is...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 24-deepseek-v4) It is a huge challenge to use a uniform grouping mechanism and make great use of memory, thus vLLM offers a specific way for DeepSeek-V4 for a more effective kvcache planning. And the main differences: -...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: methods. - `get_kv_cache_groups`: keep this api as we need this in when profiling cudagraph mem in `_init_minimal_kv_cache_for_profiling` - `get_kv_cache_configs_from_groups`: ditto - `get_kv_cache_configs`: this is at...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
