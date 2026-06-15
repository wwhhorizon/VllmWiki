# vllm-project/vllm#38839: fix(metrics): Prometheus counter crash on negative prompt tokens with external KV transfer

| 字段 | 值 |
| --- | --- |
| Issue | [#38839](https://github.com/vllm-project/vllm/issues/38839) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api |
| 子分类 |  |
| Operator 关键词 | cache |
| 症状 | crash |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> fix(metrics): Prometheus counter crash on negative prompt tokens with external KV transfer

### Issue 正文摘录

## Bug When using `NixlConnector` for disaggregated prefill/decode, the Prometheus metrics logger crashes with a negative prompt token count. **Error:** `vllm/v1/metrics/loggers.py:1316 — ValueError: Negative prompt token count` ## Environment - vLLM 0.18.0 (also reproduced on 0.16.0) - `NixlConnector` with `kv_buffer_device=cpu` - Decode worker receiving KV from remote prefill worker via NIXL LIBFABRIC over EFA RDMA - Cross-accelerator P/D: Trainium prefill → H100 decode ## Reproduction 1. Deploy disaggregated P/D with Dynamo frontend and NixlConnector 2. Send 8+ concurrent requests to the frontend 3. Decode engine crashes after processing ~4 requests ## Root Cause When KV cache arrives externally via NIXL, the prompt tokens are not counted in the decode worker's local metrics. The logger computes `prompt_tokens = total_tokens - completion_tokens`, which goes negative because the decode worker never saw the prompt tokens — they were processed on the remote prefill worker. ## Suggested Fix Clamp prompt token count to `max(0, ...)` in the metrics logger, or track externally-received prompt tokens separately via the KV connector metadata. The negative value is a bookkeeping artifact...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: xternal KV transfer ## Bug When using `NixlConnector` for disaggregated prefill/decode, the Prometheus metrics logger crashes with a negative prompt token count. **Error:** `vllm/v1/metrics/loggers.py:1316 — ValueError:...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: track externally-received prompt tokens separately via the KV connector metadata. The negative value is a bookkeeping artifact of disaggregated serving, not an actual error. ## Impact Kills the decode engine under susta...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: Error: Negative prompt token count` ## Environment - vLLM 0.18.0 (also reproduced on 0.16.0) - `NixlConnector` with `kv_buffer_device=cpu` - Decode worker receiving KV from remote prefill worker via NIXL LIBFABRIC over...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: NIXL LIBFABRIC over EFA RDMA - Cross-accelerator P/D: Trainium prefill → H100 decode ## Reproduction 1. Deploy disaggregated P/D with Dynamo frontend and NixlConnector 2. Send 8+ concurrent requests to the frontend 3. D...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: Decode engine crashes after processing ~4 requests ## Root Cause When KV cache arrives externally via NIXL, the prompt tokens are not counted in the decode worker's local metrics. The logger computes `prompt_tokens = to...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
