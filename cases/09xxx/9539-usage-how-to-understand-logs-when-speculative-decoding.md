# vllm-project/vllm#9539: [Usage]: how to understand logs (when speculative decoding)

| 字段 | 值 |
| --- | --- |
| Issue | [#9539](https://github.com/vllm-project/vllm/issues/9539) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to understand logs (when speculative decoding)

### Issue 正文摘录

### Your current environment ```text vllm 0.6.3 ``` ### How would you like to use vllm vllm of version v0.6.3: ``` INFO 10-16 19:05:47 metrics.py:367] Speculative metrics: Draft acceptance rate: 0.642, System efficiency: 0.598, Number of speculative tokens: 3, Number of accepted tokens: 8547, Number of draft tokens: 13311, Number of emitted tokens: 10616. INFO 10-16 19:06:01 metrics.py:361] Prefix cache hit rate: GPU: 94.35%, CPU: 0.00% ``` I want to know the meaning of `System efficiency`, `Number of emitted tokens` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ent ```text vllm 0.6.3 ``` ### How would you like to use vllm vllm of version v0.6.3: ``` INFO 10-16 19:05:47 metrics.py:367] Speculative metrics: Draft acceptance rate: 0.642, System efficiency: 0.598, Number of specul...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: how to understand logs (when speculative decoding) usage ### Your current environment ```text vllm 0.6.3 ``` ### How would you like to use vllm vllm of version v0.6.3: ``` INFO 10-16 19:05:47 metrics.py:367] Sp...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ber of emitted tokens: 10616. INFO 10-16 19:06:01 metrics.py:361] Prefix cache hit rate: GPU: 94.35%, CPU: 0.00% ``` I want to know the meaning of `System efficiency`, `Number of emitted tokens` ### Before submitting a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ns` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: 11, Number of emitted tokens: 10616. INFO 10-16 19:06:01 metrics.py:361] Prefix cache hit rate: GPU: 94.35%, CPU: 0.00% ``` I want to know the meaning of `System efficiency`, `Number of emitted tokens` ### Before submit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
