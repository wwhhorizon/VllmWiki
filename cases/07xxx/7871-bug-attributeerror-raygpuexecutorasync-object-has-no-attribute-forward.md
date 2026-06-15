# vllm-project/vllm#7871: [Bug]: AttributeError: 'RayGPUExecutorAsync' object has no attribute 'forward_dag'

| 字段 | 值 |
| --- | --- |
| Issue | [#7871](https://github.com/vllm-project/vllm/issues/7871) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'RayGPUExecutorAsync' object has no attribute 'forward_dag'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I want to accomplish distributed inference in containers deployed on two different machines via vllm and NCCL. These containers are from one image. Here is the startup command on the head node: `python -m vllm.entrypoints.openai.api_server --model /root/vllm/models/Qwen1.5-1.8B-Chat --served-model-name qwen --host 0.0.0.0 --port $API_PORT --tensor-parallel-size 4`. Through `ray status`, I ensured that the containers have 4 available GPUs. And the errors are as follows: ``` INFO 08-26 19:08:13 api_server.py:219] vLLM API server version 0.5.3 INFO 08-26 19:08:13 api_server.py:220] args: Namespace(host='0.0.0.0', port=3456, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], model='/root/vllm/models/Qwen1.5-1.8B-Chat', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=Fal...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: teError: 'RayGPUExecutorAsync' object has no attribute 'forward_dag' bug;stale ### Your current environment ### 🐛 Describe the bug I want to accomplish distributed inference in containers deployed on two different machi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: nd on the head node: `python -m vllm.entrypoints.openai.api_server --model /root/vllm/models/Qwen1.5-1.8B-Chat --served-model-name qwen --host 0.0.0.0 --port $API_PORT --tensor-parallel-size 4`. Through `ray status`, I...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: e as follows: ``` INFO 08-26 19:08:13 api_server.py:219] vLLM API server version 0.5.3 INFO 08-26 19:08:13 api_server.py:220] args: Namespace(host='0.0.0.0', port=3456, uvicorn_log_level='info', allow_credentials=False,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='outlines', distributed_executor_ba...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: host='0.0.0.0', port=3456, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
