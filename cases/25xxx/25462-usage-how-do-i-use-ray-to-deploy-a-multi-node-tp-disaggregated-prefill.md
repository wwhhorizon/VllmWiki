# vllm-project/vllm#25462: [Usage]: How Do I use Ray to deploy a multi node TP Disaggregated Prefilling ?

| 字段 | 值 |
| --- | --- |
| Issue | [#25462](https://github.com/vllm-project/vllm/issues/25462) |
| 状态 | closed |
| 标签 | usage;ray;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How Do I use Ray to deploy a multi node TP Disaggregated Prefilling ?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference for a 1P1D setup, where both P and D utilize only Tensor Parallelism (TP) across multiple nodes. However, I'm unsure how to integrate this with vllm. I've tried using Ray with p2pNcclConnector and the lmcache+nixl approach, but neither works. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: erence for a 1P1D setup, where both P and D utilize only Tensor Parallelism (TP) across multiple nodes. However, I'm unsure how to integrate this with vllm. I've tried using Ray with p2pNcclConnector and the lmcache+nix...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: How Do I use Ray to deploy a multi node TP Disaggregated Prefilling ? usage;ray;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
