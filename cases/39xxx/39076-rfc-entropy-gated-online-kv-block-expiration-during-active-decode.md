# vllm-project/vllm#39076: [RFC]: Entropy-Gated Online KV Block Expiration During Active Decode

| 字段 | 值 |
| --- | --- |
| Issue | [#39076](https://github.com/vllm-project/vllm/issues/39076) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cache;cuda;fp8;kernel;operator;quantization;triton |
| 症状 |  |
| 根因提示 | dtype;memory_layout;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Entropy-Gated Online KV Block Expiration During Active Decode

### Issue 正文摘录

### Motivation. vLLM's BlockSpaceManager and the attention kernel share no runtime feedback channel. Once physical KV cache blocks are allocated to a running request, they are immovable until the request completes or is preempted entirely. Under memory pressure, the scheduler's only available action is whole-request preemption — discarding all KV state and forcing full recomputation upon resumption. This is a blunt instrument. In practice, attention weight distributions during autoregressive decode are highly non-uniform: a small fraction of early context tokens accumulate the overwhelming majority of cumulative attention mass, while large contiguous spans of the KV cache contribute negligibly to every generated token. These "dead" blocks occupy physical pages indefinitely, even though evicting them would change model outputs by a provably bounded, negligible amount. Gap analysis against existing work: RFC #5751 / RFC #12254 (Sparse KV cache framework): Both closed. Both focus on prefill-time eviction using abstract CachePolicy interfaces. Neither establishes a live kernel → block manager feedback path during decode. PagedEviction (arXiv:2509.04377): Operates at prefill time using...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: sum(softmax_weights[h, t] for t in block b, for all h) to a GPU-resident float32 buffer of shape [max_num_blocks], updated via atomic adds. This path requires FlashAttention to be bypassed in favor of the Triton kernel...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 5: nd the attention kernel share no runtime feedback channel. Once physical KV cache blocks are allocated to a running request, they are immovable until the request completes or is preempted entirely. Under memory pressure...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [RFC]: Entropy-Gated Online KV Block Expiration During Active Decode RFC ### Motivation. vLLM's BlockSpaceManager and the attention kernel share no runtime feedback channel. Once physical KV cache blocks are allocated t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: key-norm proxies. Explicitly avoids attention score computation because FlashAttention does not return attention weights. Does not implement decode-phase intra-request block eviction. Not integrated with vLLM's BlockSpa...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: on by at most O(theta) in L∞ norm. For theta = 1e-3, this is within BF16 numerical precision and strictly dominated by existing quantization error in INT8/FP8 KV deployments. 4. Files Affected vllm/attention/backends/fl...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
