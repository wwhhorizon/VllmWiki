# vllm-project/vllm#21943: [Feature] Skip modules for disabled modalities

| 字段 | 值 |
| --- | --- |
| Issue | [#21943](https://github.com/vllm-project/vllm/issues/21943) |
| 状态 | closed |
| 标签 | good first issue;feature request;multi-modality |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature] Skip modules for disabled modalities

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Provide a way to skip loading modules by modality. We can enable this automatically via `--limit-mm-per-prompt`, as discussed in https://github.com/vllm-project/vllm/pull/20868#issuecomment-3071205115. For example, we can use text-only mode for an image-text model by setting `--limit-mm-per-prompt '{"image": 0}'` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ent-3071205115. For example, we can use text-only mode for an image-text model by setting `--limit-mm-per-prompt '{"image": 0}'` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature] Skip modules for disabled modalities good first issue;feature request;multi-modality ### 🚀 The feature, motivation and pitch Provide a way to skip loading modules by modality. We can enable this automatically...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
