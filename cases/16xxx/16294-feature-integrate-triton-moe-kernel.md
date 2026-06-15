# vllm-project/vllm#16294: [Feature]: Integrate Triton MoE Kernel

| 字段 | 值 |
| --- | --- |
| Issue | [#16294](https://github.com/vllm-project/vllm/issues/16294) |
| 状态 | closed |
| 标签 | good first issue;feature request;stale |
| 评论 | 26; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Integrate Triton MoE Kernel

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Triton released a new MoE kernel: https://github.com/triton-lang/triton/pull/6429 Should be worth integrating into vLLM. Step 1: Benchmark on realistic sizes for MoEs vLLM supports. Step 2: Integrate into vLLM. A lot of help is needed here. Contribution welcomed! ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Integrate Triton MoE Kernel good first issue;feature request;stale ### 🚀 The feature, motivation and pitch Triton released a new MoE kernel: https://github.com/triton-lang/triton/pull/6429 Should be worth int...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: on-lang/triton/pull/6429 Should be worth integrating into vLLM. Step 1: Benchmark on realistic sizes for MoEs vLLM supports. Step 2: Integrate into vLLM. A lot of help is needed here. Contribution welcomed! ### Alternat...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: Integrate Triton MoE Kernel good first issue;feature request;stale ### 🚀 The feature, motivation and pitch Triton released a new MoE kernel: https://github.com/triton-lang/triton/pull/6429 Should be worth int...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Feature]: Integrate Triton MoE Kernel good first issue;feature request;stale ### 🚀 The feature, motivation and pitch Triton released a new MoE kernel: https://github.com/triton-lang/triton/pull/6429 Should be worth int...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
