# vllm-project/vllm#31902: [Feature][Benchmarks] Be able to try a different prompt when sending the first test prompt instead of failing directly

| 字段 | 值 |
| --- | --- |
| Issue | [#31902](https://github.com/vllm-project/vllm/issues/31902) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][Benchmarks] Be able to try a different prompt when sending the first test prompt instead of failing directly

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When running benchmarks, an initial test run is performed with a random request from the dataset. The `wait_for_endpoint` function sends the same request in loop until either getting a successful response or reaching the timeout. The problem is that the request might be the problem, for example if the prompt + expected output tokens is too long and doesn't fit `max-model-len`, the request will fail for any number of trials. Being unlucky and sampling such an invalid prompt as test request shouldn't compromise the whole benchmark, there might be many other prompts that would run successfully. I suggest, the same as using a timeout duration, to allow testing with multiple prompts, say 5, before failing. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: t when sending the first test prompt instead of failing directly feature request;stale ### 🚀 The feature, motivation and pitch When running benchmarks, an initial test run is performed with a random request from the dat...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Feature][Benchmarks] Be able to try a different prompt when sending the first test prompt instead of failing directly feature request;stale ### 🚀 The feature, motivation and pitch When running benchmarks, an initial te...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: if the prompt + expected output tokens is too long and doesn't fit `max-model-len`, the request will fail for any number of trials. Being unlucky and sampling such an invalid prompt as test request shouldn't compromise...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
