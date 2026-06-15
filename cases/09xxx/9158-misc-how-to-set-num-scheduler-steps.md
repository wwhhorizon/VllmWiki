# vllm-project/vllm#9158: [Misc]: How to set num-scheduler-steps

| 字段 | 值 |
| --- | --- |
| Issue | [#9158](https://github.com/vllm-project/vllm/issues/9158) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: How to set num-scheduler-steps

### Issue 正文摘录

### Anything you want to discuss about vllm. Recently **num-scheduler-steps** was introduced to "set the maximum number of forward steps per scheduler call". Is there any documentation on what this exactly means? Also some guidance would on how to set this value would be much appreciated. For example, if I host a 70B model on 2x A100 with 80GB, does this narrow down the range of values I should consider? Thanks to all the amazing vllm contributers for making this great peace of software! 🏎 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: alue would be much appreciated. For example, if I host a 70B model on 2x A100 with 80GB, does this narrow down the range of values I should consider? Thanks to all the amazing vllm contributers for making this great pea...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Misc]: How to set num-scheduler-steps stale ### Anything you want to discuss about vllm. Recently **num-scheduler-steps** was introduced to "set the maximum number of forward steps per scheduler call". Is there any doc...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ns? Also some guidance would on how to set this value would be much appreciated. For example, if I host a 70B model on 2x A100 with 80GB, does this narrow down the range of values I should consider? Thanks to all the am...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: o set this value would be much appreciated. For example, if I host a 70B model on 2x A100 with 80GB, does this narrow down the range of values I should consider? Thanks to all the amazing vllm contributers for making th...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
