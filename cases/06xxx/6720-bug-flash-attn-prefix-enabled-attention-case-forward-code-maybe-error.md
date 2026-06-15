# vllm-project/vllm#6720: [Bug]: flash_attn  # prefix-enabled attention case forward code maybe error?

| 字段 | 值 |
| --- | --- |
| Issue | [#6720](https://github.com/vllm-project/vllm/issues/6720) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: flash_attn  # prefix-enabled attention case forward code maybe error?

### Issue 正文摘录

### Your current environment code review ### 🐛 Describe the bug flash_attn.py forward func code: else: # prefix-enabled attention assert prefill_meta.seq_lens is not None max_seq_len = max(prefill_meta.seq_lens) flash_attn_varlen_func( in this case,flash_attn_varlen_func input params order may be wrong. cu_seqlens_q=prefill_meta.query_start_loc, max_seqlen_q=prefill_meta.max_query_len, cu_seqlens_k=prefill_meta.seq_start_loc, max_seqlen_k=max_seq_len, the input order should be cu_s,cu_q,max_s,max_q?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: lash_attn # prefix-enabled attention case forward code maybe error? bug;stale ### Your current environment code review ### 🐛 Describe the bug flash_attn.py forward func code: else: # prefix-enabled attention assert pref...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ### 🐛 Describe the bug flash_attn.py forward func code: else: # prefix-enabled attention assert prefill_meta.seq_lens is not None max_seq_len = max(prefill_meta.seq_lens) flash_attn_varlen_func( in this case,flas

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
