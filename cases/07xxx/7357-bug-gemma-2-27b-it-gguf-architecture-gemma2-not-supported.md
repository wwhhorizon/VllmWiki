# vllm-project/vllm#7357: [Bug]: `gemma-2-27b-it-GGUF`: `Architecture gemma2 not supported`

| 字段 | 值 |
| --- | --- |
| Issue | [#7357](https://github.com/vllm-project/vllm/issues/7357) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `gemma-2-27b-it-GGUF`: `Architecture gemma2 not supported`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm trying to run openai compatible server for `bartowski/gemma-2-27b-it-GGUF` with a nightly `vllm` build (downloaded about an hour ago, should be b4e9528f9569d6eb8c29624771a4058fe794cb5a I think), and getting a `ValueError: Architecture gemma2 not supported` error: ``` $ VLLM_ATTENTION_BACKEND=FLASHINFER CUDA_DEVICE_ORDER=PCI_BUS_ID CUDA_VISIBLE_DEVICES=0,1,2,3 /opt/vllm/venv/bin/python -m vllm.entrypoints.openai.api_server --port=5003 --host=0.0.0.0 --model gemma-2-27b-it-Q8_0.gguf --tokenizer google/gemma-2-27b-it --seed 1234 --tensor-parallel-size=4 INFO 08-09 16:17:48 api_server.py:352] vLLM API server version 0.5.4 INFO 08-09 16:17:48 api_server.py:353] args: Namespace(host='0.0.0.0', port=5003, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, model='gemma-2-27b-it-Q8_0.gguf', t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: patible server for `bartowski/gemma-2-27b-it-GGUF` with a nightly `vllm` build (downloaded about an hour ago, should be b4e9528f9569d6eb8c29624771a4058fe794cb5a I think), and getting a `ValueError: Architecture gemma2 n...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: `gemma-2-27b-it-GGUF`: `Architecture gemma2 not supported` bug ### Your current environment ### 🐛 Describe the bug I'm trying to run openai compatible server for `bartowski/gemma-2-27b-it-GGUF` with a nightly `vl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: False, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, num_speculative_tokens=None, speculative_draft_tensor_parallel_si...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ueError: Architecture gemma2 not supported` error: ``` $ VLLM_ATTENTION_BACKEND=FLASHINFER CUDA_DEVICE_ORDER=PCI_BUS_ID CUDA_VISIBLE_DEVICES=0,1,2,3 /opt/vllm/venv/bin/python -m vllm.entrypoints.openai.api_server --port...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: host='0.0.0.0', port=5003, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
