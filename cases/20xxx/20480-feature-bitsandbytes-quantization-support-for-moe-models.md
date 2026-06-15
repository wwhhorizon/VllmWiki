# vllm-project/vllm#20480: [Feature]: BitsandBytes Quantization Support for MoE Models

| 字段 | 值 |
| --- | --- |
| Issue | [#20480](https://github.com/vllm-project/vllm/issues/20480) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: BitsandBytes Quantization Support for MoE Models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch **Motivation** Currently, we supports 3 types of BNB quantization for dense models: - In-flight 4-bit quantization - Offline 4-bit quantization - Offline 8-bit quantization However, BNB inference has not yet been implemented for MoE models. To achieve feature parity and enable efficient deployment of MoE models, we need to extend support for all three quantization types to MoE models. **Related issues** https://github.com/vllm-project/vllm/issues/16121 https://github.com/vllm-project/vllm/issues/16713 https://github.com/vllm-project/vllm/issues/17199 https://github.com/vllm-project/vllm/issues/17337 **Related PRs** - In-flight 4-bit quantization: https://github.com/vllm-project/vllm/pull/20061 - offline 4-bit &8-bit quantizaion: https://github.com/vllm-project/vllm/pull/20864 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: BitsandBytes Quantization Support for MoE Models feature request;stale ### 🚀 The feature, motivation and pitch **Motivation** Currently, we supports 3 types of BNB quantization for dense models: - In-flight 4...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: een implemented for MoE models. To achieve feature parity and enable efficient deployment of MoE models, we need to extend support for all three quantization types to MoE models. **Related issues** https://github.com/vl...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: BitsandBytes Quantization Support for MoE Models feature request;stale ### 🚀 The feature, motivation and pitch **Motivation** Currently, we supports 3 types of BNB quantization for dense models: - In-flight 4...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: BitsandBytes Quantization Support for MoE Models feature request;stale ### 🚀 The feature, motivation and pitch **Motivation** Currently, we supports 3 types of BNB quantization for dense models: - In-flight 4...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
