# vllm-project/vllm#15378: [Feature]: Add CoT dataset to the benchmark

| 字段 | 值 |
| --- | --- |
| Issue | [#15378](https://github.com/vllm-project/vllm/issues/15378) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add CoT dataset to the benchmark

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, the benchmarking datasets are prepared for vision or conversational tasks. While they represent some common tasks, they focus more on the short output scenario. Recently, reasoning LLMs have gained a lot of popularity, and there is a much longer decoding phase due to CoT generation. As a result, the performance behaviour will be different from previous LLMs. I think it would be nice if we can add some common datasets to the `BenchmarkDataset` to benchmark the reasoning LLMs and capture these characteristics. For instance: [ ] AIME 2024 [ ] LiveCodeBench ### Alternatives An alternative way to solve it is to use `RandomDataset` and set the random dataset's output length. However, it may not provide much insights into the reasoning LLM's behaviour as currently RandomDataset's prompt tokens are [purely meaningless](https://github.com/vllm-project/vllm/blob/3892e58ad7c0f325c9257cb3468aa1cde9e1ed6f/benchmarks/benchmark_dataset.py#L315-L326). A dataset of sensible and meaningful prompts is more suitable for benchmarking the performance of reasoning LLMs. ### Additional context I am happy to work on this! ### Before submitting a new issue...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add CoT dataset to the benchmark feature request;stale ### 🚀 The feature, motivation and pitch Currently, the benchmarking datasets are prepared for vision or conversational tasks. While they represent some c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Feature]: Add CoT dataset to the benchmark feature request;stale ### 🚀 The feature, motivation and pitch Currently, the benchmarking datasets are prepared for vision or conversational tasks. While they represent some c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: is! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
