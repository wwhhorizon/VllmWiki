# vllm-project/vllm#20063: [Feature]: Fallback strategy for KV loading of KVConnectors.

| 字段 | 值 |
| --- | --- |
| Issue | [#20063](https://github.com/vllm-project/vllm/issues/20063) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Fallback strategy for KV loading of KVConnectors.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When we use KV cache connectors like the LMCache, we load the needed cache from disk/remote/other servers. In the example of using LMCache, the scheduler first looks up the cache pool and then starts loading. But we don't have any try-catch mechanism for the loading process. There can be unexpected behavior in the loading process (power outage, bugs), and we do not have a fallback plan. Now it results in a silent error. In case of a disk load failuer, the vLLM will just continue its computation with the random data. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: che pool and then starts loading. But we don't have any try-catch mechanism for the loading process. There can be unexpected behavior in the loading process (power outage, bugs), and we do not have a fallback plan. Now...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Fallback strategy for KV loading of KVConnectors. feature request ### 🚀 The feature, motivation and pitch When we use KV cache connectors like the LMCache, we load the needed cache from disk/remote/other serv...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: Fallback strategy for KV loading of KVConnectors. feature request ### 🚀 The feature, motivation and pitch When we use KV cache connectors like the LMCache, we load the needed cache from disk/remote/other serv...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: rs. feature request ### 🚀 The feature, motivation and pitch When we use KV cache connectors like the LMCache, we load the needed cache from disk/remote/other servers. In the example of using LMCache, the scheduler first...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
