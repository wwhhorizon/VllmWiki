# vllm-project/vllm#19424: [Bug]: InternVL3 FP8 missing module/parameter on model load

| 字段 | 值 |
| --- | --- |
| Issue | [#19424](https://github.com/vllm-project/vllm/issues/19424) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;quantization;sampling |
| 症状 | crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: InternVL3 FP8 missing module/parameter on model load

### Issue 正文摘录

### Your current environment ### vLLM environment - v0.9.0.1 - docker environment: vllm/vllm-openai:v0.9.0.1 - on host: NVIDIA-SMI 570.133.20, Driver Version: 570.133.20, CUDA Version: 12.8 - CUDA : NVIDIA RTX 6000 ADA (Lovelace) - run via: `serve JustJaro/InternVL3-38B-FP8-Dynamic --config config.yaml` ### config.yaml _additional config commented out after attempts also failed_ ### 🐛 Describe the bug ### Error while attempting to run InternVL3-38B-FP8 **huggingface link**: https://huggingface.co/JustJaro/InternVL3-38B-FP8-Dynamic ### Primary Error: There is no module or parameter named 'mlp1.1.weight_scale' in InternVLChatModel Error using V1 Engine: ``` INFO 06-10 06:36:54 [api_server.py:1289] vLLM API server version 0.9.0.1 INFO 06-10 06:36:54 [cli_args.py:300] non-default args: {'api_key': *REDACTED*, 'enable_auto_tool_choice': True, 'tool_call_parser': 'hermes', 'trust_remote_code': True, 'max_model_len': 20000, 'served_model_name': ['internvl3-38b-fp8'], 'gpu_memory_utilization': 0.95, 'device': 'cuda', 'disable_log_requests': True, 'enable_server_load_tracking': True} INFO 06-10 06:37:04 [config.py:793] This model supports multiple tasks: {'embed', 'reward', 'generate', 'sc...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ug;stale ### Your current environment ### vLLM environment - v0.9.0.1 - docker environment: vllm/vllm-openai:v0.9.0.1 - on host: NVIDIA-SMI 570.133.20, Driver Version: 570.133.20, CUDA Version: 12.8 - CUDA : NVIDIA RTX...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: InternVL3 FP8 missing module/parameter on model load bug;stale ### Your current environment ### vLLM environment - v0.9.0.1 - docker environment: vllm/vllm-openai:v0.9.0.1 - on host: NVIDIA-SMI 570.133.20, Driver...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: InternVL3 FP8 missing module/parameter on model load bug;stale ### Your current environment ### vLLM environment - v0.9.0.1 - docker environment: vllm/vllm-openai:v0.9.0.1 - on host: NVIDIA-SMI 570.133.20, Driver...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: InternVL3 FP8 missing module/parameter on model load bug;stale ### Your current environment ### vLLM environment - v0.9.0.1 - docker environment: vllm/vllm-openai:v0.9.0.1 - on host: NVIDIA-SMI 570.133.20, Driver...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
