# vllm-project/vllm#8808: [New Model]: allenai/Molmo-7B-0-0924 VisionLM

| 字段 | 值 |
| --- | --- |
| Issue | [#8808](https://github.com/vllm-project/vllm/issues/8808) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: allenai/Molmo-7B-0-0924 VisionLM

### Issue 正文摘录

### The model to consider. https://huggingface.co/allenai/Molmo-7B-O-0924 https://huggingface.co/collections/allenai/molmo-66f379e6fe3b8ef090a8ca19 ### The closest model vllm already supports. Existing Olmo Models by AllenAi: `OLMoForCausalLM` and `OLMoEForCausalLM` are supported. ### What's your difficulty of supporting the model you want? Molmo is a vision LM, so unlike the previous Olmo models by Allen AI, this model includes vision. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: allenai/Molmo-7B-0-0924 VisionLM new-model ### The model to consider. https://huggingface.co/allenai/Molmo-7B-O-0924 https://huggingface.co/collections/allenai/molmo-66f379e6fe3b8ef090a8ca19 ### The closest...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ady supports. Existing Olmo Models by AllenAi: `OLMoForCausalLM` and `OLMoEForCausalLM` are supported. ### What's your difficulty of supporting the model you want? Molmo is a vision LM, so unlike the previous Olmo model...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
