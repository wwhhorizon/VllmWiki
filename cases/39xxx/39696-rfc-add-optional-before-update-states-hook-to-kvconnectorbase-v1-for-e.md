# vllm-project/vllm#39696: [RFC]: Add optional `before_update_states` hook to `KVConnectorBase_V1` for external KV cache integrations

| 字段 | 值 |
| --- | --- |
| Issue | [#39696](https://github.com/vllm-project/vllm/issues/39696) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Add optional `before_update_states` hook to `KVConnectorBase_V1` for external KV cache integrations

### Issue 正文摘录

### Motivation. External KV cache projects (AIBrix, LMCache, Mooncake, NixlConnector and similar) need to inject custom lookup logic into the request scheduling path — specifically, just **before** `GPUModelRunner._update_states()` runs, so that externally-cached prefix tokens can be reported back to the scheduler and skipped from recomputation. Today there is no public extension point for this. The only way to plug into that location is to **patch `gpu_model_runner.py` directly**. Each connector project carries one `.patch` file per supported vLLM release (AIBrix has 4 patches today: v0.8.5, v0.9.1, v0.10.2, v0.14.0), and each patch is several thousand lines because the surrounding context drifts between releases. Concrete numbers from the AIBrix v0.14 patch: - 4,057 lines, 9 modified files. - The actual hook insertion in `gpu_model_runner.py` is **~5 hunks of dict[str, int]: """Optional hook called before the model runner updates its per-request state for the current step. Connectors can use this to look up externally-cached KV blocks and report how many tokens of each request are already available in the external cache, so the scheduler can skip recomputation. Returns: A mappin...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: external project. ### Backwards compatibility - `KVConnectorBase_V1` ships a default implementation returning `{}`. - Existing connectors that don't override the hook see no behavior change. - The call site is gated on...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: .kv_connector is not None`, identical to how other connector hooks are dispatched today. - No public class is renamed or removed. ### Out of scope for this RFC - Changes to scheduler internals beyond consuming the retur...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: and each patch is several thousand lines because the surrounding context drifts between releases. Concrete numbers from the AIBrix v0.14 patch: - 4,057 lines, 9 modified files. - The actual hook insertion in `gpu_model_...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ptional `before_update_states` hook to `KVConnectorBase_V1` for external KV cache integrations RFC ### Motivation. External KV cache projects (AIBrix, LMCache, Mooncake, NixlConnector and similar) need to inject custom...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: t step. Connectors can use this to look up externally-cached KV blocks and report how many tokens of each request are already available in the external cache, so the scheduler can skip recomputation. Returns: A mapping...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
