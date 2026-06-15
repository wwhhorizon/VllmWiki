# vllm-project/vllm#12180: [Bug]: Vllm can't load models from unsloth-bnb-4bit

| 字段 | 值 |
| --- | --- |
| Issue | [#12180](https://github.com/vllm-project/vllm/issues/12180) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;operator;quantization |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Vllm can't load models from unsloth-bnb-4bit

### Issue 正文摘录

### Your current environment I am running the v0.6.6.post1 version of vllm out of a docker container. I tried using the following models from unsloth: - unsloth/phi-4-unsloth-bnb-4bit - unsloth/Llama-3.2-11B-Vision-Instruct-unsloth-bnb-4bit The model with just the `bnb-4bit` suffix seem to work fine. ### Model Input Dumps _No response_ ### 🐛 Describe the bug Here is the command I am using to run the model: ```bash docker run --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HF_TOKEN=$HF_TOKEN" \ --env "VLLM_LOGGING_LEVEL=DEBUG" \ --env "VLLM_TRACE_FUNCTION=1" \ -p 8000:8000 \ --ipc=host \ vllm/vllm-openai:latest \ --model $MODEL \ --enforce-eager \ --gpu_memory_utilization 0.60 \ --load-format bitsandbytes \ --quantization bitsandbytes \ --max_model_len 9000 ``` Here is the output: ```bash INFO 01-17 18:07:27 api_server.py:712] vLLM API server version 0.6.6.post1 INFO 01-17 18:07:27 api_server.py:713] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*' ], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_templat...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: bnb-4bit bug ### Your current environment I am running the v0.6.6.post1 version of vllm out of a docker container. I tried using the following models from unsloth: - unsloth/phi-4-unsloth-bnb-4bit - unsloth/Llama-3.2-11...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Vllm can't load models from unsloth-bnb-4bit bug ### Your current environment I am running the v0.6.6.post1 version of vllm out of a docker container. I tried using the following models from unsloth: - unsloth/ph...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: kens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='unsloth/phi-4-unsloth-bnb-4bit', task...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: --gpu_memory_utilization 0.60 \ --load-format bitsandbytes \ --quantization bitsandbytes \ --max_model_len 9000 ``` Here is the output: ```bash INFO 01-17 18:07:27 api_server.py:712] vLLM API server version 0.6.6.post1...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug]: Vllm can't load models from unsloth-bnb-4bit bug ### Your current environment I am running the v0.6.6.post1 version of vllm out of a docker container. I tried using the following models from unsloth: - unsloth/ph...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
