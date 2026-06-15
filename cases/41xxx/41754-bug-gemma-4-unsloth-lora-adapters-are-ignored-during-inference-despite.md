# vllm-project/vllm#41754: [Bug]: Gemma 4: Unsloth LoRA adapters are ignored during inference despite successful loading

| 字段 | 值 |
| --- | --- |
| Issue | [#41754](https://github.com/vllm-project/vllm/issues/41754) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Gemma 4: Unsloth LoRA adapters are ignored during inference despite successful loading

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Issue: Unsloth-trained Gemma 4 Adapters Ineffective in vLLM While the **bitsandbytes** compatibility for Gemma 4 has been addressed (see [PR #40321](https://github.com/vllm-project/vllm/pull/40321)), LoRA adapters trained via **Unsloth** (e.g., for the 31B model) currently fail to apply correctly in vLLM. **Observations:** * **Tested Hardware:** RTX 4090 and A6000 Pro. * **Behavior:** The engine loads without crashing, but the adapter is effectively ignored and has no impact on model output. * **Attempted Fixes:** Manual re-mapping of layers was attempted but did not resolve the issue, suggesting a deeper incompatibility in how the adapter weights are being addressed or integrated. Unsloth: ``` model.save_pretrained("model_temp") tokenizer.save_pretrained("model_temp") ``` vLLM: ``` outputs = llm.generate( prompts=conversations, sampling_params=sampling_params, lora_request=LoRARequest("adapter", 1, lora_path) ) ``` Adapter loading works fine for Gemma 3 / Mistral / Qwen. **I'm pretty sure it's a vLLM bug**, since it works fine with FastModel from unsloth. ### Before submitting a new issue... - [x] Make sure you already searc...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Gemma 4: Unsloth LoRA adapters are ignored during inference despite successful loading bug ### Your current environment ### 🐛 Describe the bug ### Issue: Unsloth-trained Gemma 4 Adapters Ineffective in vLLM While...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: to apply correctly in vLLM. **Observations:** * **Tested Hardware:** RTX 4090 and A6000 Pro. * **Behavior:** The engine loads without crashing, but the adapter is effectively ignored and has no impact on model output. *...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: Gemma 4: Unsloth LoRA adapters are ignored during inference despite successful loading bug ### Your current environment ### 🐛 Describe the bug ### Issue: Unsloth-trained Gemma 4 Adapters Ineffective in vLLM While...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: Gemma 4: Unsloth LoRA adapters are ignored during inference despite successful loading bug ### Your current environment ### 🐛 Describe the bug ### Issue: Unsloth-trained Gemma 4 Adapters Ineffective in vLLM While...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: pts=conversations, sampling_params=sampling_params, lora_request=LoRARequest("adapter", 1, lora_path) ) ``` Adapter loading works fine for Gemma 3 / Mistral / Qwen. **I'm pretty sure it's a vLLM bug**, since it works fi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
