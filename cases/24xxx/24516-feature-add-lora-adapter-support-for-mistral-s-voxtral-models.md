# vllm-project/vllm#24516: [Feature]: Add LoRA adapter support for Mistral's Voxtral models

| 字段 | 值 |
| --- | --- |
| Issue | [#24516](https://github.com/vllm-project/vllm/issues/24516) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add LoRA adapter support for Mistral's Voxtral models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch For now, LoRA support could be implemented for text-only modules: ["q_proj", "k_proj", "v_proj", "o_proj"] Models: `mistralai/Voxtral-Mini-3B-2507` & `mistralai/Voxtral-Small-24B-2507` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: "o_proj"] Models: `mistralai/Voxtral-Mini-3B-2507` & `mistralai/Voxtral-Small-24B-2507` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you alread...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Add LoRA adapter support for Mistral's Voxtral models feature request ### 🚀 The feature, motivation and pitch For now, LoRA support could be implemented for text-only modules: ["q_proj", "k_proj", "v_proj", "...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Add LoRA adapter support for Mistral's Voxtral models feature request ### 🚀 The feature, motivation and pitch For now, LoRA support could be implemented for text-only modules: ["q_proj", "k_proj", "v_proj", "...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
