# vllm-project/vllm#34444: [RFC]: Decoupled Attention/FFN Parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#34444](https://github.com/vllm-project/vllm/issues/34444) |
| 状态 | open |
| 标签 | RFC;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Decoupled Attention/FFN Parallelism

### Issue 正文摘录

### Motivation. ### Introduction This RFC proposes extensions to vLLM's **Decode Context Parallelism (DCP)** to support: 1. **Decoupled attention/FFN parallelism** - Independent control of attention head sharding vs FFN sharding 2. **A2A communication backend** - Alternative to AllGather+ReduceScatter, enabling memory-efficient KV sharding for models with grouped KV heads (GQA, MLA) These extensions enable decoupled parallelism (as described in the [Helix paper](https://arxiv.org/abs/2507.07120)) where attention uses `head_parallel × kv_parallel` while FFN uses standard tensor parallelism, avoiding KV cache replication when scaling beyond the number of KV heads. Related RFC: #34018 ### The KV Replication Problem When using tensor parallelism, each GPU needs access to KV cache for attention computation. The relationship between `TP` (tensor parallel size) and `num_kv_heads` determines whether KV is **sharded** or **replicated**: ``` TP ≤ num_kv_heads: KV Sharded (Efficient) Example: TP=4, num_kv_heads=8 ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ │GPU 0 │ │GPU 1 │ │GPU 2 │ │GPU 3 │ │KV 0,1│ │KV 2,3│ │KV 4,5│ │KV 6,7│ ← Each GPU has unique KV └──────┘ └──────┘ └──────┘ └──────┘ TP > num_kv_...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ve to AllGather+ReduceScatter, enabling memory-efficient KV sharding for models with grouped KV heads (GQA, MLA) These extensions enable decoupled parallelism (as described in the [Helix paper](https://arxiv.org/abs/250...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [RFC]: Decoupled Attention/FFN Parallelism RFC;stale ### Motivation. ### Introduction This RFC proposes extensions to vLLM's **Decode Context Parallelism (DCP)** to support: 1. **Decoupled attention/FFN parallelism** -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: Decoupled Attention/FFN Parallelism RFC;stale ### Motivation. ### Introduction This RFC proposes extensions to vLLM's **Decode Context Parallelism (DCP)** to support: 1. **Decoupled attention/FFN parallelism** -...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ontrol of attention head sharding vs FFN sharding 2. **A2A communication backend** - Alternative to AllGather+ReduceScatter, enabling memory-efficient KV sharding for models with grouped KV heads (GQA, MLA) These extens...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: backend** - Alternative to AllGather+ReduceScatter, enabling memory-efficient KV sharding for models with grouped KV heads (GQA, MLA) These extensions enable decoupled parallelism (as described in the [Helix paper](http...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
