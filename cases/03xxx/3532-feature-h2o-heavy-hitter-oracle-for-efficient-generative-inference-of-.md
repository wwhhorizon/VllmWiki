# vllm-project/vllm#3532: [Feature]: H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models

| 字段 | 值 |
| --- | --- |
| Issue | [#3532](https://github.com/vllm-project/vllm/issues/3532) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch This paper might be of interest: https://arxiv.org/pdf/2306.14048.pdf This paper mentions removing a small portion of the KV cache does not affect the results but improves memory efficiency. A 20% reduction in Heavy Hitters (H2) can increase throughput by 29 times and reduce latency by 1.9 times. When calculating attention scores, a small portion of tokens contribute the majority of the value. This paper proposes the Heavy Hitter Oracle (H2O), a KV cache eviction strategy that dynamically balances retention between recent tokens and H2 tokens. They frame the eviction problem of the KV cache as a dynamic submodular problem. Trade-off: Deleting some deemed unimportant KV cache may raise concerns about accuracy, but it reduces memory usage to improve throughput. @simon-mo Is this a feature you'd like to see implemented? ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: es memory efficiency. A 20% reduction in Heavy Hitters (H2) can increase throughput by 29 times and reduce latency by 1.9 times. When calculating attention scores, a small portion of tokens contribute the majority of th...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Feature]: H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models feature request;stale ### 🚀 The feature, motivation and pitch This paper might be of interest: https://arxiv.org/pdf/2306.1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: acle for Efficient Generative Inference of Large Language Models feature request;stale ### 🚀 The feature, motivation and pitch This paper might be of interest: https://arxiv.org/pdf/2306.14048.pdf This paper mentions re...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: -off: Deleting some deemed unimportant KV cache may raise concerns about accuracy, but it reduces memory usage to improve throughput. @simon-mo Is this a feature you'd like to see implemented? ### Alternatives _No respo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: st: https://arxiv.org/pdf/2306.14048.pdf This paper mentions removing a small portion of the KV cache does not affect the results but improves memory efficiency. A 20% reduction in Heavy Hitters (H2) can increase throug...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
