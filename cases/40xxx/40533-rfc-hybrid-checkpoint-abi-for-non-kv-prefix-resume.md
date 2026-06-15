# vllm-project/vllm#40533: [RFC]: Hybrid checkpoint ABI for non-KV prefix resume

| 字段 | 值 |
| --- | --- |
| Issue | [#40533](https://github.com/vllm-project/vllm/issues/40533) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;frontend_api;model_support;sampling_logits;scheduler_memory |
| 子分类 | edge_case |
| Operator 关键词 | cache;cuda |
| 症状 | nondeterministic |
| 根因提示 | dtype;memory_layout;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Hybrid checkpoint ABI for non-KV prefix resume

### Issue 正文摘录

### Motivation. Prefix caching is comparatively clean for transformer KV state because the cache object and the reuse boundary align closely. Hybrid models complicate that with non-KV state such as recurrent state, conv buffers, and local-window or hybrid side state. That state is often updated in place, materialized differently across phases, backend-specific in storage layout, and not safely validated by raw backing-buffer equality alone. A recent Metal/MLX proof point showed that storing live runtime-backed arrays in a hybrid checkpoint cache can be unsafe, and that a correct restore contract must distinguish **payload immutability** from **logical state equality**. Public vLLM docs already describe hybrid cache coordination and still note that Mamba-style prefix caching is a work in progress. A checkpoint ABI would give hybrid recurrent-state resume the same kind of explicit correctness contract that APC already gives KV prefix reuse. Numbers from the Metal/MLX proof point: - first TTFT: 10.93s → repeated replay TTFT: 1.90s (~5.7x) - 8-request soak: warm-tail TTFT stable at 1.88–1.90s after request 1 - tool calls, content, and finish reason identical across replays - semantic...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: ol calls, content, and finish reason identical across replays - semantic drift fully eliminated on the tested Hermes workload Before the fix, repeated replay was fast but wrong: cache hits were real and TTFT collapsed,...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: ace, materialized differently across phases, backend-specific in storage layout, and not safely validated by raw backing-buffer equality alone. A recent Metal/MLX proof point showed that storing live runtime-backed arra...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: real and TTFT collapsed, but a request that previously emitted a `web_search` tool call would instead terminate with `stop` and no tool call on replay. After the fix, that drift is gone. This RFC proposes making that di...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ten updated in place, materialized differently across phases, backend-specific in storage layout, and not safely validated by raw backing-buffer equality alone. A recent Metal/MLX proof point showed that storing live ru...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: te because the cache object and the reuse boundary align closely. Hybrid models complicate that with non-KV state such as recurrent state, conv buffers, and local-window or hybrid side state. That state is often updated...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
