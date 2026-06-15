# vllm-project/vllm#9643: [Bug]: preifx cache reuse

| 字段 | 值 |
| --- | --- |
| Issue | [#9643](https://github.com/vllm-project/vllm/issues/9643) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: preifx cache reuse

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I want to know whether the prefix cache in vllm supports automatic cache reuse before a request has been computed. For instance, if there is a new batch of requests with shared prefixes, will it automatically reuse the prefixes, or is it like TensorRT-LLM, where cache reuse for KV can only occur after the requestis complete? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: preifx cache reuse feature request;stale ### 🚀 The feature, motivation and pitch I want to know whether the prefix cache in vllm supports automatic cache reuse before a request has been computed. For instance, if...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: tale ### 🚀 The feature, motivation and pitch I want to know whether the prefix cache in vllm supports automatic cache reuse before a request has been computed. For instance, if there is a new batch of requests with shar...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
