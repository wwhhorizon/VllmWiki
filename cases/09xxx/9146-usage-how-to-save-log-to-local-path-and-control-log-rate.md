# vllm-project/vllm#9146: [Usage]: How to save log to local path and control log rate?

| 字段 | 值 |
| --- | --- |
| Issue | [#9146](https://github.com/vllm-project/vllm/issues/9146) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to save log to local path and control log rate?

### Issue 正文摘录

### Your current environment . ### How would you like to use vllm I have find over from https://docs.vllm.ai/en/latest/serving/env_vars.html#environment-variables and https://github.com/vllm-project/vllm/blob/main/vllm/engine/arg_utils.py but I can not find any parameter about to save log to local path and control log rate. my vllm version is 0.5.1, VLLM_LOGGING_INTERVAL_SEC in https://github.com/vllm-project/vllm/pull/8213 is OK? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: parameter about to save log to local path and control log rate. my vllm version is 0.5.1, VLLM_LOGGING_INTERVAL_SEC in https://github.com/vllm-project/vllm/pull/8213 is OK? ### Before submitting a new issue... - [X] Mak...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: OK? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: How to save log to local path and control log rate? usage;stale ### Your current environment . ### How would you like to use vllm I have find over from https://docs.vllm.ai/en/latest/serving/env_vars.html#envir...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: d you like to use vllm I have find over from https://docs.vllm.ai/en/latest/serving/env_vars.html#environment-variables and https://github.com/vllm-project/vllm/blob/main/vllm/engine/arg_utils.py but I can not find any...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
