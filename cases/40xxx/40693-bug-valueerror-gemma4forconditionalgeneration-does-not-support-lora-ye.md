# vllm-project/vllm#40693: [Bug]: ValueError: Gemma4ForConditionalGeneration does not support LoRA yet.

| 字段 | 值 |
| --- | --- |
| Issue | [#40693](https://github.com/vllm-project/vllm/issues/40693) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ValueError: Gemma4ForConditionalGeneration does not support LoRA yet.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I made lora fine tuning of gemma-4-E4B-it through unsloth, and tried to start gemma-4-E4B-it and fine tuning model with vllm0.19.1, but I got ValueError: Gemma4ForConditionalGeneration does not support LoRA yet. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: ValueError: Gemma4ForConditionalGeneration does not support LoRA yet. bug ### Your current environment ### 🐛 Describe the bug I made lora fine tuning of gemma-4-E4B-it through unsloth, and tried to start gemma-4-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: et. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 🐛 Describe the bug I made lora fine tuning of gemma-4-E4B-it through unsloth, and tried to start gemma-4-E4B-it and fine tuning model with vllm0.19.1, but I got ValueError: Gemma4ForConditionalGeneration does not suppor...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: ValueError: Gemma4ForConditionalGeneration does not support LoRA yet. bug ### Your current environment ### 🐛 Describe the bug I made lora fine tuning of gemma-4-E4B-it through unsloth, and tried to start gemma-4-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
