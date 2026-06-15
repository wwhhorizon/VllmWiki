# vllm-project/vllm#29580: [Feature]: [CPU Backend] Grouped GEMM kernel for CPU backend

| 字段 | 值 |
| --- | --- |
| Issue | [#29580](https://github.com/vllm-project/vllm/issues/29580) |
| 状态 | closed |
| 标签 | feature request;stale;cpu |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: [CPU Backend] Grouped GEMM kernel for CPU backend

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Implement Grouped GEMM kernel to optimize MOE for CPU backend ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Feature]: [CPU Backend] Grouped GEMM kernel for CPU backend feature request;stale;cpu ### 🚀 The feature, motivation and pitch Implement Grouped GEMM kernel to optimize MOE for CPU backend ### Alternatives _No response_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: [CPU Backend] Grouped GEMM kernel for CPU backend feature request;stale;cpu ### 🚀 The feature, motivation and pitch Implement Grouped GEMM kernel to optimize MOE for CPU backend ### Alternatives _No response_...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: [CPU Backend] Grouped GEMM kernel for CPU backend feature request;stale;cpu ### 🚀 The feature, motivation and pitch Implement Grouped GEMM kernel to optimize MOE for CPU backend ### Alternatives _No response_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
