# vllm-project/vllm#37823: [RFC] Tail-Optimized LRU (T-LRU): Reducing Tail Latency via Conversation-Aware KV Cache Eviction

| 字段 | 值 |
| --- | --- |
| Issue | [#37823](https://github.com/vllm-project/vllm/issues/37823) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC] Tail-Optimized LRU (T-LRU): Reducing Tail Latency via Conversation-Aware KV Cache Eviction

### Issue 正文摘录

### Motivation. ## Summary We propose **Tail-Optimized LRU (T-LRU)**, a lightweight modification to vLLM's existing LRU prefix-cache eviction policy that reduces P95 tail Time-to-First-Token (TTFT) by up to **27.4%** on real conversation workloads, with no overhead during normal (cache-hit) operation and no change to API surface. The idea and full analysis appear in our paper: > **Tail-Optimized Caching for LLM Inference** > Wenxin Zhang, Yueying Li, Ciamac C. Moallemi, Tianyi Peng > **NeurIPS 2025.** arXiv: https://arxiv.org/abs/2510.15152 ## Motivation vLLM's current eviction policy is LRU. LRU maximizes cache-hit rate but is **conversation-length blind**: it treats a block from a 5-turn, 10 000-token conversation identically to a block from a 1-turn, 100-token conversation. This creates an avoidable source of tail latency. ## Key Insight T-LRU is **not** “keep everything from long conversations.” It asks a narrower question: > **How much of this conversation’s prefix do we need to keep so that the next turn still meets the TTFT target?** Suppose a conversation has `H` cached history blocks, the next turn is estimated to add `Q_hat` blocks, and the TTFT budget is `xi` blocks of...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ed to add `Q_hat` blocks, and the TTFT budget is `xi` blocks of uncached prefill work. If `c` history blocks remain cached, the next turn must recompute `(H - c) + Q_hat` blocks. To stay within budget, we need: `(H - c)...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ximizes cache-hit rate but is **conversation-length blind**: it treats a block from a 5-turn, 10 000-token conversation identically to a block from a 1-turn, 100-token conversation. This creates an avoidable source of t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ure/tlru-eviction-policy on github.com/wenxinzhang0/vllm vllm serve meta-llama/Llama-3-8B \ --enable-prefix-caching \ --tlru-xi-tokens 4096 \ --tlru-qhat-tokens 200 ``` ## References - Zhang, Li, Moallemi, Peng. *Tail-O...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [RFC] Tail-Optimized LRU (T-LRU): Reducing Tail Latency via Conversation-Aware KV Cache Eviction RFC ### Motivation. ## Summary We propose **Tail-Optimized LRU (T-LRU)**, a lightweight modification to vLLM's existing LR...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: *27.4%** on real conversation workloads, with no overhead during normal (cache-hit) operation and no change to API surface. The idea and full analysis appear in our paper: > **Tail-Optimized Caching for LLM Inference**...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
