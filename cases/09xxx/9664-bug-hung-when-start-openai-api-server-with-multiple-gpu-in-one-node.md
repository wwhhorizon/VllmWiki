# vllm-project/vllm#9664: [Bug]: hung when start openai api server with multiple gpu in one node.

| 字段 | 值 |
| --- | --- |
| Issue | [#9664](https://github.com/vllm-project/vllm/issues/9664) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: hung when start openai api server with multiple gpu in one node.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug server hung (RTX 6000 ADA x 2): (heliumos-env) root@a185c0e318fb:~# vllm serve /models/Llama-3.1-70B-Instruct-AWQ-INT4 --served-model-name helium --max-model-len 32768 --max-num-seqs 16 --gpu-memory-utilization 0.95 --seed 20240915 --disable-log-requests --tensor-parallel-size 2 --enable-prefix-caching --host 0.0.0.0 --port 8000 --num-scheduler-steps 8 INFO 10-24 15:18:24 api_server.py:528] vLLM API server version 0.6.3.post1 INFO 10-24 15:18:24 api_server.py:529] args: Namespace(subparser='serve', model_tag='/models/Llama-3.1-70B-Instruct-AWQ-INT4', config='', host='0.0.0.0', port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/models/Llama-3.1-70B-Instruct-A...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: g]: hung when start openai api server with multiple gpu in one node. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug server hung (RTX 6000 ADA x 2): (heliumos-env) root@...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: scheduler-steps 8 INFO 10-24 15:18:24 api_server.py:528] vLLM API server version 0.6.3.post1 INFO 10-24 15:18:24 api_server.py:529] args: Namespace(subparser='serve', model_tag='/models/Llama-3.1-70B-Instruct-AWQ-INT4',...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: -env) root@a185c0e318fb:~# vllm serve /models/Llama-3.1-70B-Instruct-AWQ-INT4 --served-model-name helium --max-model-len 32768 --max-num-seqs 16 --gpu-memory-utilization 0.95 --seed 20240915 --disable-log-requests --ten...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: # Model Input Dumps _No response_ ### 🐛 Describe the bug server hung (RTX 6000 ADA x 2): (heliumos-env) root@a185c0e318fb:~# vllm serve /models/Llama-3.1-70B-Instruct-AWQ-INT4 --served-model-name helium --max-model-len...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: host='0.0.0.0', port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
