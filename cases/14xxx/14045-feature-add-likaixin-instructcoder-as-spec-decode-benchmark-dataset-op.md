# vllm-project/vllm#14045: [Feature]: Add likaixin/InstructCoder as spec decode benchmark dataset option

| 字段 | 值 |
| --- | --- |
| Issue | [#14045](https://github.com/vllm-project/vllm/issues/14045) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add likaixin/InstructCoder as spec decode benchmark dataset option

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Contribution to this issue: #14013 1. open up a pr and add to benchmark_latency/benchmark_serving 2. incorporate #13933 3. incorporate rejection sampler triton kernel #14930 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Add likaixin/InstructCoder as spec decode benchmark dataset option feature request ### 🚀 The feature, motivation and pitch Contribution to this issue: #14013 1. open up a pr and add to benchmark_latency/bench...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Feature]: Add likaixin/InstructCoder as spec decode benchmark dataset option feature request ### 🚀 The feature, motivation and pitch Contribution to this issue: #14013 1. open up a pr and add to benchmark_latency/bench...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: enchmark_serving 2. incorporate #13933 3. incorporate rejection sampler triton kernel #14930 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
