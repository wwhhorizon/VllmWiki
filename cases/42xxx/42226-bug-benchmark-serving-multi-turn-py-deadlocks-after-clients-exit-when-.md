# vllm-project/vllm#42226: [Bug]: benchmark_serving_multi_turn.py deadlocks after clients exit when --max-num-requests is used

| 字段 | 值 |
| --- | --- |
| Issue | [#42226](https://github.com/vllm-project/vllm/issues/42226) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: benchmark_serving_multi_turn.py deadlocks after clients exit when --max-num-requests is used

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **What happens:** When `--max-num-requests` is used with large conversations (e.g., ShareGPT multi-turn), `benchmark_serving_multi_turn.py` hangs forever after printing "All N clients exited". No stats summary is produced, no output JSON is written. **How to reproduce:** ```bash python benchmarks/multi_turn/benchmark_serving_multi_turn.py \ --model NousResearch/Hermes-3-Llama-3.1-8B \ --url http://localhost:8000 \ --input-file sharegpt_500.json \ --num-clients 8 \ --max-num-requests 2000 \ --output-file results.json ``` **Conditions that trigger it:** - `--max-num-requests` causes early termination (many unconsumed tasks remain in the queue) - Conversations are large enough that unconsumed items overflow the OS pipe buffer (~64KB on Linux) - More conversations queued than will be consumed (`num_conversations >> max_num_requests / avg_turns`) **Conditions where it does NOT trigger:** - Small/synthetic conversations (zipf) that fit in the pipe buffer - No `--max-num-requests` (all conversations consumed) **Expected behavior:** After "All N clients exited", the benchmark prints the statistics summary and writes the output JSON. **Ac...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: benchmark_serving_multi_turn.py deadlocks after clients exit when --max-num-requests is used ### Your current environment ### 🐛 Describe the bug **What happens:** When `--max-num-requests` is used with large conv...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: chmarks/multi_turn/benchmark_serving_multi_turn.py \ --model NousResearch/Hermes-3-Llama-3.1-8B \ --url http://localhost:8000 \ --input-file sharegpt_500.json \ --num-clients 8 \ --max-num-requests 2000 \ --output-file...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ash python benchmarks/multi_turn/benchmark_serving_multi_turn.py \ --model NousResearch/Hermes-3-Llama-3.1-8B \ --url http://localhost:8000 \ --input-file sharegpt_500.json \ --num-clients 8 \ --max-num-requests 2000 \...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: benchmark_serving_multi_turn.py deadlocks after clients exit when --max-num-requests is used ### Your current environment ### 🐛 Describe the bug **What happens:** When `--max-num-requests` is used with large conv...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ted". No stats summary is produced, no output JSON is written. **How to reproduce:** ```bash python benchmarks/multi_turn/benchmark_serving_multi_turn.py \ --model NousResearch/Hermes-3-Llama-3.1-8B \ --url http://local...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
