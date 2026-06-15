# vllm-project/vllm#7294: [Bug]: ValueError: BitAndBytes with enforce_eager = False is not supported yet.

| 字段 | 值 |
| --- | --- |
| Issue | [#7294](https://github.com/vllm-project/vllm/issues/7294) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ValueError: BitAndBytes with enforce_eager = False is not supported yet.

### Issue 正文摘录

### Your current environment vLLM API server version 0.5.4 python 3.11.5 when i use vllm to doploy the model Mistral-Large-Instruct-2407-bnb-4bit,there is something wrong the model is from https://www.modelscope.cn/models/LLM-Research/Mistral-Large-Instruct-2407-bnb-4bit/files and files like tokenizer are from https://huggingface.co/mistralai/Mistral-Large-Instruct-2407/blob/main/config.json ### 🐛 Describe the bug /home/workspace/Mistral-Large-Instruct-2407-bnb-4bit$ CUDA_VISIBLE_DEVICES=1 python -m vllm.entrypoints.openai.api_server --model /home/workspace/Mistral-Large-Instruct-2407-bnb-4bit --served-model-name Mistral-Large-Instruct-2407-bnb-4bit --gpu-memory-utilization .6 --host 192.168.0.109 --port 8006 INFO 08-08 14:21:38 api_server.py:339] vLLM API server version 0.5.4 INFO 08-08 14:21:38 api_server.py:340] args: Namespace(host='192.168.0.109', port=8006, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: False, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, num_speculative_tokens=None, speculative_draft_tensor_parallel_si...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='outlines', distributed_executor_ba...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: LLM API server version 0.5.4 python 3.11.5 when i use vllm to doploy the model Mistral-Large-Instruct-2407-bnb-4bit,there is something wrong the model is from https://www.modelscope.cn/models/LLM-Research/Mistral-Large-...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug]: ValueError: BitAndBytes with enforce_eager = False is not supported yet. bug ### Your current environment vLLM API server version 0.5.4 python 3.11.5 when i use vllm to doploy the model Mistral-Large-Instruct-240...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ething wrong the model is from https://www.modelscope.cn/models/LLM-Research/Mistral-Large-Instruct-2407-bnb-4bit/files and files like tokenizer are from https://huggingface.co/mistralai/Mistral-Large-Instruct-2407/blob...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
