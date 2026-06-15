# vllm-project/vllm#18382: [Bug]: GGUF model with architecture qwen3moe is not supported yet.

| 字段 | 值 |
| --- | --- |
| Issue | [#18382](https://github.com/vllm-project/vllm/issues/18382) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GGUF model with architecture qwen3moe is not supported yet.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I used Qwen3-235B-A22B-128K-GGUF's UD-Q4_K_XL to merge via llama-gguf-split into: Qwen3-235B-A22B-merge-UD-Q4_K_XL.gguf, an error occurred when starting with vllm: 0.8.5.post1 python3 -m vllm.entrypoints.openai.api_server --model /xinference/my_model/Qwen3-235B-A22B-UD-Q4_K_XL/Qwen3-235B-A22B-merge-UD-Q4_K_XL.gguf --served-model-name Qwen3 --tensor-parallel-size 4 --trust-remote-code --max_model_len 4096 --host 0.0.0.0 --port 8501 --dtype bfloat16 --enable-auto-tool-choice --tool-call-parser hermes --gpu-memory-utilization 0.9 error_log: ``` INFO 05-20 13:04:04 [__init__.py:239] Automatically detected platform cuda. INFO 05-20 13:04:06 [api_server.py:1043] vLLM API server version 0.8.5.post1 INFO 05-20 13:04:06 [api_server.py:1044] args: Namespace(host='0.0.0.0', port=8501, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_s...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: GGUF model with architecture qwen3moe is not supported yet. bug;stale ### Your current environment ### 🐛 Describe the bug When I used Qwen3-235B-A22B-128K-GGUF's UD-Q4_K_XL to merge via llama-gguf-split into: Qwe...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: 4 --trust-remote-code --max_model_len 4096 --host 0.0.0.0 --port 8501 --dtype bfloat16 --enable-auto-tool-choice --tool-call-parser hermes --gpu-memory-utilization 0.9 error_log: ``` INFO 05-20 13:04:04 [__init__.py:239...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: GGUF model with architecture qwen3moe is not supported yet. bug;stale ### Your current environment ### 🐛 Describe the bug When I used Qwen3-235B-A22B-128K-GGUF's UD-Q4_K_XL to merge via llama-gguf-split into: Qwe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: platform cuda. INFO 05-20 13:04:06 [api_server.py:1043] vLLM API server version 0.8.5.post1 INFO 05-20 13:04:06 [api_server.py:1044] args: Namespace(host='0.0.0.0', port=8501, uvicorn_log_level='info', disable_uvicorn_a...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: .0.0', port=8501, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapter...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
