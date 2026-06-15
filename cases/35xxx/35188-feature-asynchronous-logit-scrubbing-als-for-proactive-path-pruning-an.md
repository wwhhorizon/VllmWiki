# vllm-project/vllm#35188: [Feature]: Asynchronous Logit Scrubbing (ALS) for Proactive Path Pruning and 85% Efficiency Gain

| 字段 | 值 |
| --- | --- |
| Issue | [#35188](https://github.com/vllm-project/vllm/issues/35188) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;frontend_api;model_support;sampling_logits;scheduler_memory |
| 子分类 | race_cond |
| Operator 关键词 | kernel |
| 症状 | nondeterministic;oom;slowdown |
| 根因提示 | memory_layout;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Asynchronous Logit Scrubbing (ALS) for Proactive Path Pruning and 85% Efficiency Gain

### Issue 正文摘录

### 🚀 The feature, motivation and pitch **Description:** **Is your feature request related to a problem? Please describe.** Current vLLM/SRT architecture suffers from the "Atomic Requirement Fallacy". The scheduler is reactive: it only sees the output after de-tokenization. On high-end compute (H100/A100), this leads to massive resource waste (up to 85% in our stress tests) as the GPU continues to propagate hallucinated or divergent states that could have been identified much earlier in the logit space. **Describe the solution you'd like** We propose the integration of **Asynchronous Logit Scrubbing (ALS)**. This moves vLLM from "reactive filtering" to **"proactive state pruning"**. **Key Architectural Components:** **Logit Sidecar Audit:** A non-blocking monitor that analyzes logit drift (Entropy/VDU) in parallel with the next hidden state computation. **Deterministic Inference Rewind:** Low-level access to the Block Manager to allow the scheduler to "rewind" the KV-cache and prune invalid reasoning paths before they propagate. **Pinned Memory Buffers:** Utilizing shared memory for zero-copy logit streaming between the Engine and the ALS Sidecar to maintain near-zero latency over...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: rubbing (ALS) for Proactive Path Pruning and 85% Efficiency Gain feature request;stale ### 🚀 The feature, motivation and pitch **Description:** **Is your feature request related to a problem? Please describe.** Current...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: 100/A100), this leads to massive resource waste (up to 85% in our stress tests) as the GPU continues to propagate hallucinated or divergent states that could have been identified much earlier in the logit space. **Descr...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: :** **Logit Sidecar Audit:** A non-blocking monitor that analyzes logit drift (Entropy/VDU) in parallel with the next hidden state computation. **Deterministic Inference Rewind:** Low-level access to the Block Manager t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: eature request related to a problem? Please describe.** Current vLLM/SRT architecture suffers from the "Atomic Requirement Fallacy". The scheduler is reactive: it only sees the output after de-tokenization. On high-end...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: level access to the Block Manager to allow the scheduler to "rewind" the KV-cache and prune invalid reasoning paths before they propagate. **Pinned Memory Buffers:** Utilizing shared memory for zero-copy logit streaming...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
