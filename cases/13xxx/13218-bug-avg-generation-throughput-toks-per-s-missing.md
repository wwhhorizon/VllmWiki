# vllm-project/vllm#13218: [Bug]: avg_generation_throughput_toks_per_s missing

| 字段 | 值 |
| --- | --- |
| Issue | [#13218](https://github.com/vllm-project/vllm/issues/13218) |
| 状态 | closed |
| 标签 | bug;unstale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: avg_generation_throughput_toks_per_s missing

### Issue 正文摘录

### Your current environment After upgrading vllm 0.5.3. post1 to vllm 0.7.2, the avg.generation_throughput_toks_per_2 monitoring metric is missing from the metrics. ### 🐛 Describe the bug After upgrading vllm 0.5.3. post1 to vllm 0.7.2, the avg.generation_throughput_toks_per_2 monitoring metric is missing from the metrics. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: avg_generation_throughput_toks_per_s missing bug;unstale ### Your current environment After upgrading vllm 0.5.3. post1 to vllm 0.7.2, the avg.generation_throughput_toks_per_2 monitoring metric is missing from th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: cs. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: avg_generation_throughput_toks_per_s missing bug;unstale ### Your current environment After upgrading vllm 0.5.3. post1 to vllm 0.7.2, the avg.generation_throughput_toks_per_2 monitoring metric is missing from th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
