# vllm-project/vllm#9654: [Feature]: support SageAttention

| 字段 | 值 |
| --- | --- |
| Issue | [#9654](https://github.com/vllm-project/vllm/issues/9654) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: support SageAttention

### Issue 正文摘录

### 🚀 The feature, motivation and pitch [SageAttention](https://github.com/thu-ml/SageAttention) is a Quantized Attention that achieves speedups of 2.1x and 2.7x compared to FlashAttention2 and xformers, respectively, without lossing end-to-end metrics across various models. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: support SageAttention feature request;stale ### 🚀 The feature, motivation and pitch [SageAttention](https://github.com/thu-ml/SageAttention) is a Quantized Attention that achieves speedups of 2.1x and 2.7x co...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: Quantized Attention that achieves speedups of 2.1x and 2.7x compared to FlashAttention2 and xformers, respectively, without lossing end-to-end metrics across various models. ### Alternatives _No response_ ### Additional...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: and pitch [SageAttention](https://github.com/thu-ml/SageAttention) is a Quantized Attention that achieves speedups of 2.1x and 2.7x compared to FlashAttention2 and xformers, respectively, without lossing end-to-end metr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: formers, respectively, without lossing end-to-end metrics across various models. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
