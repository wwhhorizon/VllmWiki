# vllm-project/vllm#12845: [Usage]: benchmark

| 字段 | 值 |
| --- | --- |
| Issue | [#12845](https://github.com/vllm-project/vllm/issues/12845) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: benchmark

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm hi， I want to know the difference between `Output token throughput (tok/s)` and `Time per Output Token` in benchmark ，like bellow： ============ Serving Benchmark Result ============ Successful requests: 772 Benchmark duration (s): 329.83 Total input tokens: 130743 Total generated tokens: 174589 Request throughput (req/s): 2.34 Output token throughput (tok/s): 529.33 Total Token throughput (tok/s): 925.72 ---------------Time to First Token---------------- Mean TTFT (ms): 249.49 Median TTFT (ms): 201.98 P99 TTFT (ms): 953.35 -----Time per Output Token (excl. 1st token)------ Mean TPOT (ms): 108.19 Median TPOT (ms): 108.15 P99 TPOT (ms): 169.89 ---------------Inter-token Latency---------------- Mean ITL (ms): 105.85 Median ITL (ms): 80.62 P99 ITL (ms): 340.52 ================================================== Output token throughput (tok/s) is 529.33，that is 1000/529=1.8 ms， but P99 TPOT (ms) is 169.89ms，it is so strange？ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner o...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Usage]: benchmark usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm hi， I want to know the difference between `Output token throughput (tok/s)` and...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ge？ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e bellow： ============ Serving Benchmark Result ============ Successful requests: 772 Benchmark duration (s): 329.83 Total input tokens: 130743 Total generated tokens: 174589 Request throughput (req/s): 2

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
