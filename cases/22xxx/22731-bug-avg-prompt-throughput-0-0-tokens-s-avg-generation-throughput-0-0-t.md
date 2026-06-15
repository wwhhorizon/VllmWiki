# vllm-project/vllm#22731: [Bug]: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 21.1%, Prefix cache hit rate: 11.9%

| 字段 | 值 |
| --- | --- |
| Issue | [#22731](https://github.com/vllm-project/vllm/issues/22731) |
| 状态 | open |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 21.1%, Prefix cache hit rate: 11.9%

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I use vLLM for large-scale inference, the following issue always occurs with the last task.：INFO 08-12 05:40:06 [loggers.py:111] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 21.1%, Prefix cache hit rate: 11.9% ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: neration throughput: 0.0 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 21.1%, Prefix cache hit rate: 11.9% bug ### Your current environment ### 🐛 Describe the bug When I use vLLM for large-scale infere...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 21.1%, Prefix cache hit rate: 11.9% bug ### Your current environment ### 🐛 Descr...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: s/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 21.1%, Prefix cache hit rate: 11.9% bug ### Your current environment ### 🐛 Describe the bug When I use vLLM for large-scale inference, the following issue alway...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: urrent environment ### 🐛 Describe the bug When I use vLLM for large-scale inference, the following issue always occurs with the last task.：INFO 08-12 05:40:06 [loggers.py:111] Engine 000: Avg prompt throughput: 0.0 toke...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .9% ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
