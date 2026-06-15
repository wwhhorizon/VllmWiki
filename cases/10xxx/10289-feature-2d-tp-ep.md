# vllm-project/vllm#10289: [Feature]: 2D TP & EP

| 字段 | 值 |
| --- | --- |
| Issue | [#10289](https://github.com/vllm-project/vllm/issues/10289) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: 2D TP & EP

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I want to add 2D tensor parallelism and expert parallelism in vLLM. Which parts of the code should I modify? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ## 🚀 The feature, motivation and pitch I want to add 2D tensor parallelism and expert parallelism in vLLM. Which parts of the code should I modify? ### Alternatives _No response_ ### Additional context _No response_ ###...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: 2D TP & EP feature request;stale ### 🚀 The feature, motivation and pitch I want to add 2D tensor parallelism and expert parallelism in vLLM. Which parts of the code should I modify? ### Alternatives _No respo...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: e feature, motivation and pitch I want to add 2D tensor parallelism and expert parallelism in vLLM. Which parts of the code should I modify? ### Alternatives _No response_ ### Additional context _No response_ ### Before...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
