# vllm-project/vllm#34698: [Feature]: Atomic Rewind & Correct (ARC) via KV-Cache Rollback for Logical Grounding

| 字段 | 值 |
| --- | --- |
| Issue | [#34698](https://github.com/vllm-project/vllm/issues/34698) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Atomic Rewind & Correct (ARC) via KV-Cache Rollback for Logical Grounding

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Description Current LLM inference suffers from 15-30% compute waste (Parasitic Load) due to logical drift and physical reality violations. We propose integrating a monitoring layer support (SDAG Protocol) for Atomic Rewind & Correct (ARC). Motivation In our simulations, by utilizing KV-Cache Rollback at the moment of violation detection (e.g., physical constraints failure), we achieved up to 85% compute cycles saved. Proposed Solution Implement/Expose low-latency (<2ms) interrupt hooks in vLLM to allow an external sidecar (C++/Rust) to: Detect logical/deterministic defects mid-generation. Trigger an immediate KV-Cache Rollback to a safe state (Token #N-1). Resume with corrective constraints. Technical Specs & Evidence Latency: < 2ms. Trace Data: Detailed implementation logic and simulation traces are available here: [https://gist.github.com/alexbuiko-sketch/8d3a48fcbde51a19f769a1753b9870a3](https://github.com/vllm-project/vllm/issues) We believe this is essential for industrial-grade Mistral/Llama deployments where 100% reliability is required. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new is...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: up to 85% compute cycles saved. Proposed Solution Implement/Expose low-latency (<2ms) interrupt hooks in vLLM to allow an external sidecar (C++/Rust) to: Detect logical/deterministic defects mid-generation. Trigger an i...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: erence suffers from 15-30% compute waste (Parasitic Load) due to logical drift and physical reality violations. We propose integrating a monitoring layer support (SDAG Protocol) for Atomic Rewind & Correct (ARC). Motiva...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Feature]: Atomic Rewind & Correct (ARC) via KV-Cache Rollback for Logical Grounding feature request ### 🚀 The feature, motivation and pitch Description Current LLM inference suffers from 15-30% compute waste (Parasitic...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: /vllm/issues) We believe this is essential for industrial-grade Mistral/Llama deployments where 100% reliability is required. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a n...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
