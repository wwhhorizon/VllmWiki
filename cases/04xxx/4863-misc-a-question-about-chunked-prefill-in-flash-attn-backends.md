# vllm-project/vllm#4863: [Misc]: a question about chunked-prefill in flash-attn backends

| 字段 | 值 |
| --- | --- |
| Issue | [#4863](https://github.com/vllm-project/vllm/issues/4863) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: a question about chunked-prefill in flash-attn backends

### Issue 正文摘录

### Anything you want to discuss about vllm. https://github.com/vllm-project/vllm/blob/99caa4910651754f3f68de518ca42349c8c424d1/vllm/attention/backends/flash_attn.py#L282 I noticed that in flash-attn backends. `forward_prefix` and `forward_decode` seem to be executed serially. Does `forward_decode` wait for `forward_prefix` to finish before running? Can this take advantage of the performance provided by chunked-prefill? I mean the tokens of prefill are in the same batch as the tokens of decode. ```python if prefill_meta := attn_metadata.prefill_metadata: output[:num_prefill_tokens] = PagedAttention.forward_prefix(...) if decode_meta := attn_metadata.decode_metadata: output[num_prefill_tokens:] = PagedAttention.forward_decode(...) ```

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Misc]: a question about chunked-prefill in flash-attn backends stale ### Anything you want to discuss about vllm. https://github.com/vllm-project/vllm/blob/99caa4910651754f3f68de518ca42349c8c424d1/vllm/attention/backen...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Misc]: a question about chunked-prefill in flash-attn backends stale ### Anything you want to discuss about vllm. https://github.com/vllm-project/vllm/blob/99caa4910651754f3f68de518ca42349c8c424d1/vllm/attention/backen...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: e same batch as the tokens of decode. ```python if prefill_meta := attn_metadata.prefill_metadata: output[:num_prefill_tokens] = PagedAttention.forward_prefix(...) if decode_meta := attn_metadata.decode_metadata: output...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
