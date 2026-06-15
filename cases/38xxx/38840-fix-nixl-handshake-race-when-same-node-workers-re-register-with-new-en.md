# vllm-project/vllm#38840: fix(nixl): Handshake race when same-node workers re-register with new engine IDs

| 字段 | 值 |
| --- | --- |
| Issue | [#38840](https://github.com/vllm-project/vllm/issues/38840) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> fix(nixl): Handshake race when same-node workers re-register with new engine IDs

### Issue 正文摘录

## Bug NIXL handshake assertion failure when a worker on the same node restarts and registers with a new engine ID. **Error:** `AssertionError` at `nixl_connector.py:2108` — layer count mismatch during re-handshake ## Environment - vLLM 0.16.0 / 0.18.0 with NixlConnector - Same-node disaggregated workers (both prefill and decode on one p5.48xlarge) - Dynamo with etcd-based service discovery ## Reproduction 1. Deploy prefill + decode workers on the same node using NixlConnector 2. Kill and restart one worker (it receives a new `engine_id` from the scheduler) 3. The restarted worker's handshake conflicts with the stale metadata from the old engine_id The old handshake entry still exists in the connector's metadata store. When the new worker registers from the same `host:port` but with a different `engine_id`, the layer count from the old registration does not match the new one, triggering the assertion at line 2108. ## Expected Behavior Re-registration from the same `host:port` should invalidate the stale handshake entry and accept the new metadata cleanly. ## Actual Behavior `AssertionError` on layer count mismatch. The connector holds stale metadata from the previous engine instan...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: 16.0 / 0.18.0 with NixlConnector - Same-node disaggregated workers (both prefill and decode on one p5.48xlarge) - Dynamo with etcd-based service discovery ## Reproduction 1. Deploy prefill + decode workers on the same n...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: . **Error:** `AssertionError` at `nixl_connector.py:2108` — layer count mismatch during re-handshake ## Environment - vLLM 0.16.0 / 0.18.0 with NixlConnector - Same-node disaggregated workers (both prefill and decode on...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: **Error:** `AssertionError` at `nixl_connector.py:2108` — layer count mismatch during re-handshake ## Environment - vLLM 0.16.0 / 0.18.0 with NixlConnector - Same-node disaggregated workers (both prefill and decode on o...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: scheduler) 3. The restarted worker's handshake conflicts with the stale metadata from the old engine_id The old handshake entry still exists in the connector's metadata store. When the new worker registers from the same...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
