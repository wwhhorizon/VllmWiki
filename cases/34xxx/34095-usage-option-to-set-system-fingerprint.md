# vllm-project/vllm#34095: [Usage]: Option to set system_fingerprint?

| 字段 | 值 |
| --- | --- |
| Issue | [#34095](https://github.com/vllm-project/vllm/issues/34095) |
| 状态 | open |
| 标签 | usage;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Option to set system_fingerprint?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I would like to know if there is an option to set the `system_fingerprint` returned in Chat Completions API via vLLM. I looked through the code base but couldn't find anything concrete, so thought I should ask here. I realize that OpenAI has announced they're deprecating this particular return value soon, but I think there is an inherent value in having a field which can help distinguish between servers that are being run in-house. I would be happy to raise a PR if this functionality doesn't exist currently, but I'd be hesitant to do so, if the `system_fingerprint` field is going to be removed soon according to OpenAI's deprecation timeline. For more context, we are interested in using that response field to be able to identify which GPUs our models are running on when the request is being served. cc @njhill @robertgshaw2-redhat @russellb would love to hear your thoughts/concerns! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Option to set system_fingerprint? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I would like to know if there is an option to set...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ns! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ested in using that response field to be able to identify which GPUs our models are running on when the request is being served. cc @njhill @robertgshaw2-redhat @russellb would love to hear your thoughts/concerns! ### B...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
