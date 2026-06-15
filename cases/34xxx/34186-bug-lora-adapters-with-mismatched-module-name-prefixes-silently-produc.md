# vllm-project/vllm#34186: [Bug]: LoRA adapters with mismatched module name prefixes silently produce base-model output

| 字段 | 值 |
| --- | --- |
| Issue | [#34186](https://github.com/vllm-project/vllm/issues/34186) |
| 状态 | open |
| 标签 | unstale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | wrong_output |
| Operator 关键词 | cuda;operator |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LoRA adapters with mismatched module name prefixes silently produce base-model output

### Issue 正文摘录

## Your current environment ## Describe the bug **LoRA adapters whose weight keys have a different module name prefix than what the model expects are loaded without any error or warning, but silently produce output identical to the base model.** The adapter weights are stored in memory under incorrect keys and never applied at inference time. This is a follow-up to https://github.com/vllm-project/vllm/issues/12106 where a user reported "Incompatible lora modules should raise error, instead of silently getting ignored" — this issue provides the root cause analysis and a minimal reproduction. ### Concrete example [stewy33's SDF LoRA adapters](https://huggingface.co/stewy33/gemma-3-4b-it-0524_rowan_original_prompt_augmented_egregious_cake_bake-bd093845) for `google/gemma-3-4b-it` were trained against `GemmaForCausalLM`, so their weight keys use: ``` base_model.model.model.layers.0.self_attn.q_proj.lora_A.weight ``` But vLLM loads Gemma 3 as `Gemma3ForConditionalGeneration`, which wraps the LM in a `language_model` submodule. The model's actual module paths are: ``` language_model.model.layers.0.self_attn.q_proj ``` The adapter loads "successfully" — no error, no warning — but output...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: "}], "max_tokens": 50, "temperature": 0, "seed": 42 }' | python3 -c "import sys,json; print(json.load(sys.stdin)['choices'][0]['message']['content'])" # Adapter (should differ if LoRA is applied — this adapter was train...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: LoRA adapters with mismatched module name prefixes silently produce base-model output unstale ## Your current environment ## Describe the bug **LoRA adapters whose weight keys have a different module name prefix than wh...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: LoRA adapters with mismatched module name prefixes silently produce base-model output unstale ## Your current environment ## Describe the bug **LoRA adapters whose weight keys have a different module name prefix...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: LoRA adapters with mismatched module name prefixes silently produce base-model output unstale ## Your current environment ## Describe the bug **LoRA adapters whose weight keys have a different module name prefix...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: **: Both outputs are byte-for-byte identical. The adapter is loaded into GPU memory but never used. For comparison, [maius/gemma-3-4b-it-personas](https://huggingface.co/maius/gemma-3-4b-it-personas) persona adapters fo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
