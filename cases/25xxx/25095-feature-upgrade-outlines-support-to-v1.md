# vllm-project/vllm#25095: [Feature]: Upgrade `outlines` support to v1

| 字段 | 值 |
| --- | --- |
| Issue | [#25095](https://github.com/vllm-project/vllm/issues/25095) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Upgrade `outlines` support to v1

### Issue 正文摘录

### 🚀 The feature, motivation and pitch `outlines` is available in v1.x meanwhile. It'd be great if vLLM upgraded its `outlines` pin to >=1.0. Apart from the apparent benefits of more stability, new features etc. this is also useful for all applications that use both `outlines` and vLLM directly. ### Alternatives _No response_ ### Additional context I'm maintaining a [zero-shot document processing library that does exactly this](https://github.com/MantisAI/sieves/), and I can't support the latest versions of both `outlines` and vLLM for this reason. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Upgrade `outlines` support to v1 feature request;stale ### 🚀 The feature, motivation and pitch `outlines` is available in v1.x meanwhile. It'd be great if vLLM upgraded its `outlines` pin to >=1.0. Apart from...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: is](https://github.com/MantisAI/sieves/), and I can't support the latest versions of both `outlines` and vLLM for this reason. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issue...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: n. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ly this](https://github.com/MantisAI/sieves/), and I can't support the latest versions of both `outlines` and vLLM for this reason. ### Before submitting a new issue... - [x] Make sure you already searched for relevant...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
