# vllm-project/vllm#13498: [V1] Optimize rejection sampler

| 字段 | 值 |
| --- | --- |
| Issue | [#13498](https://github.com/vllm-project/vllm/issues/13498) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [V1] Optimize rejection sampler

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The current V1 rejection sampler is not optimized enough, taking unnecessary overheads. In my benchmarks, this takes 10-25% of the overall running time. We should profile & optimize it. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ion sampler is not optimized enough, taking unnecessary overheads. In my benchmarks, this takes 10-25% of the overall running time. We should profile & optimize it. ### Alternatives _No response_ ### Additional context...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [V1] Optimize rejection sampler feature request ### 🚀 The feature, motivation and pitch The current V1 rejection sampler is not optimized enough, taking unnecessary overheads. In my benchmarks, this takes 10-25% of the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
