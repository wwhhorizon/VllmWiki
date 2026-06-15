# vllm-project/vllm#10269: [Usage]: Adaptive Batching and number of concurrent requests

| 字段 | 值 |
| --- | --- |
| Issue | [#10269](https://github.com/vllm-project/vllm/issues/10269) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Adaptive Batching and number of concurrent requests

### Issue 正文摘录

### Your current environment I am using the async engine or docker with openai completions endpoint. ### How would you like to use vllm Lets say I am setting max num batched tokens to 50k. It tells me I can run 15 concurrent requests. Now as far as I understood adaptive batching, if one request finished computing, the batch is refilled with the next request ensuring a consistent throughput. So can I send 1000 requests at once and it would continuously process around 15 requests at a time by refilling the batch? Or should I only send 15 requests at a time and wait until they are processed to send the next 15? Is there some limit which would overwhelm the system? **Edit:** When sending a certain amount of requests at once, the engine kept crashing. This confused me and therefore this post. Turns out he engine just crashed because of a timeout as mentioned in #10002. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: uting, the batch is refilled with the next request ensuring a consistent throughput. So can I send 1000 requests at once and it would continuously process around 15 requests at a time by refilling the batch? Or should I...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: uests usage ### Your current environment I am using the async engine or docker with openai completions endpoint. ### How would you like to use vllm Lets say I am setting max num batched tokens to 50k. It tells me I can...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 02. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Adaptive Batching and number of concurrent requests usage ### Your current environment I am using the async engine or docker with openai completions endpoint. ### How would you like to use vllm Lets say I am se...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
