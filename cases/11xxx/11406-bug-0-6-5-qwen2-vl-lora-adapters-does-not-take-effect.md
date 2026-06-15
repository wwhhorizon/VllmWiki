# vllm-project/vllm#11406: [Bug]: [0.6.5] Qwen2-VL LoRA Adapters  does not take effect.

| 字段 | 值 |
| --- | --- |
| Issue | [#11406](https://github.com/vllm-project/vllm/issues/11406) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm |
| 子分类 | env_compat |
| Operator 关键词 | cuda;gemm;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [0.6.5] Qwen2-VL LoRA Adapters  does not take effect.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hi, there. I have finetuned Qwen2-VL-7B-Instruct with LLaMA-Factory in two different tasks and got two lora weights(named lora1 and lora2). However, when I start an server with base model and these two lora adapters, just follow the document(https://docs.vllm.ai/en/latest/usage/lora.html), I found that no matter which lora model I request for, the response just as same as the base model. As I print the details in https://github.com/vllm-project/vllm/blob/29c748930e0d35a98351a8cf8a093fba4b758114/vllm/lora/models.py#L368， I found register modules are named with "language_model.model.layers.XXX" (maybe same as base model), however, the loaded weights of lora adapters are named with "model.layers.XXX"(processed by function `parse_fine_tuned_lora_name`). The difference makes `module_lora=None` and the foward process does not pass through the lora module. I have not met with the same problem with 0.6.4post1, and I wonder if I misunderstand the usage in new version. `python3 -m vllm.entrypoints.openai.api_server --model $MODEL --served-model-name $SERVED_MODEL_NAME --enable-lora --lora-modules $LORA_M...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: [0.6.5] Qwen2-VL LoRA Adapters does not take effect. bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hi, there. I have finetuned Qwen2-VL-7B-Instruct with LLaMA-Factory...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: roblem with 0.6.4post1, and I wonder if I misunderstand the usage in new version. `python3 -m vllm.entrypoints.openai.api_server --model $MODEL --served-model-name $SERVED_MODEL_NAME --enable-lora --lora-modules $LORA_M...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: "allow_logprobs": true, "allow_search_indices": false, "allow_view": true, "allow_fine_tuning": false, "organization": "*", "group": null, "is_blocking":
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: "created": 1734852933, "allow_create_engine": false, "allow_sampling": true, "allow_logprobs": true, "allow_search_indices": false, "allow_view": true, "allow_fine_tuni
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: end_api;hardware_porting;model_support;multimodal_vlm cuda;gemm;operator;triton build_error dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
