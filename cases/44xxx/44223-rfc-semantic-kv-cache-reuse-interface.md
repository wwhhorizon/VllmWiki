# vllm-project/vllm#44223: [RFC]: Semantic KV Cache Reuse Interface

| 字段 | 值 |
| --- | --- |
| Issue | [#44223](https://github.com/vllm-project/vllm/issues/44223) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | shape_align |
| Operator 关键词 | attention;cache;cuda;operator;quantization |
| 症状 | build_error;mismatch;nondeterministic;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Semantic KV Cache Reuse Interface

### Issue 正文摘录

### Motivation. vLLM's exact prefix cache is the right primitive when requests share the same token prefix. Many long-context workloads have a nearby but different shape: the expensive reusable content is present, but the request starts with a different instruction, chat wrapper, retrieval order, or paraphrased lead-in. Exact prefix caching correctly misses in those cases. This potentially leaves a lot of potential optimization on the table. This proposal is about exposing the engine-side controls needed for that class of reuse without putting a semantic search algorithm in vLLM. External systems can discover donors; vLLM should continue to own scheduling, paged KV allocation, block lifetime, failure recovery, and exact prefix-cache semantics. - semantic lookup is an optional external policy decision, - reporting external tokens to vLLM is a materialization promise, - exact prefix-cache writes must remain exact, - any approximate or request-only reuse needs explicit cache-commit semantics before it can be enabled safely with prefix caching. ### Proposed Change. # Semantic KV Cache Connector Interface for vLLM ## Summary vLLM already has most of the control points needed for semant...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 9: ver donors; vLLM should continue to own scheduling, paged KV allocation, block lifetime, failure recovery, and exact prefix-cache semantics. - semantic lookup is an optional external policy decision, - reporting externa...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 8: [RFC]: Semantic KV Cache Reuse Interface RFC ### Motivation. vLLM's exact prefix cache is the right primitive when requests share the same token prefix. Many long-context workloads have a nearby but different shape: the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: C ### Motivation. vLLM's exact prefix cache is the right primitive when requests share the same token prefix. Many long-context workloads have a nearby but different shape: the expensive reusable content is present, but...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 7: but the request starts with a different instruction, chat wrapper, retrieval order, or paraphrased lead-in. Exact prefix caching correctly misses in those cases. This potentially leaves a lot of potential optimization o...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: eady has an explicit `num_external_computed_tokens` path, and the worker/model-runner path already lets connectors load KV into vLLM-owned paged KV slots before attention reads them. This proposal defines a conservative...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
