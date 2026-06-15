# vllm-project/vllm#6228: [Usage]: vllm openai api server never ends in most cases

| 字段 | 值 |
| --- | --- |
| Issue | [#6228](https://github.com/vllm-project/vllm/issues/6228) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: vllm openai api server never ends in most cases

### Issue 正文摘录

### Your current environment Hey Guys, I tried the open ai api server, to load a 70B Llama-3 checkpoint. I think out of the 3-4 efforts I did, only one time the model successfully loaded after about 1 our, for the other two times, nothing happened, even after 3 hours of wait time. I'm loading the model on 8xA100/80G azure nodes. Am I following the right practice? For the failed cases, cuda memory usage wont exceed 18G (it should be around 70-80G otherwise) ### How would you like to use vllm ```text (nlp) azureuser@dev-8xa100-b:/mnt/batch/tasks/shared/LS_root/mounts/clusters/dev-8xa100-b/code/Users/hamid.hassanzadeh/cava-data/llama_expr$ NAME='Llama-3-70B-Instruct' && python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8000 --served-model-name $NAME --model /home/azureuser/cloudfiles/code/Users/user/llama_setup/model_catalog_llama/Meta-Llama-3-70B-Instruct/mlflow_model_folder/data/model/ --tensor-parallel-size 8 --trust-remote-code INFO 07-08 20:49:31 api_server.py:206] vLLM API server version 0.5.1 INFO 07-08 20:49:31 api_server.py:207] args: Namespace(allow_credentials=False, allowed_headers=['*'], allowed_methods=['*'], allowed_origins=['*'], api_key=None, block_s...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Usage]: vllm openai api server never ends in most cases usage;stale ### Your current environment Hey Guys, I tried the open ai api server, to load a 70B Llama-3 checkpoint. I think out of the 3-4 efforts I did, only on...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ding_window=False, distributed_executor_backend=None, download_dir=None, dtype='auto', enable_chunked_prefill=False, enable_lora=False, enable_prefix_caching=False, enforce_eager=False, engine_use_ray=False, fully_shard...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ent environment Hey Guys, I tried the open ai api server, to load a 70B Llama-3 checkpoint. I think out of the 3-4 efforts I did, only one time the model successfully loaded after about 1 our, for the other two times, n...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: trust-remote-code INFO 07-08 20:49:31 api_server.py:206] vLLM API server version 0.5.1 INFO 07-08 20:49:31 api_server.py:207] args: Namespace(allow_credentials=False, allowed_headers=['*'], allowed_methods=['*'], allowe...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: FO 07-08 20:49:31 api_server.py:207] args: Namespace(allow_credentials=False, allowed_headers=['*'], allowed_methods=['*'], allowed_origins=['*'], api_key=None, block_size=16, chat_template=None, code_revision=None, dev...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
