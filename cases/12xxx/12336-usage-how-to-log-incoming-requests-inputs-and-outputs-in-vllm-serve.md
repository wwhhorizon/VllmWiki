# vllm-project/vllm#12336: [Usage]: How to log incoming requests (inputs and outputs) in vllm serve ?

| 字段 | 值 |
| --- | --- |
| Issue | [#12336](https://github.com/vllm-project/vllm/issues/12336) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to log incoming requests (inputs and outputs) in vllm serve ?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm For in-the-wild deployment, we want to make sure service is used as intended. I'm currently serving the model with `vllm serve` command, however, I'm not sure how to log the requests (inputs/outputs) ? One workaround is to redirect stderr/stdout to a file, but that requires complex parsing (which fails at times....). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: How to log incoming requests (inputs and outputs) in vllm serve ? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm For in-the-wild de...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: want to make sure service is used as intended. I'm currently serving the model with `vllm serve` command, however, I'm not sure how to log the requests (inputs/outputs) ? One workaround is to redirect stderr/stdout to a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
