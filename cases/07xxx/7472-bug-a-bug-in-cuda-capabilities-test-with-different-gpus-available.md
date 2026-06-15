# vllm-project/vllm#7472: [Bug]: a bug in CUDA capabilities test with different GPUs available

| 字段 | 值 |
| --- | --- |
| Issue | [#7472](https://github.com/vllm-project/vllm/issues/7472) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: a bug in CUDA capabilities test with different GPUs available

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug There's a bug in test for CUDA compute capability when running `vllm` with at least 2 CUDA GPUs with different capabilities, where the one with the greatest capability isn't the first one by PCI bus ID, like on such a system: ``` $ nvidia-smi --query-gpu=pci.bus_id,gpu_name --format=csv pci.bus_id, name 00000000:01:00.0, NVIDIA GeForce RTX 2060 00000000:07:00.0, NVIDIA GeForce RTX 4070 Ti ``` In this case the test for compute capabilities breaks, e.g., ``` $ VLLM_ATTENTION_BACKEND=FLASHINFER python -m vllm.entrypoints.openai.api_server --port=5003 --host=0.0.0.0 --model gemma-2-27b-it-Q2_K.gguf --tokenizer google/gemma-2-27b-it INFO 08-13 15:39:03 api_server.py:352] vLLM API server version 0.5.4 INFO 08-13 15:39:03 api_server.py:353] args: Namespace(host='0.0.0.0', port=5003, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False,...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='outlines', distributed_executor_ba...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: False, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, num_speculative_tokens=None, speculative_draft_tensor_parallel_si...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ties, where the one with the greatest capability isn't the first one by PCI bus ID, like on such a system: ``` $ nvidia-smi --query-gpu=pci.bus_id,gpu_name --format=csv pci.bus_id, name 00000000:01:00.0, NVIDIA GeForce...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: a bug in CUDA capabilities test with different GPUs available bug ### Your current environment ### 🐛 Describe the bug There's a bug in test for CUDA compute capability when running `vllm` with at least 2 CUDA GPU...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ke on such a system: ``` $ nvidia-smi --query-gpu=pci.bus_id,gpu_name --format=csv pci.bus_id, name 00000000:01:00.0, NVIDIA GeForce RTX 2060 00000000:07:00.0, NVIDIA GeForce RTX 4070 Ti ``` In this case the test for co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
