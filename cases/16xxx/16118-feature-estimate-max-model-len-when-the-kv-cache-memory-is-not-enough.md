# vllm-project/vllm#16118: [Feature]: Estimate max-model-len when the KV cache memory is not enough

| 字段 | 值 |
| --- | --- |
| Issue | [#16118](https://github.com/vllm-project/vllm/issues/16118) |
| 状态 | closed |
| 标签 | help wanted;good first issue;feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Estimate max-model-len when the KV cache memory is not enough

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When the KV cache is not enough for holding one request, vLLM v1 will raise an error like this > ERROR 04-05 01:12:55 [core.py:390] ValueError: To serve at least one request with the models's max seq len (1048576), (24.00 GiB KV cache is needed, which is larger than the available KV cache memory (9.97 GiB). Try increasing `gpu_memory_utilization` or decreasing `max_model_len` when initializing the engine. It would be more convenient if we can provide an estimated `max_model_len` to the users in this error log. The estimation is more complex than `max_model_len = block_size * num_gpu_blocks` after the introduction of different types of KV cache like sliding window, and help wanted on implementing with binary search of `max_model_len` based on the `KVCacheSpec.max_memory_usage_bytes`. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: cache like sliding window, and help wanted on implementing with binary search of `max_model_len` based on the `KVCacheSpec.max_memory_usage_bytes`. ### Alternatives _No response_ ### Additional context _No response_ ###...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Feature]: Estimate max-model-len when the KV cache memory is not enough help wanted;good first issue;feature request ### 🚀 The feature, motivation and pitch When the KV cache is not enough for holding one request, vLLM...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: in this error log. The estimation is more complex than `max_model_len = block_size * num_gpu_blocks` after the introduction of different types of KV cache like sliding window, and help wanted on implementing with binary...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Estimate max-model-len when the KV cache memory is not enough help wanted;good first issue;feature request ### 🚀 The feature, motivation and pitch When the KV cache is not enough for holding one request, vLLM...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: n the KV cache memory is not enough help wanted;good first issue;feature request ### 🚀 The feature, motivation and pitch When the KV cache is not enough for holding one request, vLLM v1 will raise an error like this > E...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
