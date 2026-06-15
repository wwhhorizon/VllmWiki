# vllm-project/vllm#19139: [Bug]: Error when loading model(gemma-3-4b) merged after DeepSpeed training into vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#19139](https://github.com/vllm-project/vllm/issues/19139) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 |  |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error when loading model(gemma-3-4b) merged after DeepSpeed training into vLLM

### Issue 正文摘录

### Your current environment library versions - transformers==4.52.3 - vllm==0.9.0.1 ### 🐛 Describe the bug I encountered an error when trying to load a model into vLLM that was merged after training with DeepSpeed. The merging process was done using the following code, which produced pytorch_model.bin, config.json, etc. (I also saved the model using safetensors.) ```python state_dict = get_fp32_state_dict_from_zero_checkpoint(checkpoint_path) torch.save(state_dict, os.path.join(output_dir, "pytorch_model.bin")) ``` For merging, I used the checkpoint with the lowest validation loss as the best model. ![Image](https://github.com/user-attachments/assets/f399a187-9f6e-4601-87b2-5477f9a98830) There are no issues when using the original, untrained gemma-3-4b model: `python generate_answer_vllm.py --model_name gemma-3-4b --shot 0` However, when using the fine-tuned model: `python generate_answer_vllm.py --model_name gemma-3-4b --shot 0 --use_finetuned_model` ```python def load_model_and_tokenizer(model_name, use_finetuned_model, fintuned_path): model_path = fintuned_path if use_finetuned_model else MODEL_MAPPING[model_name] # vLLM 모델 로드 llm = LLM( model=model_path, tensor_parallel_size=...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: h config: model='data/outputs/gemma-3-4b_petqa_preprocessed/best_model', speculative_config=None, tokenizer='data/outputs/gemma-3-4b_petqa_preprocessed/best_model', skip_tokenizer_init=False, tokenizer_mode=auto, revisi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='xgrammar', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: tensor_parallel_size=2, trust_remote_code=True, dtype=torch.bfloat16, gpu_memory_utilization=0.9, ) tokenizer = AutoTokenizer.from_pretrained(model_path) if tokenizer.pad_token_id is None: tokenizer.pad_token_id = token...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Error when loading model(gemma-3-4b) merged after DeepSpeed training into vLLM bug ### Your current environment library versions - transformers==4.52.3 - vllm==0.9.0.1 ### 🐛 Describe the bug I encountered an erro...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: er DeepSpeed training into vLLM bug ### Your current environment library versions - transformers==4.52.3 - vllm==0.9.0.1 ### 🐛 Describe the bug I encountered an error when trying to load a model into vLLM that was merge...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
