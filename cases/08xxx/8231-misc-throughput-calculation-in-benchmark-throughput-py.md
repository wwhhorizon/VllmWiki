# vllm-project/vllm#8231: [Misc]: Throughput calculation in benchmark_throughput.py

| 字段 | 值 |
| --- | --- |
| Issue | [#8231](https://github.com/vllm-project/vllm/issues/8231) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Throughput calculation in benchmark_throughput.py

### Issue 正文摘录

### Anything you want to discuss about vllm. I just confused in benchmark scripts, why computes the throughput request input length, total_num_tokens = sum(prompt_len + output_len for _, prompt_len, output_len in requests) Normally, we consider the prefill and generated process performance, and the generated throughput can be define as: generated tokens/latency could somebody share comments on these? many thanks！ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Misc]: Throughput calculation in benchmark_throughput.py stale ### Anything you want to discuss about vllm. I just confused in benchmark scripts, why computes the throughput request input length, total_num_tokens = sum
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Misc]: Throughput calculation in benchmark_throughput.py stale ### Anything you want to discuss about vllm. I just confused in benchmark scripts, why computes the throughput request input length, total_num_tokens = sum...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ks！ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
