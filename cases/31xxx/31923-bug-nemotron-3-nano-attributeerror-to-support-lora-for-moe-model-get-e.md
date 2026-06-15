# vllm-project/vllm#31923: [Bug]: Nemotron 3 nano - AttributeError: To support LoRA for MoE model, 'get_expert_mapping' must be implemented

| 字段 | 值 |
| --- | --- |
| Issue | [#31923](https://github.com/vllm-project/vllm/issues/31923) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Nemotron 3 nano - AttributeError: To support LoRA for MoE model, 'get_expert_mapping' must be implemented

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I get this error when loading nemotron 3 nano with lora: AttributeError: To support LoRA for MoE model, 'get_expert_mapping' must be implemented Why is this? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: Nemotron 3 nano - AttributeError: To support LoRA for MoE model, 'get_expert_mapping' must be implemented bug;stale ### Your current environment ### 🐛 Describe the bug I get this error when loading nemotron 3 nan...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: is? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: tron 3 nano - AttributeError: To support LoRA for MoE model, 'get_expert_mapping' must be implemented bug;stale ### Your current environment ### 🐛 Describe the bug I get this error when loading nemotron 3 nano with lora...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Nemotron 3 nano - AttributeError: To support LoRA for MoE model, 'get_expert_mapping' must be implemented bug;stale ### Your current environment ### 🐛 Describe the bug I get this error when loading nemotron 3 nan...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: support LoRA for MoE model, 'get_expert_mapping' must be implemented bug;stale ### Your current environment ### 🐛 Describe the bug I get this error when loading nemotron 3 nano with lora: AttributeError: To support LoRA...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
