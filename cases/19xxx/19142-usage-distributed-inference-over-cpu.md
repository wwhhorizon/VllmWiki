# vllm-project/vllm#19142: [Usage]: Distributed Inference Over CPU

| 字段 | 值 |
| --- | --- |
| Issue | [#19142](https://github.com/vllm-project/vllm/issues/19142) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Distributed Inference Over CPU

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I am currently trying to run vLLM in pure CPU environments, and I noticed that vLLM now supports Inferencing over CPU. However, I'm not quite sure about whether vLLM support cross-node distributed inference, I beg to know about: 1. Does vLLM supports cross-node distributed inference in pure CPU environments (TCP is preferred for inter-node communication)? 2. If the answer is yes for the above question, how can I launch a cross-node CPU inference instance? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: LM in pure CPU environments, and I noticed that vLLM now supports Inferencing over CPU. However, I'm not quite sure about whether vLLM support cross-node distributed inference, I beg to know about: 1. Does vLLM supports...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ce? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Distributed Inference Over CPU usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I am currently trying to run vLLM in pure CPU environ...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
