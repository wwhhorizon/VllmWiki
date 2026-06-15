# vllm-project/vllm#22531: [Usage]: How to choose max_num_batched_tokens when chunked prefill is enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#22531](https://github.com/vllm-project/vllm/issues/22531) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to choose max_num_batched_tokens when chunked prefill is enabled

### Issue 正文摘录

### Your current environment My question is unrelated to my current environment. ### How would you like to use vllm I am wondering how large max_num_batched_tokens could be set when 1) chunked prefill is enabled. 2) max_model_len is the max_positional_embedding, that is, you can not have the input + output longer than max_model_len. My questions are 1) if max_num_batched_tokens > max_model_len, what would happen? 2) I found that "If a last pending prefill request cannot fit into max_num_batched_tokens, it chunks it." here (https://docs.vllm.ai/en/v0.4.2/models/performance.html), does it mean that only the first max_num_batched_tokens - used_tokens tokens of the input would be chunked and their KV caches are prefilled? [Edit] Addition questions: 3) What limits how large max_num_batched_tokens can be with and without chunked prefill enabled? If I just want higher throughput, my understanding is that, in both cases, max_num_batched_tokens can be as high as possible until GPU usage is saturated or GPU memory is full. 4) If my prompt length is longer than max_model_len, does chunked prefill help in this case? My understanding is that it won't help given that you still need $(prompt len...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: How to choose max_num_batched_tokens when chunked prefill is enabled usage;stale ### Your current environment My question is unrelated to my current environment. ### How would you like to use vllm I am wonderin...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ched_tokens - used_tokens tokens of the input would be chunked and their KV caches are prefilled? [Edit] Addition questions: 3) What limits how large max_num_batched_tokens can be with and without chunked prefill enable...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: s can be with and without chunked prefill enabled? If I just want higher throughput, my understanding is that, in both cases, max_num_batched_tokens can be as high as possible until GPU usage is saturated or GPU memory...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: en. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: _batched_tokens could be set when 1) chunked prefill is enabled. 2) max_model_len is the max_positional_embedding, that is, you can not have the input + output longer than max_model_len. My questions are 1) if max_num_b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
