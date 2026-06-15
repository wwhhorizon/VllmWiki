# vllm-project/vllm#10562: [Feature]: How to run speculative models with tensor parallelism?

| 字段 | 值 |
| --- | --- |
| Issue | [#10562](https://github.com/vllm-project/vllm/issues/10562) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: How to run speculative models with tensor parallelism?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I noticed that the current speculative mode does not support tp from this link (https://docs.vllm.ai/en/stable/models/spec_decode.html). However, not supporting TP will greatly limit the choice of speculative models. I would like to know why there is no TP support for speculative models. I am trying to read and modify this part of the code, but I don't understand why the scorer model can support TP, but the speculative model cannot. What are the considerations in system design? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: How to run speculative models with tensor parallelism? feature request;stale ### 🚀 The feature, motivation and pitch I noticed that the current speculative mode does not support tp from this link (https://doc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: How to run speculative models with tensor parallelism? feature request;stale ### 🚀 The feature, motivation and pitch I noticed that the current speculative mode does not support tp from this link (https://doc...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: noticed that the current speculative mode does not support tp from this link (https://docs.vllm.ai/en/stable/models/spec_decode.html). However, not supporting TP will greatly limit the choice of speculative models. I wo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: How to run speculative models with tensor parallelism? feature request;stale ### 🚀 The feature, motivation and pitch I noticed that the current speculative mode does not support tp from this link (https://doc...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
