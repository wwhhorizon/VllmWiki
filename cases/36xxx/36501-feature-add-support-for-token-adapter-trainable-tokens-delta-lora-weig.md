# vllm-project/vllm#36501: [Feature]: Add support for token_adapter.trainable_tokens_delta LoRA weight

| 字段 | 值 |
| --- | --- |
| Issue | [#36501](https://github.com/vllm-project/vllm/issues/36501) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add support for token_adapter.trainable_tokens_delta LoRA weight

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I have gotten good results in transformers training an adapter on custom tokens using the https://huggingface.co/docs/peft/developer_guides/lora#efficiently-train-tokens-alongside-lora method. However, when I go to use those adapters in vLLM, I get the message: ``` ValueError: Call to add_lora method failed: base_model.model.language_model.model.embed_tokens.token_adapter.trainable_tokens_delta is unsupported LoRA weight ``` My LoraConfig is below and I'm training on Qwen3-VL-4B-Instruct. ``` peft_config = LoraConfig( r=64, lora_alpha=128, target_modules=[ "q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj", ], ensure_weight_tying=True, trainable_token_indices={"embed_tokens": new_token_indices}, lora_dropout=0.05, bias="none", task_type="CAUSAL_LM", ) ``` I'm adding fewer than 10 new tokens, so not only does this give me much better results than training the entire embedding module, the resulting adapter is less than quarter of the size. Is this something that can be added as a supported layer type? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sur...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: in transformers training an adapter on custom tokens using the https://huggingface.co/docs/peft/developer_guides/lora#efficiently-train-tokens-alongside-lora method. However, when I go to use those adapters in vLLM, I g...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ns using the https://huggingface.co/docs/peft/developer_guides/lora#efficiently-train-tokens-alongside-lora method. However, when I go to use those adapters in vLLM, I get the message: ``` ValueError: Call to add_lora m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Add support for token_adapter.trainable_tokens_delta LoRA weight feature request ### 🚀 The feature, motivation and pitch I have gotten good results in transformers training an adapter on custom tokens using the https://...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
