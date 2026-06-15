# vllm-project/vllm#6071: [Gemma 2 27B]: Update docker hub image to support gemma-2-27B-it

| 字段 | 值 |
| --- | --- |
| Issue | [#6071](https://github.com/vllm-project/vllm/issues/6071) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | quantization |
| 症状 | crash |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Gemma 2 27B]: Update docker hub image to support gemma-2-27B-it

### Issue 正文摘录

### The model to consider. I am trying to run docker image of vllm for gemma-2-27B-it, But facing architectures not recognized error. error: ValueError: The checkpoint you are trying to load has model type `gemma2` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date. Entire command with logs: `docker run --runtime nvidia --gpus all -v ~/Vipul/nltk_data:/home/user/nltk_data --env "HUGGING_FACE_HUB_TOKEN=" -p 8514:8514 --ipc=host --env "CUDA_VISIBLE_DEVICES=1" --entrypoint "python3" vllm/vllm-openai:latest -m vllm.entrypoints.openai.api_server --model "mlx-community/gemma-2-9b-it-8bit" --gpu-memory-utilization 0.96 --port 8514 --trust-remote-code --tensor-parallel-size 1 --use-v2-block-manager INFO 07-02 15:11:13 api_server.py:177] vLLM API server version 0.5.0.post1 INFO 07-02 15:11:13 api_server.py:178] args: Namespace(host=None, port=8514, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=No...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Gemma 2 27B]: Update docker hub image to support gemma-2-27B-it new-model ### The model to consider. I am trying to run docker image of vllm for gemma-2-27B-it, But facing architectures not recognized error. error: Val
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: n 0.96 --port 8514 --trust-remote-code --tensor-parallel-size 1 --use-v2-block-manager INFO 07-02 15:11:13 api_server.py:177] vLLM API server version 0.5.0.post1 INFO 07-02 15:11:13 api_server.py:178] args: Namespace(ho...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Gemma 2 27B]: Update docker hub image to support gemma-2-27B-it new-model ### The model to consider. I am trying to run docker image of vllm for gemma-2-27B-it, But facing architectures not recognized error. error: Val...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ssor=None, image_processor_revision=None, disable_image_processor=False, scheduler_delay_factor=0.0, enable_chunked_prefill=False, speculative_model=None, num_speculative_tokens=None, speculative_max_model_len=None, spe...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: e='auto', trust_remote_code=True, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='outlines', distributed_executor_ba...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
