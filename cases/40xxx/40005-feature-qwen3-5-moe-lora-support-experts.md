# vllm-project/vllm#40005: [Feature]: Qwen3.5-Moe LoRA Support (experts)

| 字段 | 值 |
| --- | --- |
| Issue | [#40005](https://github.com/vllm-project/vllm/issues/40005) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Qwen3.5-Moe LoRA Support (experts)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hello! The LoRA weights trained with megatron-swift for Qwen3.5-MoE cannot be loaded with vLLM, while Qwen3-MoE and Qwen3.5-Dense both work fine. The structure of the experts' LoRA between these two models is the same (except for shared_experts). We have provided weight examples here: https://modelscope.cn/models/huangjintao/test_vllm_qwen3_5_moe_lora Could the vLLM team please add support for this? ``` 00000 = 'base_model.model.model.language_model.layers.0.linear_attn.in_proj_a.lora_A.weight' 00001 = 'base_model.model.model.language_model.layers.0.linear_attn.in_proj_a.lora_B.weight' 00002 = 'base_model.model.model.language_model.layers.0.linear_attn.in_proj_b.lora_A.weight' 00003 = 'base_model.model.model.language_model.layers.0.linear_attn.in_proj_b.lora_B.weight' 00004 = 'base_model.model.model.language_model.layers.0.linear_attn.in_proj_qkv.lora_A.weight' 00005 = 'base_model.model.model.language_model.layers.0.linear_attn.in_proj_qkv.lora_B.weight' 00006 = 'base_model.model.model.language_model.layers.0.linear_attn.in_proj_z.lora_A.weight' 00007 = 'base_model.model.model.language_model.layers.0.linear_attn.in_proj_z.lora_B.weight' 0000...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Qwen3.5-Moe LoRA Support (experts) feature request ### 🚀 The feature, motivation and pitch Hello! The LoRA weights trained with megatron-swift for Qwen3.5-MoE cannot be loaded with vLLM, while Qwen3-MoE and Q...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Feature]: Qwen3.5-Moe LoRA Support (experts) feature request ### 🚀 The feature, motivation and pitch Hello! The LoRA weights trained with megatron-swift for Qwen3.5-MoE cannot be loaded with vLLM, while Qwen3-MoE and Q...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Qwen3.5-Moe LoRA Support (experts) feature request ### 🚀 The feature, motivation and pitch Hello! The LoRA weights trained with megatron-swift for Qwen3.5-MoE cannot be loaded with vLLM, while Qwen3-MoE and Q...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: provided weight examples here: https://modelscope.cn/models/huangjintao/test_vllm_qwen3_5_moe_lora Could the vLLM team please add support for this? ``` 00000 = 'base_model.model.model.language_model.layers.0.linear_attn...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
