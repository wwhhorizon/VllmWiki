# vllm-project/vllm#35807: [Feature]: Performance Tuning of FlashInfer MLA Sparse

| 字段 | 值 |
| --- | --- |
| Issue | [#35807](https://github.com/vllm-project/vllm/issues/35807) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Performance Tuning of FlashInfer MLA Sparse

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The sweep that motivated the heuristics in https://github.com/vllm-project/vllm/pull/33451 shows there are issues running with higher concurrencies and TP < 8, so the results are not giving full coverage. It seems that manual tuning can still give better perf. We should rerun the sweep with better coverage ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: Performance Tuning of FlashInfer MLA Sparse feature request ### 🚀 The feature, motivation and pitch The sweep that motivated the heuristics in https://github.com/vllm-project/vllm/pull/33451 shows there are i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ject/vllm/pull/33451 shows there are issues running with higher concurrencies and TP < 8, so the results are not giving full coverage. It seems that manual tuning can still give better perf. We should rerun the sweep wi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Performance Tuning of FlashInfer MLA Sparse feature request ### 🚀 The feature, motivation and pitch The sweep that motivated the heuristics in https://github.com/vllm-project/vllm/pull/33451 shows there are i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
