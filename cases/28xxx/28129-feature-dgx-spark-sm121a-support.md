# vllm-project/vllm#28129: [Feature]: DGX Spark sm121a support

| 字段 | 值 |
| --- | --- |
| Issue | [#28129](https://github.com/vllm-project/vllm/issues/28129) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: DGX Spark sm121a support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Does vLLM support the DGX Spark hardware? I know nvidia provide a vLLM container with the support packaged, but i believe it uses vLLM version 0.10.2 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: DGX Spark sm121a support feature request ### 🚀 The feature, motivation and pitch Does vLLM support the DGX Spark hardware? I know nvidia provide a vLLM container with the support packaged, but i believe it us...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e a vLLM container with the support packaged, but i believe it uses vLLM version 0.10.2 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you alread...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: DGX Spark sm121a support feature request ### 🚀 The feature, motivation and pitch Does vLLM support the DGX Spark hardware? I know nvidia provide a vLLM container with the support packaged, but i believe it us...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
