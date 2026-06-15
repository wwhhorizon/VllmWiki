# vllm-project/vllm#42157: [Bug]: V1 Scheduler hard-fails on stale req_id in `_update_after_schedule` (defensive guard missing)

| 字段 | 值 |
| --- | --- |
| Issue | [#42157](https://github.com/vllm-project/vllm/issues/42157) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: V1 Scheduler hard-fails on stale req_id in `_update_after_schedule` (defensive guard missing)

### Issue 正文摘录

### Environment - vllm 0.19.1 (verified via vllm-omni's vendored copy) - Affected: v0.19.1, v0.20.0, v0.20.1, v0.20.2, main HEAD (sha 530d3713 as of 2026-05-09) - Model: MiniCPM-o-4.5 (multi-stage omni — Thinker / Talker / Code2Wav via vllm-omni) ### Bug V1 scheduler's `_update_after_schedule()` does an unchecked `self.requests[req_id]` lookup and hard-fails the engine core process with `KeyError` when the request was concurrently finished/aborted between schedule build and post-schedule update. This kills every active client connection. **This issue is about the hard-fail (defensive guard missing), not the underlying race itself.** The race condition (abort/finish ordering) is a separate concern; see #26400 for one related thread. ### Stack trace ``` File "vllm/v1/core/sched/scheduler.py", line 990, in _update_after_schedule request = self.requests[req_id] ~~~~~~~~~~~~~^^^^^^^^ KeyError: 'chatcmpl-8a6f39cb01952274' ``` ### Existing inconsistency in the same file `scheduler.py` already uses the defensive `.get(req_id)` pattern in many places: - ✅ `self.requests.get(req_id)` at lines 1235, 1296, 1606, 1633, 1715 - ❌ `self.requests[req_id]` (unchecked) at lines 944 (this bug), 1446,...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: V1 Scheduler hard-fails on stale req_id in `_update_after_schedule` (defensive guard missing) ### Environment - vllm 0.19.1 (verified via vllm-omni's vendored copy) - Affected: v0.19.1, v0.20.0, v0.20.1, v0.20.2,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: just isn't following it. ### Reproducer vllm-omni multi-stage setup (`backend=vllm_omni`, MiniCPM-o-Demo). Realtime WebSocket voice conversation, then either: - start a new turn before the previous response finishes, or...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: in this file — `_update_after_schedule()` just isn't following it. ### Reproducer vllm-omni multi-stage setup (`backend=vllm_omni`, MiniCPM-o-Demo). Realtime WebSocket voice conversation, then either: - start a new turn...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ror` when the request was concurrently finished/aborted between schedule build and post-schedule update. This kills every active client connection. **This issue is about the hard-fail (defensive guard missing), not the...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: quests()` synchronously removes the req from `self.requests` (via `_free_blocks()` and `del self.requests[...]` around lines 1755 / 1836). The `_update_after_schedule()` of the same step then hits the stale id and crash...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
