# vllm-project/vllm#44354: [Feature]: AMD Zen CPU CI

| 字段 | 值 |
| --- | --- |
| Issue | [#44354](https://github.com/vllm-project/vllm/issues/44354) |
| 状态 | open |
| 标签 | feature request;rocm |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: AMD Zen CPU CI

### Issue 正文摘录

### 🚀 The feature, motivation and pitch running vLLM on AMD Zen CPU (without GPU) is an supported platform in vLLM yet CI is lacking here https://github.com/vllm-project/vllm/pull/41813 @andyluo7 can u get machines allocated & hooked up? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: AMD Zen CPU CI feature request;rocm ### 🚀 The feature, motivation and pitch running vLLM on AMD Zen CPU (without GPU) is an supported platform in vLLM yet CI is lacking here https://github.com/vllm-project/vl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: AMD Zen CPU CI feature request;rocm ### 🚀 The feature, motivation and pitch running vLLM on AMD Zen CPU (without GPU) is an supported platform in vLLM yet CI is lacking here https://github.com/vllm-project/vl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: AMD Zen CPU CI feature request;rocm ### 🚀 The feature, motivation and pitch running vLLM on AMD Zen CPU (without GPU) is an supported platform in vLLM yet CI is lacking here https://github.com/vllm-project/vl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
