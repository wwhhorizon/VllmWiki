# vllm-project/vllm#39815: [Bug]: Gemma4 LoRA adapters zeroed out

| 字段 | 值 |
| --- | --- |
| Issue | [#39815](https://github.com/vllm-project/vllm/issues/39815) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Gemma4 LoRA adapters zeroed out

### Issue 正文摘录

### 🐛 Describe the bug Gemma4-style aliased module paths can cause LoRA activation to zero itself out in `LoRAModelManager`. The issue is not that aliasing exists. The issue is that LoRA module creation was registering the same physical module multiple times under different names. ## Root Cause This started after Gemma4 added the fast-prefill / YOCO split. That added `self_decoder` and `cross_decoder` wrappers, but those wrappers point back to the same decoder layers. So the same module can show up twice: ```text model.layers.0... model.self_decoder.decoder_layers.0... ``` My first fix was to remove remove_duplicate=False: ```self.model.named_modules()``` That seemed to fix it because the alias path disappeared. Only one path got registered, so LoRA activation could not load weights on one name and then reset the same module through another name. But that ended up being too broad. _create_lora_modules() is also where we keep the module names LoRA is allowed to match against. After Gemma4ForConditionalGeneration LoRA support was added, we need to keep those paths around because adapter names can map to things like: ``` language_model.model.layers... language_model.lm_head... ``` So...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Gemma4 LoRA adapters zeroed out bug ### 🐛 Describe the bug Gemma4-style aliased module paths can cause LoRA activation to zero itself out in `LoRAModelManager`. The issue is not that aliasing exists. The issue is...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ferent names. ## Root Cause This started after Gemma4 added the fast-prefill / YOCO split. That added `self_decoder` and `cross_decoder` wrappers, but those wrappers point back to the same decoder layers. So the same mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: .decoder_layers.0... ``` My first fix was to remove remove_duplicate=False: ```self.model.named_modules()``` That seemed to fix it because the alias path disappeared. Only one path got registered, so LoRA activation cou...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: Gemma4 LoRA adapters zeroed out bug ### 🐛 Describe the bug Gemma4-style aliased module paths can cause LoRA activation to zero itself out in `LoRAModelManager`. The issue is not that aliasing exists. The issue is...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
