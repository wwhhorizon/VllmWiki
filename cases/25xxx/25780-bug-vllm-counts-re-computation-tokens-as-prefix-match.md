# vllm-project/vllm#25780: [Bug]: vLLM counts re-computation tokens as prefix match

| 字段 | 值 |
| --- | --- |
| Issue | [#25780](https://github.com/vllm-project/vllm/issues/25780) |
| 状态 | closed |
| 标签 | bug;good first issue |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM counts re-computation tokens as prefix match

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I got a 30% prefix cache hit rate when profiling throughput on random dataset: ``` $ vllm bench throughput --model NousResearch/Hermes-3-Llama-3.1-8B --dataset-name random --num-prompts 1000 --input-len 1024 --output-len 1024 ... INFO 09-26 11:20:52 [loggers.py:127] Engine 000: Avg prompt throughput: 6102.8 tokens/s, Avg generation throughput: 1221.7 tokens/s, Running: 259 reqs, Waiting: 535 reqs, GPU KV cache usage: 82.3%, Prefix cache hit rate: 32.2% ``` The reason is that if requests are preempted and recomputed, these count in prefix cache hit rate. See [this thread](https://vllm-dev.slack.com/archives/C07R5Q1Q2BB/p1758911248156359) in vLLM slack for fix guidance. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: nment ### 🐛 Describe the bug I got a 30% prefix cache hit rate when profiling throughput on random dataset: ``` $ vllm bench throughput --model NousResearch/Hermes-3-Llama-3.1-8B --dataset-name random --num-prompts 1000...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: sue ### Your current environment ### 🐛 Describe the bug I got a 30% prefix cache hit rate when profiling throughput on random dataset: ``` $ vllm bench throughput --model NousResearch/Hermes-3-Llama-3.1-8B --dataset-nam...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: profiling throughput on random dataset: ``` $ vllm bench throughput --model NousResearch/Hermes-3-Llama-3.1-8B --dataset-name random --num-prompts 1000 --input-len 1024 --output-len 1024 ... INFO 09-26 11:20:52 [loggers...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: tokens/s, Avg generation throughput: 1221.7 tokens/s, Running: 259 reqs, Waiting: 535 reqs, GPU KV cache usage: 82.3%, Prefix cache hit rate: 32.2% ``` The reason is that if requests are preempted and recomputed, these...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: Your current environment ### 🐛 Describe the bug I got a 30% prefix cache hit rate when profiling throughput on random dataset: ``` $ vllm bench throughput --model NousResearch/Hermes-3-Llama-3.1-8B --dataset-name random...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
