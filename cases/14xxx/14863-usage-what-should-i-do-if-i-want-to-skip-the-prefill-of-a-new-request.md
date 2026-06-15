# vllm-project/vllm#14863: [Usage]: What should I do if I want to skip the prefill of a new request?

| 字段 | 值 |
| --- | --- |
| Issue | [#14863](https://github.com/vllm-project/vllm/issues/14863) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: What should I do if I want to skip the prefill of a new request?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm MyQuestion: I want to add a new request to engine, and make some dummy kv cache for it, and then let it directly start the decode stage. What should I do for this? Maybe I should first modify the STATUS in SeqGroup, allocate and faked some kv cache in the block manager? But i'm still confused about how to add the faked first output token for it? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Usage]: What should I do if I want to skip the prefill of a new request? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm MyQuestion: I want...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: it? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: MyQuestion: I want to add a new request to engine, and make some dummy kv cache for it, and then let it directly start the decode stage. What should I do for this? Maybe I should first modify the STATUS in SeqGroup, all...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: t modify the STATUS in SeqGroup, allocate and faked some kv cache in the block manager? But i'm still confused about how to add the faked first output token for it? ### Before submitting a new issue... - [x] Make sure y...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
