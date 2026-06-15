# vllm-project/vllm#4670: [Usage]: prefix-caching

| 字段 | 值 |
| --- | --- |
| Issue | [#4670](https://github.com/vllm-project/vllm/issues/4670) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: prefix-caching

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to know how (if it can) vllm ensure the correctness when reusing KV cache under high-concurrency and system prompt difference? I noticed hash prefix tree is used in prefix-caching. If I launch a server with enabling prefix caching, considering the following three cases: #### case 1: some user called the service with identical system prompt but different usr prompt (many users with high concurrency and multi-session), will the KV cache be reused with cross-requests? for example, request 1 from session one: system prompt + usr prompt is: 'you are a clever assistant' + 'please introduce CNN to me.' request 2 from session two: system prompt + usr prompt is: 'you are a clever assistant' + 'what is the most popular interest place in China?' will request 2 reuse partial KV cache of request 1 ? as there are some tokens are identical. #### case 2: some user called the service with different system prompt and usr prompt(because they are under different tasks) request 1 from session one: system prompt + usr prompt is: 'you are developed by AIRR,' + 'please recommend some s...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: prefix-caching usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to know how (if it can) vllm ensure the correctness when reusi...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: completion) and in the further chat of the two session, will KV cache be mismatched between two sessions? #### case 3: only one user called the service in ONE session but with different system prompt and usr prompt. req...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: mpletion) and in the further chat of the two session, will KV cache be mismatched between two sessions? #### case 3: only one user called the service in ONE session but with different system prompt and usr prompt. reque...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: I want to know how (if it can) vllm ensure the correctness when reusing KV cache under high-concurrency and system prompt difference? I noticed hash prefix tree is used in prefix-caching. If I launch a server with enabl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
