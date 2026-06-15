# vllm-project/vllm#20950: [Feature]: Model execution timeout

| 字段 | 值 |
| --- | --- |
| Issue | [#20950](https://github.com/vllm-project/vllm/issues/20950) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Model execution timeout

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently when there is a bug in the path of model execution, it could hang indefinitely and user may not get timely and useful feedback. It would be useful to have a timeout mechanism and signal the user. Currently RayDistributedExecutor with Compiled Graph supports a timeout, but vLLM could benefit from supporting this in executor in general. See [discussion](https://vllm-dev.slack.com/archives/C08CBAP9BUG/p1752532064610089?thread_ts=1752477597.112679&cid=C08CBAP9BUG) cc @stephanie-wang @youkaichao ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ut mechanism and signal the user. Currently RayDistributedExecutor with Compiled Graph supports a timeout, but vLLM could benefit from supporting this in executor in general. See [discussion](https://vllm-dev.slack.com/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: timely and useful feedback. It would be useful to have a timeout mechanism and signal the user. Currently RayDistributedExecutor with Compiled Graph supports a timeout, but vLLM could benefit from supporting this in exe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Model execution timeout feature request;stale ### 🚀 The feature, motivation and pitch Currently when there is a bug in the path of model execution, it could hang indefinitely and user may not get timely and u...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Model execution timeout feature request;stale ### 🚀 The feature, motivation and pitch Currently when there is a bug in the path of model execution, it could hang indefinitely and user may not get timely and u...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
