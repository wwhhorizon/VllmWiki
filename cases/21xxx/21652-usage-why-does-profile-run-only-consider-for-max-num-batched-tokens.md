# vllm-project/vllm#21652: [Usage]: Why does profile_run only consider for max_num_batched_tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#21652](https://github.com/vllm-project/vllm/issues/21652) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Why does profile_run only consider for max_num_batched_tokens

### Issue 正文摘录

### Your current environment Using V1 with chunked prefill enabled. ### How would you like to use vllm Hi, I want to confirm if the problem in this discussion is truly exist: https://discuss.vllm.ai/t/question-about-profile-run/1194 Let's assume that the `max_num_seqs` is set to 1, I found out that the current `profile_run` will only consider the peak memory inferring the **new tokens of size `max_num_batched_tokens`** but not related to `max_model_len`. If the chunked prefill is enabled, it may use more memory when `max_model_len` is larger than `max_num_batched_tokens` because on the last round of chunked prefill, it will have **computed tokens of size `max_model_len - max_num_batched_tokens` plus new tokens of size `max_num_batched_tokens`**. So when we have big `max_model_len` and small `max_num_batched_tokens` with chunked prefill enabled, the system may raise oom? I wonder if this is a real limitation or I am just getting this idea wrong. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of fr...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ize `max_num_batched_tokens`**. So when we have big `max_model_len` and small `max_num_batched_tokens` with chunked prefill enabled, the system may raise oom? I wonder if this is a real limitation or I am just getting t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ge]: Why does profile_run only consider for max_num_batched_tokens usage;stale ### Your current environment Using V1 with chunked prefill enabled. ### How would you like to use vllm Hi, I want to confirm if the problem...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Usage]: Why does profile_run only consider for max_num_batched_tokens usage;stale ### Your current environment Using V1 with chunked prefill enabled. ### How would you like to use vllm Hi, I want to confirm if the prob...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: x_num_batched_tokens` with chunked prefill enabled, the system may raise oom? I wonder if this is a real limitation or I am just getting this idea wrong. ### Before submitting a new issue... - [x] Make sure you already...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: **new tokens of size `max_num_batched_tokens`** but not related to `max_model_len`. If the chunked prefill is enabled, it may use more memory when `max_model_len` is larger than `max_num_batched_tokens` because on the l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
