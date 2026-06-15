# vllm-project/vllm#18327: [Feature]: Tree-Attention Support for Speculative Decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#18327](https://github.com/vllm-project/vllm/issues/18327) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Tree-Attention Support for Speculative Decoding

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### **Summary** We propose adding tree-attention-based speculative decoding support to vLLM to improve inference throughput, token acceptance rates, and memory efficiency during generation. This approach is inspired by SpecInfer ([[arXiv:2305.09781](https://arxiv.org/abs/2305.09781)](https://arxiv.org/abs/2310.08560)) and EAGLE2 ([arXiv:2406.16858](https://arxiv.org/abs/2406.16858)), both of which demonstrate state-of-the-art performance using token tree structures and topology-aware attention for parallel decoding. -------------------------------------------------------------------------------------------------------------- ### **Motivation** Current speculative decoding strategies in vLLM rely on batch expansion or multi-head proposals. These approaches face key limitations: - ❌ Low token acceptance rates, especially in long sequences or large models - ❌ Redundant computation and memory traffic due to duplicate KV cache updates - ❌ Inefficient parallelism across speculative paths Both SpecInfer and EAGLE2 propose using tree-based token structures combined with topology-aware masking, enabling efficient evaluation of multiple speculative pa...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: ttention-based speculative decoding support to vLLM to improve inference throughput, token acceptance rates, and memory efficiency during generation. This approach is inspired by SpecInfer ([[arXiv:2305.09781](https://a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: Tree-Attention Support for Speculative Decoding feature request;stale ### 🚀 The feature, motivation and pitch ### **Summary** We propose adding tree-attention-based speculative decoding support to vLLM to imp...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: to improve inference throughput, token acceptance rates, and memory efficiency during generation. This approach is inspired by SpecInfer ([[arXiv:2305.09781](https://arxiv.org/abs/2305.09781)](https://arxiv.org/abs/2310...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: emory traffic due to duplicate KV cache updates - ❌ Inefficient parallelism across speculative paths Both SpecInfer and EAGLE2 propose using tree-based token structures combined with topology-aware masking, enabling eff...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ulative paths in a single kernel invocation. This approach improves both accuracy and decoding speed. -------------------------------------------------------------------------------------------------------------- ### **...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
