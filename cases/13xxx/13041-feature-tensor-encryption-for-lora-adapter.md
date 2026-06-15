# vllm-project/vllm#13041: [Feature]: Tensor encryption for LoRA Adapter

| 字段 | 值 |
| --- | --- |
| Issue | [#13041](https://github.com/vllm-project/vllm/issues/13041) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Tensor encryption for LoRA Adapter

### Issue 正文摘录

### 🚀 The feature, motivation and pitch With `Tensorizer`, vLLM have supporting tensor encryption to load model ([doc](https://docs.vllm.ai/en/stable/models/extensions/tensorizer.html)). But as I found, it is only for base model, not for adapter. Could you please consider tensor encryption on weights of adapter as well? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Tensor encryption for LoRA Adapter feature request;stale ### 🚀 The feature, motivation and pitch With `Tensorizer`, vLLM have supporting tensor encryption to load model ([doc](https://docs.vllm.ai/en/stable/m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: pitch With `Tensorizer`, vLLM have supporting tensor encryption to load model ([doc](https://docs.vllm.ai/en/stable/models/extensions/tensorizer.html)). But as I found, it is only for base model, not for adapter. Could...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
