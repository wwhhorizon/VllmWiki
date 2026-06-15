# vllm-project/vllm#8406: [Bug]: Qwen2-VL GPTQ does not work

| 字段 | 值 |
| --- | --- |
| Issue | [#8406](https://github.com/vllm-project/vllm/issues/8406) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: Qwen2-VL GPTQ does not work

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug With the latest release vllm-0.6.1 installed, start the service to run [Qwen2-VL-7B-Instruct-GPTQ-Int8](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct-GPTQ-Int8): ```shell $ vllm serve /models/Qwen2-VL-7B-Instruct-GPTQ-Int8 --dtype half INFO 09-12 09:34:47 api_server.py:495] vLLM API server version 0.6.1 INFO 09-12 09:34:47 api_server.py:496] args: Namespace(model_tag='/models/Qwen2-VL-7B-Instruct-GPTQ-Int8', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_auto_tool_choice=False, tool_call_parser=None, model='/models/Qwen2-VL-7B-Instruct-GPTQ-Int8', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, download_d...

## 现有链接修复摘要

#8442 [Misc] Skip loading extra bias for Qwen2-VL GPTQ-Int8

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: No response_ ### 🐛 Describe the bug With the latest release vllm-0.6.1 installed, start the service to run [Qwen2-VL-7B-Instruct-GPTQ-Int8](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct-GPTQ-Int8): ```shell $ vllm se...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen2-VL GPTQ does not work bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug With the latest release vllm-0.6.1 installed, start the service to run [Qwen2-VL-7B-Instruct-
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: e, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_model_quantization=None, num_specu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: uto', quantization_param_path=None, max_model_len=16384, guided_decoding_backend='outlines', distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loadin...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Q-Int8): ```shell $ vllm serve /models/Qwen2-VL-7B-Instruct-GPTQ-Int8 --dtype half INFO 09-12 09:34:47 api_server.py:495] vLLM API server version 0.6.1 INFO 09-12 09:34:47 api_server.py:496] args: Namespace(model_tag='/...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#8442](https://github.com/vllm-project/vllm/pull/8442) | closes_keyword | 0.95 | [Misc] Skip loading extra bias for Qwen2-VL GPTQ-Int8 | FIX #8406 ping @DarkLight1337 **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside this <details> secti |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
