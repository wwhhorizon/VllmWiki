# vllm-project/vllm#25587: [Feature Request] Support `q_lora_rank=None` for MiniCPM3

| 字段 | 值 |
| --- | --- |
| Issue | [#25587](https://github.com/vllm-project/vllm/issues/25587) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature Request] Support `q_lora_rank=None` for MiniCPM3

### Issue 正文摘录

### 🚀 The feature, motivation and pitch #### 1. Motivation The immediate need for this proposal stems from a limitation in the current MiniCPM3 implementation: it strictly requires `q_lora_rank` to be an integer, causing an error for models where this value is `None`. Our team is developing a MiniCPM3-variant model with `q_lora_rank=None`, and this fix is crucial for its support in vLLM. #### 2. Benefits **Increased Versatility**: Natively supports a wider range of MiniCPM3 model configurations. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: t strictly requires `q_lora_rank` to be an integer, causing an error for models where this value is `None`. Our team is developing a MiniCPM3-variant model with `q_lora_rank=None`, and this fix is crucial for its suppor...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature Request] Support `q_lora_rank=None` for MiniCPM3 feature request;stale ### 🚀 The feature, motivation and pitch #### 1. Motivation The immediate need for this proposal stems from a limitation in the current Mini...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ing a MiniCPM3-variant model with `q_lora_rank=None`, and this fix is crucial for its support in vLLM. #### 2. Benefits **Increased Versatility**: Natively supports a wider range of MiniCPM3 model configurations. _No re...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
