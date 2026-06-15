# vllm-project/vllm#27962: [Bug]: Deploying Qwen3-VL on LoRa

| 字段 | 值 |
| --- | --- |
| Issue | [#27962](https://github.com/vllm-project/vllm/issues/27962) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Deploying Qwen3-VL on LoRa

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=0,1 vllm serve //Qwen3-VL-32B-Instruct/ --tensor-parallel-size=2 --trust-remote-code --max-model-len=4096 --dtype bfloat16 --gpu-memory-utilization 0.96 --port 8005 --served-model-name Qwen32b --enable-lora --max-lora-rank 64 INFO 11-03 05:51:41 [__init__.py:216] Automatically detected platform cuda. WARNING 11-03 05:51:44 [api_server.py:1213] LoRA dynamic loading & unloading is enabled in the API server. This should ONLY be used for local development! (APIServer pid=5385) INFO 11-03 05:51:44 [api_server.py:1839] vLLM API server version 0.11.0 (APIServer pid=5385) INFO 11-03 05:51:44 [utils.py:233] non-default args: {'model_tag': '/supconit-data/public_model/Qwen3-VL-4B-Instruct/', 'port': 8005, 'model': '/supconit-data/public_model/Qwen3-VL-4B-Instruct/', 'trust_remote_code': True, 'dtype': 'bfloat16', 'max_model_len': 4096, 'served_model_name': ['Qwen32b'], 'tensor_parallel_size': 2, 'gpu_memory_utilization': 0.96, 'enable_lora': True, 'max_lora_rank': 64} (APIServer pid=5385) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. (APIServer pid=5385) INFO 11...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_con...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: erver pid=5385) INFO 11-03 05:51:44 [api_server.py:1839] vLLM API server version 0.11.0 (APIServer pid=5385) INFO 11-03 05:51:44 [utils.py:233] non-default args: {'model_tag': '/supconit-data/public_model/Qwen3-VL-4B-In...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Deploying Qwen3-VL on LoRa bug ### Your current environment ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=0,1 vllm serve //Qwen3-VL-32B-Instruct/ --tensor-parallel-size=2 --trust-remote-code --max-model-len=4096 --...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: 1510] Using max model len 4096 (APIServer pid=5385) INFO 11-03 05:51:44 [scheduler.py:205] Chunked prefill is enabled with max_num_batched_tokens=8192. (APIServer pid=5385) WARNING 11-03 05:51:44 [lora.py:92] `lora_extr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: --tensor-parallel-size=2 --trust-remote-code --max-model-len=4096 --dtype bfloat16 --gpu-memory-utilization 0.96 --port 8005 --served-model-name Qwen32b --enable-lora --max-lora-rank 64 INFO 11-03 05:51:41 [__init__.py:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
