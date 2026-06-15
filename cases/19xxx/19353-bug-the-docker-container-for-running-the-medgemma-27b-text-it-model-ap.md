# vllm-project/vllm#19353: [Bug]: The Docker container for running the MedGemma-27b-text-it model appears to be hung during startup.

| 字段 | 值 |
| --- | --- |
| Issue | [#19353](https://github.com/vllm-project/vllm/issues/19353) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The Docker container for running the MedGemma-27b-text-it model appears to be hung during startup.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug docker image: vllm/vllm-openai:v0.9.0.1 docker command: --model /models/medgemma-27b-text-it --served-model-name medgemma-27b-text-it --tensor-parallel-size 2 --enforce-eager --max-model-len 4096 docker logs stuck here : docker logs -f c-medgemma2 ``` INFO 06-09 16:01:05 [__init__.py:243] Automatically detected platform cuda. INFO 06-09 16:01:08 [__init__.py:31] Available plugins for group vllm.general_plugins: INFO 06-09 16:01:08 [__init__.py:33] - lora_filesystem_resolver -> vllm.plugins.lora_resolvers.filesystem_resolver:register_filesystem_resolver INFO 06-09 16:01:08 [__init__.py:36] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load. INFO 06-09 16:01:08 [api_server.py:1289] vLLM API server version 0.9.0.1 INFO 06-09 16:01:08 [cli_args.py:300] non-default args: {'model': '/models/medgemma-27b-text-it', 'max_model_len': 4096, 'enforce_eager': True, 'served_model_name': ['medgemma-27b-text-it'], 'tensor_parallel_size': 2} INFO 06-09 16:01:14 [config.py:793] This model supports multiple tasks: {'embed', 'reward', 'score', 'generate', 'classify'}. Defaulting to 'generate'. INFO 06-09 16...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: The Docker container for running the MedGemma-27b-text-it model appears to be hung during startup. bug ### Your current environment ### 🐛 Describe the bug docker image: vllm/vllm-openai:v0.9.0.1 docker command: -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: p for distributed inference INFO 06-09 16:01:14 [config.py:2118] Chunked prefill is enabled with max_num_batched_tokens=2048. WARNING 06-09 16:01:14 [cuda.py:87] To see benefits of async output processing, enable CUDA g...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=2, pipeline_parallel_size=1, disable_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: The Docker container for running the MedGemma-27b-text-it model appears to be hung during startup. bug ### Your current environment ### 🐛 Describe the bug docker image: vllm/vllm-openai:v0.9.0.1 docker command: -...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
