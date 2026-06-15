# vllm-project/vllm#43315: [Bug]: b12x NSA+MTP speculative decoding hangs on PCIe TP=8 — NCCL topology-aware scheduling fix

| 字段 | 值 |
| --- | --- |
| Issue | [#43315](https://github.com/vllm-project/vllm/issues/43315) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;hardware_porting;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | attention;cache;cuda |
| 症状 | nondeterministic;slowdown |
| 根因提示 | memory_layout;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: b12x NSA+MTP speculative decoding hangs on PCIe TP=8 — NCCL topology-aware scheduling fix

### Issue 正文摘录

### Your current environment 8× RTX PRO 6000 Blackwell, PCIe-only TP=8, Ubuntu 24.04, vLLM main + b12x ### 🐛 Describe the bug ## Bug: b12x NSA + MTP speculative decoding hangs on PCIe TP=8 When running GLM-5.1 or Kimi-K2.6 with b12x `B12X_MLA_SPARSE` backend + MTP speculative decoding on PCIe-only 8-GPU setup (TP=8, no NVLink), vLLM **always hangs** during decode. This is not intermittent — it is deterministic. ### Root Cause Three layers of conflict: 1. **NCCL on PCIe topology**: NCCL's default ring/tree communication pattern conflicts with b12x's barrier sync. During MTP verify, the all-reduce for draft token scoring and b12x's cross-GPU KV sync compete for the same PCIe bandwidth. Timing skew → deadlock. 2. **b12x scheduling vs MTP dynamic batch**: b12x's CUDA Graph requires fixed input shapes and static `page_table_1` layout. MTP verify produces variable-length accepted tokens, causing `nsa_cache_seqlens` to diverge from graph-captured state at replay time. 3. **NSA indexer dangling indices**: Draft tokens write temporary KV entries. If verify rejects them, KV cache rolls back but `topk_indices` from the indexer still reference the now-invalid entries → garbage attention outpu...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: b12x NSA+MTP speculative decoding hangs on PCIe TP=8 — NCCL topology-aware scheduling fix bug ### Your current environment 8× RTX PRO 6000 Blackwell, PCIe-only TP=8, Ubuntu 24.04, vLLM main + b12x ### 🐛 Describe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: NCCL topology-aware scheduling fix bug ### Your current environment 8× RTX PRO 6000 Blackwell, PCIe-only TP=8, Ubuntu 24.04, vLLM main + b12x ### 🐛 Describe the bug ## Bug: b12x NSA + MTP speculative decoding hangs on P...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ), vLLM **always hangs** during decode. This is not intermittent — it is deterministic. ### Root Cause Three layers of conflict: 1. **NCCL on PCIe topology**: NCCL's default ring/tree communication pattern conflicts wit...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ), vLLM **always hangs** during decode. This is not intermittent — it is deterministic. ### Root Cause Three layers of conflict: 1. **NCCL on PCIe topology**: NCCL's default ring/tree communication pattern conflicts wit...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: b12x NSA+MTP speculative decoding hangs on PCIe TP=8 — NCCL topology-aware scheduling fix bug ### Your current environment 8× RTX PRO 6000 Blackwell, PCIe-only TP=8, Ubuntu 24.04, vLLM main + b12x ### 🐛 Describe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
