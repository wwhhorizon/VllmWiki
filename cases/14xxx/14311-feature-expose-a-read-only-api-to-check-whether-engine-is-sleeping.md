# vllm-project/vllm#14311: [Feature]: Expose a read-only API to check whether engine is sleeping

| 字段 | 值 |
| --- | --- |
| Issue | [#14311](https://github.com/vllm-project/vllm/issues/14311) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Expose a read-only API to check whether engine is sleeping

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The sleep feature works great! We can do even better by adding a read-only probe to check whether the engine is sleeping or not. Today the `/sleep` and `/wake_up` API endpoints `POST`s to the API server and mutates the state of the engine. We may introduce an `/is_sleeping` endpoint which `GET`s the sleep status. There are at least two use cases asking for this feature. 1. We are doing orchestration and optimization among multiple instances of vLLMs, asleep or awake. We need a global state of all the instances' sleeping status. The proposed probe is necessary to compose this state, without having to be stateful, i.e. remember whether each and every engine has been put asleep. 2. Today a sleeping engine crashes if a request is sent to it. This probe will give a good citizen peace of mind before sending a request. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: g engine crashes if a request is sent to it. This probe will give a good citizen peace of mind before sending a request. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new is...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ure]: Expose a read-only API to check whether engine is sleeping feature request ### 🚀 The feature, motivation and pitch The sleep feature works great! We can do even better by adding a read-only probe to check whether...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
