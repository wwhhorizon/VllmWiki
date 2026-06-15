# vllm-project/vllm#5566: [Usage]: how to use marlin kernel for GPTQ model

| 字段 | 值 |
| --- | --- |
| Issue | [#5566](https://github.com/vllm-project/vllm/issues/5566) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to use marlin kernel for GPTQ model

### Issue 正文摘录

### How would you like to use vllm I want to run inference of a [TheBloke/Llama-2-7B-Chat-GPTQ](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GPTQ). I don't know how to use it with vllm. I try to use the api server. `python -m vllm.entrypoints.openai.api_server --disable-log-requests --model TheBloke/Llama-2-7B-Chat-GPTQ --quantization gptq_marlin --seed 0 ` But I get an error: $ python -m vllm.entrypoints.openai.api_server --disable-log-requests --model TheBloke/Llama-2-7B-Chat-GPTQ --quantization gptq_marlin --seed 0 INFO 06-15 00:04:48 api_server.py:177] vLLM API server version 0.5.0.post1 INFO 06-15 00:04:48 api_server.py:178] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], model='TheBloke/Llama-2-7B-Chat-GPTQ', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, download_dir=None, load_fo...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: how to use marlin kernel for GPTQ model usage;stale ### How would you like to use vllm I want to run inference of a [TheBloke/Llama-2-7B-Chat-GPTQ](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GPTQ). I don't...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Usage]: how to use marlin kernel for GPTQ model usage;stale ### How would you like to use vllm I want to run inference of a [TheBloke/Llama-2-7B-Chat-GPTQ](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GPTQ). I don't...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: pace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, chat_template=None, response_role='assi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: q_marlin --seed 0 INFO 06-15 00:04:48 api_server.py:177] vLLM API server version 0.5.0.post1 INFO 06-15 00:04:48 api_server.py:178] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: pi_server --disable-log-requests --model TheBloke/Llama-2-7B-Chat-GPTQ --quantization gptq_marlin --seed 0 ` But I get an error: $ python -m vllm.entrypoints.openai.api_server --disable-log-requests --model TheBloke/Lla...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
