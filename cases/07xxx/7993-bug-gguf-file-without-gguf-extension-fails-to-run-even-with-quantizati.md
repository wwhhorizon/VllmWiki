# vllm-project/vllm#7993: [Bug]: gguf file without .gguf extension fails to run, even with "--quantization gguf --load-format gguf" flags

| 字段 | 值 |
| --- | --- |
| Issue | [#7993](https://github.com/vllm-project/vllm/issues/7993) |
| 状态 | closed |
| 标签 | bug;good first issue |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gguf file without .gguf extension fails to run, even with "--quantization gguf --load-format gguf" flags

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running .gguf files without .gguf extension does not work... renaming these files with .gguf extension and running without any flags (just using "vllm serve granite-code:latest.gguf") works. Expected behaviour is that we don't require .gguf extension to run .gguf file. ``` $ vllm serve ~/.local/share/ramalama/models/ollama/granite-code:latest --quantization gguf --load-format gguf WARNING 08-29 11:56:16 _custom_ops.py:17] Failed to import from vllm._C with ImportError('libcuda.so.1: cannot open shared object file: No such file or directory') INFO 08-29 11:56:19 api_server.py:440] vLLM API server version 0.5.5 INFO 08-29 11:56:19 api_server.py:441] args: Namespace(model_tag='/home/curtine/.local/share/ramalama/models/ollama/granite-code:latest', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_fr...

## 现有链接修复摘要

#8056 [Core][Bugfix] Accept GGUF model without .gguf extension

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: e, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_model_quantization=None, num_specu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: f --load-format gguf WARNING 08-29 11:56:16 _custom_ops.py:17] Failed to import from vllm._C with ImportError('libcuda.so.1: cannot open shared object file: No such file or directory') INFO 08-29 11:56:19 api_server.py:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: hout .gguf extension fails to run, even with "--quantization gguf --load-format gguf" flags bug;good first issue ### Your current environment ### 🐛 Describe the bug Running .gguf files without .gguf extension does not w...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='outlines', distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loadin...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: st', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#8056](https://github.com/vllm-project/vllm/pull/8056) | closes_keyword | 0.95 | [Core][Bugfix] Accept GGUF model without .gguf extension | FIX #7993 (*link existing issues this PR will resolve*) - Use GGUF magic number instead of filename suffix to check if a file is a gguf model. **BEFORE SUBMITTING, PLEASE READ |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
