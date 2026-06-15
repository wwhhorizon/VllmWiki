# vllm-project/vllm#27636: [Usage]: vllm如何保留qwen3-vl中的special token

| 字段 | 值 |
| --- | --- |
| Issue | [#27636](https://github.com/vllm-project/vllm/issues/27636) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: vllm如何保留qwen3-vl中的special token

### Issue 正文摘录

### Your current environment 我微调过的qwen3-vl模型的grounding格式为： 图片 (x1,y1),(x2,y2) 使用vllm serve推理的格式是：图片(460,66),(683,252)，这个是直接忽略了special token么，是否有方法可以保留。 ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Usage]: vllm如何保留qwen3-vl中的special token usage;stale ### Your current environment 我微调过的qwen3-vl模型的grounding格式为： 图片 (x1,y1),(x2,y2) 使用vllm serve推理的格式是：图片(460,66),(683,252)，这个是直接忽略了special token么，是否有方法可以保留。 ### How would...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: vllm如何保留qwen3-vl中的special token usage;stale ### Your current environment 我微调过的qwen3-vl模型的grounding格式为： 图片 (x1,y1),(x2,y2) 使用vllm serve推理的格式是：图片(460,66),(683,252)，这个是直接忽略了special token么，是否有方法可以保留。 ### How would...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: vllm如何保留qwen3-vl中的special token usage;stale ### Your current environment 我微调过的qwen3-vl模型的grounding格式为： 图片 (x1,y1),(x2,y2) 使用vllm serve推理的格式是：图片(460,66),(683,252)，这个是直接忽略了special token么，是否有方法可以保留。 ### How would...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
