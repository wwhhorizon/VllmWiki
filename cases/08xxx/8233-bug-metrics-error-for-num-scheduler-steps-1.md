# vllm-project/vllm#8233: [Bug]: Metrics error for --num-scheduler-steps > 1

| 字段 | 值 |
| --- | --- |
| Issue | [#8233](https://github.com/vllm-project/vllm/issues/8233) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Metrics error for --num-scheduler-steps > 1

### Issue 正文摘录

### Your current environment Your output of `python collect_env.py` here ### 🐛 Describe the bug When `--num-scheduler-steps=n`, `do_log_stats()` is called only once every `n` step. However, when calculating `num_generation_tokens` within `do_log_stats()`, it only adds one generation token for each seq_group. This results in the `Avg generation throughput` metrics output being incorrect. ![image](https://github.com/user-attachments/assets/30072995-8ea2-4029-a65d-7936ff9fa9c5) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: generation token for each seq_group. This results in the `Avg generation throughput` metrics output being incorrect. ![image](https://github.com/user-attachments/assets/30072995-8ea2-4029-a65d-7936ff9fa9c5) ### Before s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: c5) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Metrics error for --num-scheduler-steps > 1 bug ### Your current environment Your output of `python collect_env.py` here ### 🐛 Describe the bug When `--num-scheduler-steps=n`, `do_log_stats()` is called only once...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
