# vllm-project/vllm#22916: [Feature][Kernel][B200]: FI MoE LL does not use `allgatherv` and `reduce-scatterv` for dispatch and combine

| 字段 | 值 |
| --- | --- |
| Issue | [#22916](https://github.com/vllm-project/vllm/issues/22916) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][Kernel][B200]: FI MoE LL does not use `allgatherv` and `reduce-scatterv` for dispatch and combine

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Flashinfer MoE low-latency backend doesn't leverage allgatherv and reduce-scatterv for dispatch and combine as in high-throughput backend. This cause a perf gap for DP + EP for large batch size. @wenscarl To enable. cc. @nvpohanh @kushanam @alexm-redhat ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: el][B200]: FI MoE LL does not use `allgatherv` and `reduce-scatterv` for dispatch and combine feature request ### 🚀 The feature, motivation and pitch Flashinfer MoE low-latency backend doesn't leverage allgatherv and re...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ture request ### 🚀 The feature, motivation and pitch Flashinfer MoE low-latency backend doesn't leverage allgatherv and reduce-scatterv for dispatch and combine as in high-throughput backend. This cause a perf gap for D...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature][Kernel][B200]: FI MoE LL does not use `allgatherv` and `reduce-scatterv` for dispatch and combine feature request ### 🚀 The feature, motivation and pitch Flashinfer MoE low-latency backend doesn't leverage all...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Feature][Kernel][B200]: FI MoE LL does not use `allgatherv` and `reduce-scatterv` for dispatch and combine feature request ### 🚀 The feature, motivation and pitch Flashinfer MoE low-latency backend doesn't leverage all...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: use `allgatherv` and `reduce-scatterv` for dispatch and combine feature request ### 🚀 The feature, motivation and pitch Flashinfer MoE low-latency backend doesn't leverage allgatherv and reduce-scatterv for dispatch and...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
