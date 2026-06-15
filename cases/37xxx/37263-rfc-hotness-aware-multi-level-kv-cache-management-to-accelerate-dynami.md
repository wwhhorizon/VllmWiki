# vllm-project/vllm#37263: [RFC]: Hotness-aware multi-level KV cache management to accelerate dynamic sparse attention

| 字段 | 值 |
| --- | --- |
| Issue | [#37263](https://github.com/vllm-project/vllm/issues/37263) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;model_support;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cache;kernel;sampling |
| 症状 |  |
| 根因提示 | memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Hotness-aware multi-level KV cache management to accelerate dynamic sparse attention

### Issue 正文摘录

### Motivation. Background: Long-context reasoning scenarios face a dual surge in computational overhead and memory consumption, resulting in low inference efficiency and high inference costs. Dynamic sparse attention mitigates the computational surge in long sequences, but the memory bottleneck remains. Under sparse attention, accesses to the KV cache exhibit a hot-cold distribution, presenting an opportunity for heterogeneous KV cache management. - Heterogeneous KV cache leverages cheap, scalable main memory to replace expensive, limited device memory, promising significant reductions in inference costs. - By retaining frequently accessed KV cache in device memory and swapping out infrequently accessed KV cache to main memory, the memory footprint of long sequences can be reduced. Goals: - To accelerate the long sequence decoding and guarantee the accuracy, we plan implementing a hotness-ware multi-level kv cache management mechanism while keeping the sparse attention arithmetic computation unchanged. - To achieve good precision, different from KV compression and KV dropping methods (issue5751, issue 12254, and pr 11938), this implementation chooses keeping the whole kv cache an...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: ndard OffloadingManager to integrate sparse selection logic - Maintains block representations for intelligent block scoring - Implements query-aware sparse selection to identify hot blocks - Reuses the original Offloadi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: d. Goals: - To accelerate the long sequence decoding and guarantee the accuracy, we plan implementing a hotness-ware multi-level kv cache management mechanism while keeping the sparse attention arithmetic computation un...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: plan implementing a hotness-ware multi-level kv cache management mechanism while keeping the sparse attention arithmetic computation unchanged. - To achieve good precision, different from KV compression and KV dropping...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: adingHandler - BlockReprManager is integrated into the worker pipeline - Configuration through SparseConfig with parameters like sparse_topk, copy_method, cache_policy This approach maintains full compatibility with the...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: d. Goals: - To accelerate the long sequence decoding and guarantee the accuracy, we plan implementing a hotness-ware multi-level kv cache management mechanism while keeping the sparse attention arithmetic computation un...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
