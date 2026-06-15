# vllm-project/vllm#25210: [Feature]: Use deterministic hashing for KV events always

| 字段 | 值 |
| --- | --- |
| Issue | [#25210](https://github.com/vllm-project/vllm/issues/25210) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Use deterministic hashing for KV events always

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Motivation My understanding is that the KV events are mainly used to interface with the [NVIDIA Dynamo framework](https://github.com/ai-dynamo/dynamo), whose `KvIndexer` would always expect the external sequence hashes emitted by the engines to be consistent across backend engine processes. Therefore, it would probably make sense to always use SHA-256 hashing (or default to it) if the overhead is acceptable ## Pitch Always use SHA-256 hashing so the user does not need to set a fixed seed in the env var or set the `--prefix-caching-algo sha256` flag, as done [here](https://github.com/ai-dynamo/dynamo/pull/2981), which would mean the flag would be deprecated as well. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Use deterministic hashing for KV events always feature request;stale ### 🚀 The feature, motivation and pitch ## Motivation My understanding is that the KV events are mainly used to interface with the [NVIDIA...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Feature]: Use deterministic hashing for KV events always feature request;stale ### 🚀 The feature, motivation and pitch ## Motivation My understanding is that the KV events are mainly used to interface with the [NVIDIA...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: external sequence hashes emitted by the engines to be consistent across backend engine processes. Therefore, it would probably make sense to always use SHA-256 hashing (or default to it) if the overhead is acceptable ##...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Feature]: Use deterministic hashing for KV events always feature request;stale ### 🚀 The feature, motivation and pitch ## Motivation My understanding is that the KV events are mainly used to interface with the [NVIDIA...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
