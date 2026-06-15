# vllm-project/vllm#20619: [Usage]: Get Generation Metrics vllm v0.9.

| 字段 | 值 |
| --- | --- |
| Issue | [#20619](https://github.com/vllm-project/vllm/issues/20619) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Get Generation Metrics vllm v0.9.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I know that the variable Metrics is deprecated in the output of a model generation. But I absolutely need to have them (it is always at None now). Is there any way to be able to get the Metrics ? It involves metrics related to throughput, time to first token, etc... and should be related to each generation request and not a general profiling. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: e any way to be able to get the Metrics ? It involves metrics related to throughput, time to first token, etc... and should be related to each generation request and not a general profiling. ### Before submitting a new...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Get Generation Metrics vllm v0.9. usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I know that the variable Metrics is deprecated in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: g. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: vllm I know that the variable Metrics is deprecated in the output of a model generation. But I absolutely need to have them (it is always at None now). Is there any way to be able to get the Metrics ? It involves metric...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
