# vllm-project/vllm#20626: [RFC]: Hotness-aware multi-level KV cache management to accelerate dynamic sparse attention

| 字段 | 值 |
| --- | --- |
| Issue | [#20626](https://github.com/vllm-project/vllm/issues/20626) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Hotness-aware multi-level KV cache management to accelerate dynamic sparse attention

### Issue 正文摘录

### Motivation. **Background:** Long-context reasoning scenarios face a dual surge in computational overhead and memory consumption, resulting in low inference efficiency and high inference costs. Dynamic sparse attention mitigates the computational surge in long sequences, but the memory bottleneck remains. Under sparse attention, accesses to the KV cache exhibit a hot-cold distribution, presenting an opportunity for heterogeneous KV cache management. * Heterogeneous KV cache leverages cheap, scalable main memory to replace expensive, limited device memory, promising significant reductions in inference costs. * By retaining frequently accessed KV cache in device memory and swapping out infrequently accessed KV cache to main memory, the memory footprint of long sequences can be reduced. **Goals:** - To accelerate the long sequence decoding and gurantee the accuracy, we plan implementing a hotness-ware multi-level kv cache management mechanism while keeping the sparse attention arithemetic computation unchanged, - To achive good precision, different from KV compression and KV dropping methods (issue5751, issue 12254, and pr 11938), this implementation chooses keeping the whole kv c...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: sed Change. 1. In ​**V1**​, the original logic of `KVCacheManager` and `BlockTable` is fully utilized to manage ​**CPU blocks**​. 2. A **`GPUCacheManager`** class is added to the **worker** to maintain the mapping betwe...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: **Goals:** - To accelerate the long sequence decoding and gurantee the accuracy, we plan implementing a hotness-ware multi-level kv cache management mechanism while keeping the sparse attention arithemetic computation u...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: tational overhead and memory consumption, resulting in low inference efficiency and high inference costs. Dynamic sparse attention mitigates the computational surge in long sequences, but the memory bottleneck remains....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: plan implementing a hotness-ware multi-level kv cache management mechanism while keeping the sparse attention arithemetic computation unchanged, - To achive good precision, different from KV compression and KV dropping...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: **Goals:** - To accelerate the long sequence decoding and gurantee the accuracy, we plan implementing a hotness-ware multi-level kv cache management mechanism while keeping the sparse attention arithemetic computation u...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
