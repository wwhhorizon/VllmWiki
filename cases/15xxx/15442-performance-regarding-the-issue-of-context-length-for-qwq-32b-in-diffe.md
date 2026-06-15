# vllm-project/vllm#15442: [Performance]: Regarding the issue of context length for QWQ-32B in different distributed environments:

| 字段 | 值 |
| --- | --- |
| Issue | [#15442](https://github.com/vllm-project/vllm/issues/15442) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Regarding the issue of context length for QWQ-32B in different distributed environments:

### Issue 正文摘录

### Proposal to improve performance I deployed QWQ-32B inference service using vllm in two different environments: (1) Single machine with two L20 GPUs（tensor_parallel_size=2，pipeline_parallel_size=1）， (2) Two machines, each with one L20 GPU（tensor_parallel_size=1，pipeline_parallel_size=2） . We found that, with the same parameters, (1) the single machine with two L20 GPUs supports context up to 45k, whereas (2) the environment with two machines, each with one L20 GPU, only supports up to 20k. Why is this happening? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ly supports up to 20k. Why is this happening? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: xt length for QWQ-32B in different distributed environments: performance;stale ### Proposal to improve performance I deployed QWQ-32B inference service using vllm in two different environments: (1) Single machine with t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
