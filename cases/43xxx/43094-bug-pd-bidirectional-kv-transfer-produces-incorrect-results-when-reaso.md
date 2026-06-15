# vllm-project/vllm#43094: [Bug][PD] Bidirectional KV transfer produces incorrect results when reasoning traces are stripped between turns

| 字段 | 值 |
| --- | --- |
| Issue | [#43094](https://github.com/vllm-project/vllm/issues/43094) |
| 状态 | open |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug][PD] Bidirectional KV transfer produces incorrect results when reasoning traces are stripped between turns

### Issue 正文摘录

This is an issue to make sure this behavior is tracked and consistently addressed by upper-level routers. ## Summary Bidirectional KV transfer (PR #32553, RFC #32733) can produce incorrect inference results when used with reasoning models (e.g. DeepSeek-R1) whose thinking traces are stripped from the conversation history between turns. ## Problem When D generates a response with thinking traces, its `kv_transfer_params` records: - `remote_num_tokens = request.num_computed_tokens` — covering `[prompt | thinking_tokens | response_tokens]` - `remote_block_ids` — physical blocks for the entire sequence On the next turn, if the client strips thinking traces before sending, P receives a prompt like `[prompt | response_tokens | new_user_msg]` — the thinking tokens are **missing from the middle**. The block-alignment logic in `_apply_prefix_caching` ([worker.py:2310-2316](https://github.com/vllm-project/vllm/blob/main/vllm/distributed/kv_transfer/kv_connector/v1/nixl/worker.py#L2310-L2316)) does **suffix trimming**: ```python remote_block_ids[i] = remote_group[-num_local_blocks:] ``` This assumes P's prompt is a strict prefix of D's sequence — true in the normal case, but **broken** when...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ke compacting history or dropping thinking traces). **Result:** P loads KV cache computed for different tokens than its actual input, leading to silently incorrect inference. ## Suggested Fixes **Router-level detection:...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ens` — covering `[prompt | thinking_tokens | response_tokens]` - `remote_block_ids` — physical blocks for the entire sequence On the next turn, if the client strips thinking traces before sending, P receives a prompt li...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: #32733) can produce incorrect inference results when used with reasoning models (e.g. DeepSeek-R1) whose thinking traces are stripped from the conversation history between turns. ## Problem When D generates a response w...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: sure this behavior is tracked and consistently addressed by upper-level routers. ## Summary Bidirectional KV transfer (PR #32553, RFC #32733) can produce incorrect inference results when used with reasoning models (e.g....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: hinking traces, its `kv_transfer_params` records: - `remote_num_tokens = request.num_computed_tokens` — covering `[prompt | thinking_tokens | response_tokens]` - `remote_block_ids` — physical blocks for the entire seque...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
