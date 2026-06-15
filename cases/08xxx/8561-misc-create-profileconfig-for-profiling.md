# vllm-project/vllm#8561: [Misc]: Create ProfileConfig for Profiling

| 字段 | 值 |
| --- | --- |
| Issue | [#8561](https://github.com/vllm-project/vllm/issues/8561) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Create ProfileConfig for Profiling

### Issue 正文摘录

### Anything you want to discuss about vllm. Not sure if this could be a meaningful feature, so I start a discussion here. In my use case, when profiling I care about memory usage too, so I add profile_memory=True option when initializing the profiler like this: However, since PyTorch Profiler offers many more options, I’m considering whether it would be beneficial to abstract this into a `ProfileConfig`. This way, vLLM users could easily and flexibly customize their profiling according to their specific needs. If you agree with this idea, I’d be happy to submit a PR about it. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Misc]: Create ProfileConfig for Profiling stale ### Anything you want to discuss about vllm. Not sure if this could be a meaningful feature, so I start a discussion here. In my use case, when profiling I care about mem...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: iler offers many more options, I’m considering whether it would be beneficial to abstract this into a `ProfileConfig`. This way, vLLM users could easily and flexibly customize their profiling according to their specific...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: it. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Misc]: Create ProfileConfig for Profiling stale ### Anything you want to discuss about vllm. Not sure if this could be a meaningful feature, so I start a discussion here. In my use case, when profiling I care about mem...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Misc]: Create ProfileConfig for Profiling stale ### Anything you want to discuss about vllm. Not sure if this could be a meaningful feature, so I start a discussion here. In my use case, when profiling I care about mem...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
