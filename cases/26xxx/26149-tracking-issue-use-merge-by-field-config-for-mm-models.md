# vllm-project/vllm#26149: [Tracking Issue]: Use `merge_by_field_config` for MM models

| 字段 | 值 |
| --- | --- |
| Issue | [#26149](https://github.com/vllm-project/vllm/issues/26149) |
| 状态 | closed |
| 标签 | feature request;multi-modality |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Tracking Issue]: Use `merge_by_field_config` for MM models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Implement #25676 for each MM model so input shapes are the same as their HF implementations, i.e. no need to use `flatten_bn` anymore. I'm going through the list in mostly alphabetical order: - [x] #26073 - [x] #26076 - [x] #26117 - [x] #26153 - [x] #26230 - [x] #26280 - [x] #26710 - [x] #26776 - [x] #26308 - [x] #26710 - [x] #26260 - [x] #26261 After all models have been migrated, I will try to merge `TensorSchema` with `MultiModalFieldConfig` so we can apply validation inside processor instead of model forward pass (which is the critical path) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Tracking Issue]: Use `merge_by_field_config` for MM models feature request;multi-modality ### 🚀 The feature, motivation and pitch Implement #25676 for each MM model so input shapes are the same as their HF implementati...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Tracking Issue]: Use `merge_by_field_config` for MM models feature request;multi-modality ### 🚀 The feature, motivation and pitch Implement #25676 for each MM model so input shapes are the same as their HF implementati...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
