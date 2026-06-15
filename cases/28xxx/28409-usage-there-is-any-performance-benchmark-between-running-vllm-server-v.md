# vllm-project/vllm#28409: [Usage]: There is any performance benchmark between running vLLM server via docker image and python?

| 字段 | 值 |
| --- | --- |
| Issue | [#28409](https://github.com/vllm-project/vllm/issues/28409) |
| 状态 | open |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: There is any performance benchmark between running vLLM server via docker image and python?

### Issue 正文摘录

### Your current environment ```text I mean, if I run a service with the vLLM docker image, it has any performance upgrade if comparing with running it as a python service (e.g., importing vllm package, setting up vllm inference, handling payload/responses, etc)? ``` ### How would you like to use vllm _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: age]: There is any performance benchmark between running vLLM server via docker image and python? usage;stale ### Your current environment ```text I mean, if I run a service with the vLLM docker image, it has any perfor...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Usage]: There is any performance benchmark between running vLLM server via docker image and python? usage;stale ### Your current environment ```text I mean, if I run a service with the vLLM docker image, it has any per...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: benchmark between running vLLM server via docker image and python? usage;stale ### Your current environment ```text I mean, if I run a service with the vLLM docker image, it has any performance upgrade if comparing with...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
