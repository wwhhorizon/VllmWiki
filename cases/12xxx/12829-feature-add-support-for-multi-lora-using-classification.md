# vllm-project/vllm#12829: [Feature]: Add support for multi-lora using classification

| 字段 | 值 |
| --- | --- |
| Issue | [#12829](https://github.com/vllm-project/vllm/issues/12829) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add support for multi-lora using classification

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I was trying to do multi-lora serving for a custom classification model, Qwen2VL with a classifier head. Seems like currently vLLM does not support this and i wanted to understand if there are any plans to add support in the near future. In case there isn’t any support for this, can anyone guide me as to how it can be achieved? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: pitch I was trying to do multi-lora serving for a custom classification model, Qwen2VL with a classifier head. Seems like currently vLLM does not support this and i wanted to understand if there are any plans to add sup...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add support for multi-lora using classification feature request;stale ### 🚀 The feature, motivation and pitch I was trying to do multi-lora serving for a custom classification model, Qwen2VL with a classifier...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
