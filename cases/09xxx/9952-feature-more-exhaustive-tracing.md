# vllm-project/vllm#9952: [Feature]: more exhaustive tracing 

| 字段 | 值 |
| --- | --- |
| Issue | [#9952](https://github.com/vllm-project/vllm/issues/9952) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: more exhaustive tracing 

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I am using Opentelemetry traces to crack down slowness in vllm call. Only this `llm_request` one span comes out with some attributes. It only covers 10% of the time spent after a request to vllm's v1/completion endpoint. No nested span calls. Presumably the start of vllm_request span comes from seq_group.metrics.arrival_time, why it is seconds later than request to v1/compelete? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: more exhaustive tracing feature request;stale ### 🚀 The feature, motivation and pitch I am using Opentelemetry traces to crack down slowness in vllm call. Only this `llm_request` one span comes out with some...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: more exhaustive tracing feature request;stale ### 🚀 The feature, motivation and pitch I am using Opentelemetry traces to crack down slowness in vllm call. Only this `llm_request` one span comes out with some...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
