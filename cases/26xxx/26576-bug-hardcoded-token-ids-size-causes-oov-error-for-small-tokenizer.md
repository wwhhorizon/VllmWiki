# vllm-project/vllm#26576: [Bug]: Hardcoded token_ids size causes OOV error for small tokenizer

| 字段 | 值 |
| --- | --- |
| Issue | [#26576](https://github.com/vllm-project/vllm/issues/26576) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Hardcoded token_ids size causes OOV error for small tokenizer

### Issue 正文摘录

### Your current environment cannot share ### 🐛 Describe the bug When running `vllm bench latency --tokenizer ...` and the tokenizer has less than the hardcoded 10k elements, the benchmark will crash with `ValueError: Token id 9435 is out of vocabulary`. The hardcoded value is here: https://github.com/vllm-project/vllm/blob/main/vllm/benchmarks/latency.py#L111 Can this value be changed to benchmark argument? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ironment cannot share ### 🐛 Describe the bug When running `vllm bench latency --tokenizer ...` and the tokenizer has less than the hardcoded 10k elements, the benchmark will crash with `ValueError: Token id 9435 is out...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Hardcoded token_ids size causes OOV error for small tokenizer bug;stale ### Your current environment cannot share ### 🐛 Describe the bug When running `vllm bench latency --tokenizer ...` and the tokenizer has les...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Hardcoded token_ids size causes OOV error for small tokenizer bug;stale ### Your current environment cannot share ### 🐛 Describe the bug When running `vllm bench latency --tokenizer ...` and the tokenizer has les...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
