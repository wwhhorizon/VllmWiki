# vllm-project/vllm#17780: [Feature][Improvement]: Benchmarking with random conversation lengths

| 字段 | 值 |
| --- | --- |
| Issue | [#17780](https://github.com/vllm-project/vllm/issues/17780) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][Improvement]: Benchmarking with random conversation lengths

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Background I'm trying to figure out how many users my vLLM server can handle and how increases in number of users and average request rate per user over time effect the important metrics (ttft, tpot, itl). In this research, I'm assuming the users will create conversation of varying lengths. I've started this research using the ShareGPT dataset, and I found that the number of users I was able to host for was a good amount above my expectations. I started looking into how sampling was implemented for ShareGPT, and found that each SampleRequest is generated using only the two first turns of the conversation. (In ShareGPT many of the conversations are multi turn conversation). ### Feature I would suggest a feature that makes the benchmark user able to control a maximum random length of conversations. Such that when sampling occurs, it isn't only 2 first turns of the conversation, but perhaps the first 6 turns. ### Why Sampling only the first two turns of each conversation underrepresents real-world usage, where conversations are often multi-turn and longer. This can lead to overly optimistic benchmark results. Supporting variable-length samp...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Feature][Improvement]: Benchmarking with random conversation lengths feature request;stale ### 🚀 The feature, motivation and pitch ### Background I'm trying to figure out how many users my vLLM server can handle and ho...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ure][Improvement]: Benchmarking with random conversation lengths feature request;stale ### 🚀 The feature, motivation and pitch ### Background I'm trying to figure out how many users my vLLM server can handle and how inc...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: length sampling would better reflect realistic workloads and improve the accuracy of performance evaluations. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: n number of users and average request rate per user over time effect the important metrics (ttft, tpot, itl). In this research, I'm assuming the users will create conversation of varying lengths. I've started this resea...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: r over time effect the important metrics (ttft, tpot, itl). In this research, I'm assuming the users will create conversation of varying lengths. I've started this research using the ShareGPT dataset, and I found that t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
