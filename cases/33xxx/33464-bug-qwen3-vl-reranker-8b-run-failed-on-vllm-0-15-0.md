# vllm-project/vllm#33464: [Bug]: qwen3-vl-reranker-8b run failed on VLLM 0.15.0

| 字段 | 值 |
| --- | --- |
| Issue | [#33464](https://github.com/vllm-project/vllm/issues/33464) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | runtime_err |
| Operator 关键词 | attention;cuda;operator;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: qwen3-vl-reranker-8b run failed on VLLM 0.15.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash vllm serve Qwen/Qwen3-VL-Reranker-8B --runner pooling --hf_overrides '{"architectures": ["Qwen3VLForSequenceClassification"],"classifier_from_token": ["no", "yes"],"is_original_qwen3_reranker": true}' ``` ```log (APIServer pid=2274224) INFO 01-31 12:57:20 [utils.py:325] (APIServer pid=2274224) INFO 01-31 12:57:20 [utils.py:325] █ █ █▄ ▄█ (APIServer pid=2274224) INFO 01-31 12:57:20 [utils.py:325] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.15.0 (APIServer pid=2274224) INFO 01-31 12:57:20 [utils.py:325] █▄█▀ █ █ █ █ model Qwen/Qwen3-VL-Reranker-8B (APIServer pid=2274224) INFO 01-31 12:57:20 [utils.py:325] ▀▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀ ▀ (APIServer pid=2274224) INFO 01-31 12:57:20 [utils.py:325] (APIServer pid=2274224) INFO 01-31 12:57:20 [utils.py:261] non-default args: {'model_tag': 'Qwen/Qwen3-VL-Reranker-8B', 'api_server_count': 1, 'model': 'Qwen/Qwen3-VL-Reranker-8B', 'runner': 'pooling', 'hf_overrides': {'architectures': ['Qwen3VLForSequenceClassification'], 'classifier_from_token': ['no', 'yes'], 'is_original_qwen3_reranker': True}} (APIServer pid=2274224) INFO 01-31 12:57:39 [model.py:871] Resolved `--convert auto` to `--convert classify`. Pass...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: qwen3-vl-reranker-8b run failed on VLLM 0.15.0 bug ### Your current environment ### 🐛 Describe the bug ```bash vllm serve Qwen/Qwen3-VL-Reranker-8B --runner pooling --hf_overrides '{"architectures": ["Qwen3VLForS...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: =2274224) INFO 01-31 12:57:20 [utils.py:325] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.15.0 (APIServer pid=2274224) INFO 01-31 12:57:20 [utils.py:325] █▄█▀ █ █ █ █ model Qwen/Qwen3-VL-Reranker-8B (APIServer pid=2274224) INFO 01-31 12...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=262144, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_siz...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: vllm serve Qwen/Qwen3-VL-Reranker-8B --runner pooling --hf_overrides '{"architectures": ["Qwen3VLForSequenceClassification"],"classifier_from_token": ["no", "yes"],"is_original_qwen3_reranker": true}' ``` ```log (APISer...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
