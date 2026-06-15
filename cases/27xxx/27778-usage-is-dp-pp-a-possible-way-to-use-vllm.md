# vllm-project/vllm#27778: [Usage]: Is DP + PP a possible way to use vLLM?

| 字段 | 值 |
| --- | --- |
| Issue | [#27778](https://github.com/vllm-project/vllm/issues/27778) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Is DP + PP a possible way to use vLLM?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hi there, I wonder if we can adopt DP + PP in vLLM to form a heterogeneous inference pipeline. For example, If i have two V100 32G GPUs and one A100 80G GPU, can I utilize them in pipeline parallelism with vLLM? I might use V100 as the first stage, and A100 as the second. Consider that V100's compute ability is lower than A100, this would result in unbalance, and the V100 stage becomes a bottleneck. Thus I would like to use two V100s in DP at the first PP stage. Is this possible with the current released vLLM version? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ous inference pipeline. For example, If i have two V100 32G GPUs and one A100 80G GPU, can I utilize them in pipeline parallelism with vLLM? I might use V100 as the first stage, and A100 as the second. Consider that V10...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: P at the first PP stage. Is this possible with the current released vLLM version? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Is DP + PP a possible way to use vLLM? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hi there, I wonder if we can adopt DP + PP in...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
