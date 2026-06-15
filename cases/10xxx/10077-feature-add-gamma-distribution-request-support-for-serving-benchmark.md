# vllm-project/vllm#10077: [Feature]: Add Gamma Distribution Request Support for Serving Benchmark.

| 字段 | 值 |
| --- | --- |
| Issue | [#10077](https://github.com/vllm-project/vllm/issues/10077) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add Gamma Distribution Request Support for Serving Benchmark.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I would like to propose adding support for requests based on the Gamma distribution in the serving benchmark. Today's requests in LLM serving show burstiness, and the Gamma distribution is more effective at simulating this bursty behavior compared to the Poisson process typically used. Both distributions can be implemented consistently with a `burstiness` parameter to regulate the level of burstiness, better aligning the benchmarking process with real-world scenarios and performance characteristics. ![gamma_distribution](https://github.com/user-attachments/assets/eef5773d-1956-47aa-aa40-305534f54b85) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Feature]: Add Gamma Distribution Request Support for Serving Benchmark. feature request ### 🚀 The feature, motivation and pitch I would like to propose adding support for requests based on the Gamma distribution in the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Add Gamma Distribution Request Support for Serving Benchmark. feature request ### 🚀 The feature, motivation and pitch I would like to propose adding support for requests based on the Gamma distribution in the...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
