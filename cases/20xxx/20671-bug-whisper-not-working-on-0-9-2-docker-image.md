# vllm-project/vllm#20671: [Bug]: Whisper not working on 0.9.2 docker image

| 字段 | 值 |
| --- | --- |
| Issue | [#20671](https://github.com/vllm-project/vllm/issues/20671) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;operator;quantization |
| 症状 | build_error;crash;import_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Whisper not working on 0.9.2 docker image

### Issue 正文摘录

### Your current environment Docker image 0.9.2 on NVidia L40S. (The docker image has to be modified, because librosa dependency is missing.) ``` services: vllm-whisper-large-v3: # Must modify image for =0.10, 20 GB...) Log: ``` $ docker logs -f vllm-whisper-large-v3 INFO 07-09 02:08:41 [__init__.py:244] Automatically detected platform cuda. INFO 07-09 02:08:44 [api_server.py:1395] vLLM API server version 0.9.2 INFO 07-09 02:08:44 [cli_args.py:325] non-default args: {'port': 8006, 'model': 'openai/whisper-large-v3', 'gpu_memory_utilization': 0.4, 'swap_space': 5.0, 'disable_log_requests': True} INFO 07-09 02:08:49 [config.py:841] This model supports multiple tasks: {'generate', 'classify', 'reward', 'embed', 'transcription'}. Defaulting to 'transcription'. INFO 07-09 02:08:49 [config.py:1472] Using max model len 448 WARNING 07-09 02:08:49 [arg_utils.py:1735] ['WhisperForConditionalGeneration'] is not supported by the V1 Engine. Falling back to V0. INFO 07-09 02:08:50 [api_server.py:268] Started engine process with PID 266 INFO 07-09 02:08:53 [__init__.py:244] Automatically detected platform cuda. INFO 07-09 02:08:54 [llm_engine.py:230] Initializing a V0 LLM engine (v0.9.2) with co...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: Whisper not working on 0.9.2 docker image bug;stale ### Your current environment Docker image 0.9.2 on NVidia L40S. (The docker image has to be modified, because librosa dependency is missing.) ``` services: vllm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: INFO 07-09 02:08:44 [cli_args.py:325] non-default args: {'port': 8006, 'model': 'openai/whisper-large-v3', 'gpu_memory_utilization': 0.4, 'swap_space': 5.0, 'disable_log_requests': True} INFO 07-09 02:08:49 [config.py:8...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Whisper not working on 0.9.2 docker image bug;stale ### Your current environment Docker image 0.9.2 on NVidia L40S. (The docker image has to be modified, because librosa dependency is missing.) ``` services: vllm...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=448, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_cu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
