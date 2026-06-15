# vllm-project/vllm#27710: [Feature]: Faster apply_top_k_top_p without scatter

| 字段 | 值 |
| --- | --- |
| Issue | [#27710](https://github.com/vllm-project/vllm/issues/27710) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Faster apply_top_k_top_p without scatter

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In `apply_top_k_top_p`, the following code unpermutes the sorted logits: `logits = logits_sort.scatter(dim=-1, index=logits_idx, src=logits_sort)`. Then we randomly sample a token from the distribution by `return probs.div(q).argmax(dim=-1).view(-1)`. The two steps above are equivalent to `idx_permuted = probs.div(q).argmax(dim=-1).view(-1)` `return logits_idx[idx_permuted]` which (almostly) saves a `scatter` operation. `idx_permuted` is much smaller than `logits_sort`. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: d]` which (almostly) saves a `scatter` operation. `idx_permuted` is much smaller than `logits_sort`. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make su...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: eature, motivation and pitch In `apply_top_k_top_p`, the following code unpermutes the sorted logits: `logits = logits_sort.scatter(dim=-1, index=logits_idx, src=logits_sort)`. Then we randomly sample a token from the d...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Faster apply_top_k_top_p without scatter feature request;stale ### 🚀 The feature, motivation and pitch In `apply_top_k_top_p`, the following code unpermutes the sorted logits: `logits = logits_sort.scatter(di...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
