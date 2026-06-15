# vllm-project/vllm#32066: [RFC]: Expose Sharding Metadata from vLLM Model Layers

| 字段 | 值 |
| --- | --- |
| Issue | [#32066](https://github.com/vllm-project/vllm/issues/32066) |
| 状态 | open |
| 标签 | RFC;stale;rl |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Expose Sharding Metadata from vLLM Model Layers

### Issue 正文摘录

### Motivation. Currently, downstream systems that need to understand how vLLM model weights are sharded must infer sharding patterns from tensor names using heuristics: ```python # Current approach: Pattern matching on tensor names def infer_sharding(tensor_name: str) -> ShardingType: if "gate_proj" in tensor_name or "up_proj" in tensor_name: return COLUMN_PARALLEL # [tp_size, 1] elif "down_proj" in tensor_name: return ROW_PARALLEL # [1, tp_size] elif "embed_tokens" in tensor_name: return VOCAB_PARALLEL # ... many more patterns ``` This approach has several problems: 1. **Fragile**: Different model architectures use different naming conventions (e.g., Llama uses `gate_proj`, other frameworks use `w13`, some use `fc1_weight`) 2. **Incomplete**: New layer types or model architectures require updating all downstream pattern matchers 3. **Error-prone**: Subtle naming differences can lead to incorrect sharding inference, causing silent data corruption during distributed operations 4. **Duplicated logic**: Every system that needs sharding info must implement and maintain its own pattern matching 5. **No support for complex sharding**: Advanced patterns like Grouped Query Attention (GQA...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: atterns like Grouped Query Attention (GQA) with head-aware reshaping, or MoE with Expert Parallel (EP) + Expert Tensor Parallel (ETP), are difficult to express through naming conventions alone **Use cases affected:** -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: `` This approach has several problems: 1. **Fragile**: Different model architectures use different naming conventions (e.g., Llama uses `gate_proj`, other frameworks use `w13`, some use `fc1_weight`) 2. **Incomplete**:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [RFC]: Expose Sharding Metadata from vLLM Model Layers RFC;stale;rl ### Motivation. Currently, downstream systems that need to understand how vLLM model weights are sharded must infer sharding patterns from tensor names...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ointing with different parallelization strategies - Model parallelism conversion (TP/PP/DP resharding) - Distributed debugging and visualization ### Proposed Change. ### Overview Each vLLM layer that performs weight sha...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [RFC]: Expose Sharding Metadata from vLLM Model Layers RFC;stale;rl ### Motivation. Currently, downstream systems that need to understand how vLLM model weights are sharded must infer sharding patterns from tensor names...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
