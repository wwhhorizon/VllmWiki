# vllm-project/vllm#11765: [Misc]:  Finetuned llama3.2 vision instruct model is failing during VLLM weight_loader

| 字段 | 值 |
| --- | --- |
| Issue | [#11765](https://github.com/vllm-project/vllm/issues/11765) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;gemm_linear;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization |
| 症状 | crash;oom;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Misc]:  Finetuned llama3.2 vision instruct model is failing during VLLM weight_loader

### Issue 正文摘录

### Anything you want to discuss about vllm. Hi I finetuned llama3.2 vision instruct model with below config using unsloth. However when I start the model in vllm it fails in weights shape assertion Underlying system supports bfloat16 and GPU is NVIDIA L4 Tensor Core Highly appreciate if somebody please guide me on exactly where I am getting it wrong? I checked in unsloth community also and it seems vllm may have the root cause. ## Finetuning Config in Unsloth ``` model, tokenizer = FastVisionModel.from_pretrained( "unsloth/Llama-3.2-11B-Vision-Instruct", load_in_4bit = True, # Use 4bit to reduce memory use. False for 16bit LoRA. use_gradient_checkpointing = "unsloth", # True or "unsloth" for long context ) model = FastVisionModel.get_peft_model( model, finetune_vision_layers = True, # False if not finetuning vision layers finetune_language_layers = True, # False if not finetuning language layers finetune_attention_modules = True, # False if not finetuning attention layers finetune_mlp_modules = True, # False if not finetuning MLP layers r = 16, # The larger, the higher the accuracy, but might overfit lora_alpha = 16, # Recommended alpha == r at least lora_dropout = 0, bias = "non...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: uned llama3.2 vision instruct model is failing during VLLM weight_loader stale ### Anything you want to discuss about vllm. Hi I finetuned llama3.2 vision instruct model with below config using unsloth. However when I s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: system supports bfloat16 and GPU is NVIDIA L4 Tensor Core Highly appreciate if somebody please guide me on exactly where I am getting it wrong? I checked in unsloth community also and it seems vllm may have the root cau...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: in vllm it fails in weights shape assertion Underlying system supports bfloat16 and GPU is NVIDIA L4 Tensor Core Highly appreciate if somebody please guide me on exactly where I am getting it wrong? I checked in unsloth...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Misc]: Finetuned llama3.2 vision instruct model is failing during VLLM weight_loader stale ### Anything you want to discuss about vllm. Hi I finetuned llama3.2 vision instruct model with below config using unsloth. How...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: i I finetuned llama3.2 vision instruct model with below config using unsloth. However when I start the model in vllm it fails in weights shape assertion Underlying system supports bfloat16 and GPU is NVIDIA L4 Tensor Co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
