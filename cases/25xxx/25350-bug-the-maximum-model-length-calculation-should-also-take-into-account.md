# vllm-project/vllm#25350: [Bug]: The maximum model length calculation should also take into account the kv-cache-dtype

| 字段 | 值 |
| --- | --- |
| Issue | [#25350](https://github.com/vllm-project/vllm/issues/25350) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The maximum model length calculation should also take into account the kv-cache-dtype

### Issue 正文摘录

### 🐛 Describe the bug Using kv-cache-dtype fp8 gives twice as many tokens. However, the mechanism for calculating the maximum number of tokens does not take this into account and only allows the size as if the kv-cache-dtype flag were not set. with kv-cache-dtype fp8 and --max-model-len 100000 Available KV cache memory: 10.55 GiB GPU KV cache size: 230,528 tokens [kv_cache_utils.py:868] Maximum concurrency for 100,000 tokens per request: 2.31x with kv-cache-dtype fp8 and --max-model-len 221000 ValueError: To serve at least one request with the models's max seq len (221000), (10.12 GiB KV cache is needed, which is larger than the available KV cache memory (5.59 GiB). Based on the available memory, the estimated maximum model length is 122080. Try increasing `gpu_memory_utilization` or decreasing `max_model_len` when initializing the engine. It's strange that this flag changes the amount of available memory. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: imum model length calculation should also take into account the kv-cache-dtype bug;stale ### 🐛 Describe the bug Using kv-cache-dtype fp8 gives twice as many tokens. However, the mechanism for calculating the maximum num...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Using kv-cache-dtype fp8 gives twice as many tokens. However, the mechanism for calculating the maximum number of tokens does not take this into account and only allows the size as if the kv-cache-dtype flag were not se...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: : The maximum model length calculation should also take into account the kv-cache-dtype bug;stale ### 🐛 Describe the bug Using kv-cache-dtype fp8 gives twice as many tokens. However, the mechanism for calculating the ma...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: length calculation should also take into account the kv-cache-dtype bug;stale ### 🐛 Describe the bug Using kv-cache-dtype fp8 gives twice as many tokens. However, the mechanism for calculating the maximum number of toke...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: The maximum model length calculation should also take into account the kv-cache-dtype bug;stale ### 🐛 Describe the bug Using kv-cache-dtype fp8 gives twice as many tokens. However, the mechanism for calculating t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
