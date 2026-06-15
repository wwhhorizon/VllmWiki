# vllm-project/vllm#2349: [Feature] Support for SelfExtend-style context expansion

| 字段 | 值 |
| --- | --- |
| Issue | [#2349](https://github.com/vllm-project/vllm/issues/2349) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature] Support for SelfExtend-style context expansion

### Issue 正文摘录

In the paper [LLM Maybe LongLM: Self-Extend LLM Context Window Without Tuning](https://arxiv.org/pdf/2401.01325.pdf), the authors describe a method to extend the context-window of _any rope-based_ model without fine-tuning at inference time. I haven't gotten around to testing it myself but the results reported in the paper seem game-changing. How could we add support for this in vllm? Their algorithm: ```py q, k, v # queries, keys, and values seq_len, pos # input sequence length, position_idx g_size, w_size = G, w_n # normal self-attention ngb_q = apply_pos_emcode(q, pos) ngb_k = apply_pos_emcode(k, pos) ngb_attn = matmul(ngb_q, ngb_k) ngb_attn = causal_mask(ngb_attn) # grouped self-attention g_pos = pos // g_size # the floor operation shift = w_size - w_size // g_size s_g_pos = g_pos + shift g_q = apply_pos_emcode(q, s_g_pos) g_k = apply_pos_emcode(k, g_pos) g_attn = matmul(g_q, g_k) g_attn = causal_mask(g_attn) g_mask = tril(ones([seq_len-w_size, seq_len-w_size])) mask = ones([seq_len, seq_len]) mask[w_size:, :-w_size] -= g_mask attn = where(mask, ngb_attn, g_attn) # merge by replacement attn_weights = softmax(attn) output = matmul(attn_weights, v) ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: thors describe a method to extend the context-window of _any rope-based_ model without fine-tuning at inference time. I haven't gotten around to testing it myself but the results reported in the paper seem game-changing...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature] Support for SelfExtend-style context expansion stale In the paper [LLM Maybe LongLM: Self-Extend LLM Context Window Without Tuning](https://arxiv.org/pdf/2401.01325.pdf), the authors describe a method to exten...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: model without fine-tuning at inference time. I haven't gotten around to testing it myself but the results reported in the paper seem game-changing. How could we add support for this in vllm? Their algorithm: ```py q, k,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
