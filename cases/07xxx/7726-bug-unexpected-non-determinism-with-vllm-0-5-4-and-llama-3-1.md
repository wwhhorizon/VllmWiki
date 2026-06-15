# vllm-project/vllm#7726: [Bug]: Unexpected non-determinism with vLLM 0.5.4 and Llama 3.1

| 字段 | 值 |
| --- | --- |
| Issue | [#7726](https://github.com/vllm-project/vllm/issues/7726) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;nondeterministic |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unexpected non-determinism with vLLM 0.5.4 and Llama 3.1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have observed frequent non-determinism using vLLM 0.5.4 in a single-GPU environment used to serve hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4. This is unexpected insofar that I have not seen this before with vLLM 0.5.1 serving casperhansen/llama-3-8b-instruct-awq. Here are the startup args: ``` Namespace(host='0.0.0.0', port=80, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, model='/opt/intrafind/.cache/huggingface/hub/models--hugging-quants--Meta-Llama-3.1-8B-Instruct-AWQ-INT4/snapshots/db1f81ad4b8c7e39777509fac66c652eb0a52f91', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_pat...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Unexpected non-determinism with vLLM 0.5.4 and Llama 3.1 bug ### Your current environment ### 🐛 Describe the bug I have observed frequent non-determinism using vLLM 0.5.4 in a single-GPU environment used to serve...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: False, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', scheduler_delay_factor=0.0, enable_chunked_prefill=False, speculative_model=None, num_speculative_tokens=None, speculative_draft_tensor_parallel_s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: e system and user prompts for readability): ``` Aug 21 09:21:46 hal9000 docker[370341]: INFO 08-21 07:21:46 logger.py:36] Received request chat-bb2c761150f14f60b7663c48bab70b95: prompt: ' system \n\nCutting Knowledge Da...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: lse, max_log_len=None) ``` Here are two identical requests that lead to different outputs (I have redacted out the system and user prompts for readability): ``` Aug 21 09:21:46 hal9000 docker[370341]: INFO 08-21 07:21:4...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: inism using vLLM 0.5.4 in a single-GPU environment used to serve hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4. This is unexpected insofar that I have not seen this before with vLLM 0.5.1 serving casperhansen/llama...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
