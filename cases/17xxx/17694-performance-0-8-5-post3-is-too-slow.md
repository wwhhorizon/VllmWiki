# vllm-project/vllm#17694: [Performance]: 0.8.5.post3 is too slow

| 字段 | 值 |
| --- | --- |
| Issue | [#17694](https://github.com/vllm-project/vllm/issues/17694) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: 0.8.5.post3 is too slow

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I used the latest vllm to run qwen3 32b awq and found that the speed was approximately 10 tokens/s. Under the same configuration, qwen2.5 32b awq achieved 50 tokens/s. The difference in kv cache performance is also significant. 0.8.5.post3 on qwen 3：INFO 05-06 13:48:15 [loggers.py:111] Engine 000: Avg prompt throughput: 1.5 tokens/s, Avg generation throughput: 10.4 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.2%, Prefix cache hit rate: 0.0% the old verion on qwen 2.5: INFO 05-06 13:47:39 metrics.py:351] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 46.1 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 8.8%, CPU KV cache usage: 0.0%. ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of fre...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: roposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I used the latest vllm to run qwen3 32b awq and found that the speed was approximately 1...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: e configuration, qwen2.5 32b awq achieved 50 tokens/s. The difference in kv cache performance is also significant. 0.8.5.post3 on qwen 3：INFO 05-06 13:48:15 [loggers.py:111] Engine 000: Avg prompt throughput: 1.5 tokens...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: onse_ ### Misc discussion on performance I used the latest vllm to run qwen3 32b awq and found that the speed was approximately 10 tokens/s. Under the same configuration, qwen2.5 32b awq achieved 50 tokens/s. The differ...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ns/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.2%, Prefix cache hit rate: 0.0% the old verion on qwen 2.5: INFO 05-06 13:47:39 metrics.py:351] Avg prompt throughput: 0.0 tokens/s, Avg generation throughpu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
