# vllm-project/vllm#15313: [Bug]: vLLM declares itself healthy before it can serve requests

| 字段 | 值 |
| --- | --- |
| Issue | [#15313](https://github.com/vllm-project/vllm/issues/15313) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM declares itself healthy before it can serve requests

### Issue 正文摘录

### Your current environment TPU v6e on GKE ### 🐛 Describe the bug Roll out a new version of a deployment on GKE. The new pods will declare Ready/Healthy to GKE while still compiling the graph. This means requests start getting routed to them and failing. THis makes reliable rollouts impossible. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: vLLM declares itself healthy before it can serve requests bug;stale ### Your current environment TPU v6e on GKE ### 🐛 Describe the bug Roll out a new version of a deployment on GKE. The new pods will declare Read...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rent environment TPU v6e on GKE ### 🐛 Describe the bug Roll out a new version of a deployment on GKE. The new pods will declare Ready/Healthy to GKE while still compiling the graph. This means requests start getting rou...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
