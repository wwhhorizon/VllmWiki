# vllm-project/vllm#15769: [Bug]: v0.8.2 vLLM engine crashes when starting after V1 environment variable is enabled with deepseek-r1

| 字段 | 值 |
| --- | --- |
| Issue | [#15769](https://github.com/vllm-project/vllm/issues/15769) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cache;cuda;fp8;operator;quantization;triton |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.8.2 vLLM engine crashes when starting after V1 environment variable is enabled with deepseek-r1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` bash /vllm-workspace/examples/online_serving/multi-node-serving.sh leader --ray_cluster_size=$(LWS_GROUP_SIZE) && python3 -m vllm.entrypoints.openai.api_server --model /models/DeepSeek-R1 --served-model-name DeepSeek-R1 --port 8000 --tensor-parallel-size 8 --pipeline-parallel-size 2 --trust-remote-code --gpu-memory-utilization 0.95 --max-model-len 131072 --enable-reasoning --reasoning-parser deepseek_r1 --max-num-seqs 256 env: - name: GLOO_SOCKET_IFNAME value: eth0 - name: NCCL_IB_HCA value: "mlx5_0,mlx5_1,mlx5_4,mlx5_5" - name: NCCL_P2P_LEVEL value: "NVL" - name: NCCL_IB_GID_INDEX value: "0" - name: NCCL_IB_CUDA_SUPPORT value: "1" - name: NCCL_IB_DISABLE value: "0" - name: NCCL_SOCKET_IFNAME value: "eth0" - name: NCCL_DEBUG value: "INFO" - name: NCCL_NET_GDR_LEVEL value: "2" - name: VLLM_USE_MODELSCOPE value: "True" - name: VLLM_USE_V1 value: "1" ``` log： ``` 2025-03-30 18:44:55,147 INFO worker.py:1852 -- Connected to Ray cluster. All ray workers are active and the ray cluster is initialized successfully. INFO 03-30 18:45:05 [__init__.py:239] Automatically detected platform cuda. INFO 03-30 18:45:08 [api_server.py:981] vLLM...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/models/DeepSeek-R1', task='auto', t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: d platform cuda. INFO 03-30 18:45:08 [api_server.py:981] vLLM API server version 0.8.2 INFO 03-30 18:45:08 [api_server.py:982] args: Namespace(host=None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=F...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=131072, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', d...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: =None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapter...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: P_SIZE) && python3 -m vllm.entrypoints.openai.api_server --model /models/DeepSeek-R1 --served-model-name DeepSeek-R1 --port 8000 --tensor-parallel-size 8 --pipeline-parallel-size 2 --trust-remote-code

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
