# vllm-project/vllm#25950: [RFC]: Generalized KV cache reuse

| 字段 | 值 |
| --- | --- |
| Issue | [#25950](https://github.com/vllm-project/vllm/issues/25950) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Generalized KV cache reuse

### Issue 正文摘录

### Motivation. ### 🚀 The feature, motivation and pitch **Summary** This RFC proposes enabling the reuse of the KV cache for any subset of tokens, rather than restricting reuse to prefix-complete tokens. With the recently introduced KV cache connector abstraction (#15960) enabling retrieval from external storage, perforated KV caches naturally arise in real workloads. Supporting reuse in these cases avoids unnecessary recomputation and improves runtime efficiency. Looking ahead, generalized KV cache reuse unlocks richer capabilities: enabling reuse of KV entries for independent token segments across contexts — for example, in retrieval-augmented generation (RAG). This work should not be confused with sparse KV cache (#5751, #21772), where tokens are excluded from the attention computation. Here, all tokens may still participate in the computation; we simply enable reuse of even partially existing KV entries. **Background** In vLLM, efficient token generation relies heavily on KV cache reuse. The KV cache is generated and stored in the local GPU memory. When KV cache exists in GPU memory, it will always be prefix aligned. However, when external storage is used, with the intoduction...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [RFC]: Generalized KV cache reuse RFC;stale ### Motivation. ### 🚀 The feature, motivation and pitch **Summary** This RFC proposes enabling the reuse of the KV cache for any subset of tokens, rather than restricting reus...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [RFC]: Generalized KV cache reuse RFC;stale ### Motivation. ### 🚀 The feature, motivation and pitch **Summary** This RFC proposes enabling the reuse of the KV cache for any subset of tokens, rather than restricting reus...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: onnector and the scheduler. This change can be made opt-in via a runtime config flag (e.g., --enable-perforated-cache-handling), for controlled rollout. Note that FLASH_INFER’s backend doesnt need any change, as it supp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: forated-cache-handling), for controlled rollout. Note that FLASH_INFER’s backend doesnt need any change, as it supports masking. **Attention Kernel** To allow the attention kernel to control which query q is multiplied...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: in these cases avoids unnecessary recomputation and improves runtime efficiency. Looking ahead, generalized KV cache reuse unlocks richer capabilities: enabling reuse of KV entries for independent token segments across...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
