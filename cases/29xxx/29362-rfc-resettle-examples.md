# vllm-project/vllm#29362: [RFC]: Resettle examples.

| 字段 | 值 |
| --- | --- |
| Issue | [#29362](https://github.com/vllm-project/vllm/issues/29362) |
| 状态 | closed |
| 标签 | RFC;keep-open |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Resettle examples.

### Issue 正文摘录

### Motivation. [The first-level directories of examples](https://github.com/vllm-project/vllm/tree/main/examples) are offline_inference, online_serving and others. This Taxonomy system forces users to search through multiple folders to find examples for specific use cases. ``` ├─examples │ ├─offline_inference │ │ ├─basic │ │ ├─disaggregated-prefill-v1 │ │ ├─kv_load_failure_recovery │ │ ├─logits_processor │ │ ├─openai_batch │ │ ├─pooling │ │ ├─qwen2_5_omni │ │ └─qwen3_omni │ ├─online_serving │ │ ├─chart-helm │ │ │ ├─templates │ │ │ └─tests │ │ ├─dashboards │ │ │ ├─grafana │ │ │ └─perses │ │ ├─disaggregated_encoder │ │ ├─disaggregated_serving │ │ ├─disaggregated_serving_p2p_nccl_xpyd │ │ ├─elastic_ep │ │ ├─openai_embedding_long_text │ │ ├─opentelemetry │ │ ├─pooling │ │ ├─prometheus_grafana │ │ └─structured_outputs │ └─others │ └─lmcache │ └─disagg_prefill_lmcache_v1 │ └─configs ``` ### Proposed Change. That would be great, if examples can be organized under usage scenarios as the first-level directories. e.g. ``` ├─examples │ ├─basic │ │ ├─offline_inference │ │ └─online_serving │ ├─disaggregated │ ├─expert_parallelism │ ├─kv_cache_offloading │ ├─observability │ ├─others │ ├─poolin...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ry │ │ ├─logits_processor │ │ ├─openai_batch │ │ ├─pooling │ │ ├─qwen2_5_omni │ │ └─qwen3_omni │ ├─online_serving │ │ ├─chart-helm │ │ │ ├─templates │ │ │ └─tests │ │ ├─dashboards │ │ │ ├─grafana │ │ │ └─perses │ │ ├─di...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rence, online_serving and others. This Taxonomy system forces users to search through multiple folders to find examples for specific use cases. ``` ├─examples │ ├─offline_inference │ │ ├─basic │ │ ├─disaggregated-prefil...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: forces users to search through multiple folders to find examples for specific use cases. ``` ├─examples │ ├─offline_inference │ │ ├─basic │ │ ├─disaggregated-prefill-v1 │ │ ├─kv_load_failure_recovery │ │ ├─logits_proces...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ─online_serving │ ├─disaggregated │ ├─expert_parallelism │ ├─kv_cache_offloading │ ├─observability │ ├─others │ ├─pooling │ │ ├─classify │ │ ├─embed │ │ ├─plugin │ │ ├─score │ │ ├─token_classify │ │ └─token_embed │ ├─rl...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: │ │ ├─offline_inference │ │ └─online_serving │ ├─disaggregated │ ├─expert_parallelism │ ├─kv_cache_offloading │ ├─observability │ ├─others │ ├─pooling │ │ ├─classify │ │ ├─embed │ │ ├─plugin │ │ ├─score │ │ ├─token_clas...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
