# vllm-project/vllm#12283: [Feature]: Add KV Cache Metrics to Usage Object

| 字段 | 值 |
| --- | --- |
| Issue | [#12283](https://github.com/vllm-project/vllm/issues/12283) |
| 状态 | closed |
| 标签 | good first issue;feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add KV Cache Metrics to Usage Object

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hello, we are hoping to allow our users to have a better understanding of what tokens are cached during their workloads. We would like to add KV cache metrics (e.g., cached tokens, tokens used from cache on a given request, etc.) as a part of the usage object so that the requestor can get a more detailed view of how their request interacted with the KV Cache. Ideally, this would extend to encapsulate metrics from [lmcache](https://docs.lmcache.ai/index.html) also. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add KV Cache Metrics to Usage Object good first issue;feature request;stale ### 🚀 The feature, motivation and pitch Hello, we are hoping to allow our users to have a better understanding of what tokens are ca...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Feature]: Add KV Cache Metrics to Usage Object good first issue;feature request;stale ### 🚀 The feature, motivation and pitch Hello, we are hoping to allow our users to have a better understanding of what tokens are ca...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
