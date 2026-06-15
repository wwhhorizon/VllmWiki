# vllm-project/vllm#17755: [Bug]: KeyError: 'layers.11.shared_transformer.self_attn.qkv_proj.weight' for Zamba2 after finetuning

| 字段 | 值 |
| --- | --- |
| Issue | [#17755](https://github.com/vllm-project/vllm/issues/17755) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KeyError: 'layers.11.shared_transformer.self_attn.qkv_proj.weight' for Zamba2 after finetuning

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi team, I fine-tuned Zamba (`Zyphra/Zamba2-1.2B-instruct`) using standard HF `Trainer` and `TrainingArguments` (using `save_safetensors=False` as otherwise it is not saving and throwing a serialization error) and it saved the final checkpoint. When I tried to infer this fine-tuned model, it threw the following `KeyError: 'layers.11.shared_transformer.self_attn.qkv_proj.weight'` Relevant stack trace: ``` WARNING 05-07 02:08:07 [arg_utils.py:1658] ['Zamba2ForCausalLM'] is not supported by the V1 Engine. Falling back to V0. INFO 05-07 02:08:07 [llm_engine.py:240] Initializing a V0 LLM engine (v0.8.5.post1) with config: model='/mnt/batch/tasks/shared/LS_root/mounts/clusters/afge1/code//models/NOISY_Zamba2-1.2B-instruct_K_6_context_1024_maxlen_11_minlen_5_sft', speculative_config=None, tokenizer='/mnt/batch/tasks/shared/LS_root/mounts/clusters/afge1/code//models/NOISY_Zamba2-1.2B-instruct_K_6_context_1024_maxlen_11_minlen_5_sft', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_f...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: team, I fine-tuned Zamba (`Zyphra/Zamba2-1.2B-instruct`) using standard HF `Trainer` and `TrainingArguments` (using `save_safetensors=False` as otherwise it is not saving and throwing a serialization error) and it saved...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: d_transformer.self_attn.qkv_proj.weight' for Zamba2 after finetuning bug;stale ### Your current environment ### 🐛 Describe the bug Hi team, I fine-tuned Zamba (`Zyphra/Zamba2-1.2B-instruct`) using standard HF `Trainer`...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: uto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='auto', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect_mod...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
