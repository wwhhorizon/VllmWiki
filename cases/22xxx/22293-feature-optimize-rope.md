# vllm-project/vllm#22293: [Feature]: Optimize RoPE

| 字段 | 值 |
| --- | --- |
| Issue | [#22293](https://github.com/vllm-project/vllm/issues/22293) |
| 状态 | closed |
| 标签 | good first issue;feature request;torch.compile |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Optimize RoPE

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Recently, we have noticed that rope is relatively slow with vLLM based on profiling. goal is to optimize rope by: - investigate why torch.compile's result is not optimal - investigate alternative kernels (e.g. FlashInfer's rope) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ecently, we have noticed that rope is relatively slow with vLLM based on profiling. goal is to optimize rope by: - investigate why torch.compile's result is not optimal - investigate alternative kernels (e.g. FlashInfer...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: .compile's result is not optimal - investigate alternative kernels (e.g. FlashInfer's rope) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you al...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: Optimize RoPE good first issue;feature request;torch.compile ### 🚀 The feature, motivation and pitch Recently, we have noticed that rope is relatively slow with vLLM based on profiling. goal is to optimize ro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Optimize RoPE good first issue;feature request;torch.compile ### 🚀 The feature, motivation and pitch Recently, we have noticed that rope is relatively slow with vLLM based on profiling. goal is to optimize ro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
