# vllm-project/vllm#16145: [Usage]: Can Lora adapters be loaded on different GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#16145](https://github.com/vllm-project/vllm/issues/16145) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Can Lora adapters be loaded on different GPUs

### Issue 正文摘录

### Your current environment Ubuntun ### How would you like to use vllm I currently need to investigate a question: Does the LoRa adapter for vllm have to run on the same GPU as the base model? For example, if a basic model and a LoRa adapter are running on a GPU, and the video memory is almost full, can we run another LoRa adapter on another GPU of the same node? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: de? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: : Does the LoRa adapter for vllm have to run on the same GPU as the base model? For example, if a basic model and a LoRa adapter are running on a GPU, and the video memory is almost full, can we run another LoRa adapter...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Can Lora adapters be loaded on different GPUs usage;stale ### Your current environment Ubuntun ### How would you like to use vllm I currently need to investigate a question: Does the LoRa adapter for vllm have...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
