# vllm-project/vllm#25659: [Usage]: Qwen3-Reranker with ragflow have error

| 字段 | 值 |
| --- | --- |
| Issue | [#25659](https://github.com/vllm-project/vllm/issues/25659) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Qwen3-Reranker with ragflow have error

### Issue 正文摘录

### Your current environment Qwen3-Reranker with ragflow have error ``` vllm-openai-8002: runtime: nvidia # 只使用 gpu 1 deploy: resources: reservations: devices: - device_ids: ["1"] capabilities: ["gpu"] driver: "nvidia" environment: - CUDA_VISIBLE_DEVICES=1 # command: --model /models/safetensors/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 --served-model-name Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 --gpu-memory-utilization 0.75 --kv-cache-dtype fp8 --max_model_len 61440 --max-num-batched-tokens 61440 command: > --model /models/safetensors/Qwen/Qwen3-Reranker-4B --served-model-name Qwen/Qwen3-Reranker-4B --gpu-memory-utilization 0.7 --hf_overrides '{"architectures":["Qwen3ForSequenceClassification"],"classifier_from_token": ["no", "yes"],"is_original_qwen3_reranker": true}' volumes: - ./models/.cache/huggingface:/root/.cache/huggingface - ./models/safetensors:/models/safetensors dns: - 8.8.8.8 ports: - 8002:8000 ipc: host image: vllm/vllm-openai:v0.10.1.1 ``` ``` (APIServer pid=1) WARNING 09-25 01:41:57 [protocol.py:81] The following fields were present in the request but ignored: {'return_documents'} (EngineCore_0 pid=268) ERROR 09-25 01:41:58 [dump_input.py:69] Dumping input data for V1 LL...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Usage]: Qwen3-Reranker with ragflow have error usage ### Your current environment Qwen3-Reranker with ragflow have error ``` vllm-openai-8002: runtime: nvidia # 只使用 gpu 1 deploy: resources: reservat
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: 09-25 01:41:57 [protocol.py:81] The following fields were present in the request but ignored: {'return_documents'} (EngineCore_0 pid=268) ERROR 09-25 01:41:58 [dump_input.py:69] Dumping input data for V1 LLM engine (v0....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: nd=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=Qwen/Qwen3-Reranker-4B, enable_prefix_caching=Tr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: # command: --model /models/safetensors/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 --served-model-name Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 --gpu-memory-utilization 0.75 --kv-cache-dtype fp8 --max_model_len 61440 --max-num-b...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: izer='/models/safetensors/Qwen/Qwen3-Reranker-4B', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_se...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
