# vllm-project/vllm#15453: [Bug]: ValueError: not enough values to unpack (expected 22, got 21) when deploying DeepSeekV3

| 字段 | 值 |
| --- | --- |
| Issue | [#15453](https://github.com/vllm-project/vllm/issues/15453) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;kernel;quantization;sampling |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: not enough values to unpack (expected 22, got 21) when deploying DeepSeekV3

### Issue 正文摘录

### Your current environment For the environment, i simply use the vllm v0.8.0 docker image. ### 🐛 Describe the bug When deploying DeepSeekV3 with TP=16 on two nodes, I encounter the `ValueError: not enough values to unpack (expected 22, got 21) ` error. To create containers and ray, I use the following commands, in which the `run_cluster.sh` refers to [vllm sample](https://github.com/vllm-project/vllm/blob/main/examples/online_serving/run_cluster.sh). ```bash # head node DOCKER_IMAGE="xxx" HEAD_NODE_ADDRESS="xxx" NODE_TYPE="--head" # Should be --head or --worker PATH_TO_HF_HOME="xxx" CRT_NODE_ADDRESS=${HEAD_NODE_ADDRESS} bash run_cluster.sh \ ${DOCKER_IMAGE} \ ${HEAD_NODE_ADDRESS} \ ${NODE_TYPE} \ ${PATH_TO_HF_HOME} \ -e VLLM_HOST_IP=${CRT_NODE_ADDRESS} # other node DOCKER_IMAGE="xxx" HEAD_NODE_ADDRESS="xxx" NODE_TYPE="--worker" # Should be --head or --worker PATH_TO_HF_HOME="xxx" CRT_NODE_ADDRESS="xxx" bash run_cluster.sh \ ${DOCKER_IMAGE} \ ${HEAD_NODE_ADDRESS} \ ${NODE_TYPE} \ ${PATH_TO_HF_HOME} \ -e VLLM_HOST_IP=${CRT_NODE_ADDRESS} ``` To start API service, I use ```bash NCCL_DEBUG=INFO \ NCCL_SOCKET_IFNAME=eth0 \ GLOO_SOCKET_IFNAME=eth0 \ HF_EVALUATE_OFFLINE=1 \ HF_DATASETS_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: r current environment For the environment, i simply use the vllm v0.8.0 docker image. ### 🐛 Describe the bug When deploying DeepSeekV3 with TP=16 on two nodes, I encounter the `ValueError: not enough values to unpack (e...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', dis...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/mnt/huggingface_hub_137_llm/hub/mod...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: ='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ADDRESS="xxx" NODE_TYPE="--head" # Should be --head or --worker PATH_TO_HF_HOME="xxx" CRT_NODE_ADDRESS=${HEAD_NODE_ADDRESS} bash run_cluster.sh \ ${DOCKER_IMAGE} \ ${HEAD_NODE_ADDRESS} \ ${NODE_TYPE} \ ${PATH_TO_HF_HOME...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
