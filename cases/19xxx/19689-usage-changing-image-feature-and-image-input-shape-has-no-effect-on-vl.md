# vllm-project/vllm#19689: [Usage]: Changing image_feature and image_input_shape has no effect on VLM output

| 字段 | 值 |
| --- | --- |
| Issue | [#19689](https://github.com/vllm-project/vllm/issues/19689) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Changing image_feature and image_input_shape has no effect on VLM output

### Issue 正文摘录

### Your current environment ```text Hi vLLM team, I'm currently experimenting with the experimental Vision Language Model (VLM) support in vLLM. While trying to customize the image processing behavior, I attempted to change the following parameters: image_feature image_input_shape However, changing these values did not affect the model's output at all. The response remained the same, as if the parameters were being ignored. Thank you for your amazing work — and for any guidance on this! Best regards, ``` ### How would you like to use vllm ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Changing image_feature and image_input_shape has no effect on VLM output usage;stale ### Your current environment ```text Hi vLLM team, I'm currently experimenting with the experimental Vision Language Model (V...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: llm ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ng image_feature and image_input_shape has no effect on VLM output usage;stale ### Your current environment ```text Hi vLLM team, I'm currently experimenting with the experimental Vision Language Model (VLM) support in...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
