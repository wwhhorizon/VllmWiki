# vllm-project/vllm#10377: [Feature]: NVIDIA Triton GenAI Perf Benchmark

| 字段 | 值 |
| --- | --- |
| Issue | [#10377](https://github.com/vllm-project/vllm/issues/10377) |
| 状态 | closed |
| 标签 | help wanted;good first issue;feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | frontend_api |
| 子分类 |  |
| Operator 关键词 | triton |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: NVIDIA Triton GenAI Perf Benchmark

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The GenAI perf toolkit from NVIDIA can be used as an alternative benchmark tools for vLLM. While we already have benchmark scripts and framework in `benchmarks` directory, we should test out different load generators to compare the performance and accuracy of the benchmark clients. In this issues, I described some tasks that we need help with to try out the new benchmark harness: * Compare the output of the genai perf with the `benchmark_serving`, on the coverage of the result metrics and the accuracy. * Vary the workloads ShareGPT/Sonnet/synthetics * Implement it as an alternative harness through the script. Happy to elaborate as well. https://pypi.org/project/genai-perf/ ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Feature]: NVIDIA Triton GenAI Perf Benchmark help wanted;good first issue;feature request;stale ### 🚀 The feature, motivation and pitch The GenAI perf toolkit from NVIDIA can be used as an alternative benchmark tools f...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: NVIDIA Triton GenAI Perf Benchmark help wanted;good first issue;feature request;stale ### 🚀 The feature, motivation and pitch The GenAI perf toolkit from NVIDIA can be used as an alternative benchmark tools for vLLM. Wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: NVIDIA Triton GenAI Perf Benchmark help wanted;good first issue;feature request;stale ### 🚀 The feature, motivation and pitch The GenAI perf toolkit from NVIDIA can be used as an alternative benchmark tools f...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: should test out different load generators to compare the performance and accuracy of the benchmark clients. In this issues, I described some tasks that we need help with to try out the new benchmark harness: * Compare t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
