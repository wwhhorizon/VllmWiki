# vllm-project/vllm#8547: [Feature]: Quantisation Support with CPU Backend

| 字段 | 值 |
| --- | --- |
| Issue | [#8547](https://github.com/vllm-project/vllm/issues/8547) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Quantisation Support with CPU Backend

### Issue 正文摘录

### 🚀 The feature, motivation and pitch According to [the docs](https://docs.vllm.ai/en/latest/quantization/supported_hardware.html) there is no support for quantised models when running with the CPU backend. I understand that this probably not a priority for this project but is there any plan to support that in the future? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Quantisation Support with CPU Backend feature request;stale ### 🚀 The feature, motivation and pitch According to [the docs](https://docs.vllm.ai/en/latest/quantization/supported_hardware.html) there is no sup...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: Quantisation Support with CPU Backend feature request;stale ### 🚀 The feature, motivation and pitch According to [the docs](https://docs.vllm.ai/en/latest/quantization/supported_hardware.html) there is no sup...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: Quantisation Support with CPU Backend feature request;stale ### 🚀 The feature, motivation and pitch According to [the docs](https://docs.vllm.ai/en/latest/quantization/supported_hardware.html) there is no sup...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: /quantization/supported_hardware.html) there is no support for quantised models when running with the CPU backend. I understand that this probably not a priority for this project but is there any plan to support that in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
