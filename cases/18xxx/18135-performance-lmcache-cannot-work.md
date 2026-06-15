# vllm-project/vllm#18135: [Performance]: lmcache cannot work！

| 字段 | 值 |
| --- | --- |
| Issue | [#18135](https://github.com/vllm-project/vllm/issues/18135) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | cuda;gemm;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: lmcache cannot work！

### Issue 正文摘录

### Your current environment My test environment is as follow： ``` Environment: 2x H100 with NVLink ``` My testing method： ``` # P instance UCX_TLS=cuda_ipc,cuda_copy,tcp \ LMCACHE_CONFIG_FILE=/work/vllm-0.8.5/examples/lmcache/disagg_prefill_lmcache_v1/configs/lmcache-prefiller-config.yaml \ LMCACHE_USE_EXPERIMENTAL=True \ VLLM_ENABLE_V1_MULTIPROCESSING=1 \ VLLM_WORKER_MULTIPROC_METHOD=spawn \ CUDA_VISIBLE_DEVICES=0 \ vllm serve /work/Qwen/Qwen2.5-0.5B-Instruct \ --port 8100 \ --disable-log-requests \ --enforce-eager \ --kv-transfer-config \ '{"kv_connector":"LMCacheConnectorV1","kv_role":"kv_producer","kv_connector_extra_config": {"discard_partial_chunks": false, "lmcache_rpc_port": "producer1"}}' # D instance UCX_TLS=cuda_ipc,cuda_copy,tcp \ LMCACHE_CONFIG_FILE=/work/vllm-0.8.5/examples/lmcache/disagg_prefill_lmcache_v1/configs/lmcache-decoder-config.yaml \ LMCACHE_USE_EXPERIMENTAL=True \ VLLM_ENABLE_V1_MULTIPROCESSING=1 \ VLLM_WORKER_MULTIPROC_METHOD=spawn \ CUDA_VISIBLE_DEVICES=1 \ vllm serve /work/Qwen/Qwen2.5-0.5B-Instruct \ --port 8200 \ --disable-log-requests \ --enforce-eager \ --kv-transfer-config \ '{"kv_connector":"LMCacheConnectorV1","kv_role":"kv_consumer","kv_connec...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 9: ethod： ``` # P instance UCX_TLS=cuda_ipc,cuda_copy,tcp \ LMCACHE_CONFIG_FILE=/work/vllm-0.8.5/examples/lmcache/disagg_prefill_lmcache_v1/configs/lmcache-prefiller-config.yaml \ LMCACHE_USE_EXPERIMENTAL=True \ VLLM_ENABL...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ment My test environment is as follow： ``` Environment: 2x H100 with NVLink ``` My testing method： ``` # P instance UCX_TLS=cuda_ipc,cuda_copy,tcp \ LMCACHE_CONFIG_FILE=/work/vllm-0.8.5/examples/lmcache/disagg_prefill_l...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Performance]: lmcache cannot work！ usage;stale ### Your current environment My test environment is as follow： ``` Environment: 2x H100 with NVLink ``` My testing method： ``` # P instance UCX_TLS=cuda_ipc,cuda_copy,tcp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: True, config_format= , dtype='auto', max_model_len=None, guided_decoding_backend='auto', reasoning_parser=None, logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: e, model_loader_extra_config={}, use_tqdm_on_load=True, config_format= , dtype='auto', max_model_len=None, guided_decoding_backend='auto', reasoning_parser=None, logits_processor_pattern=None, model_impl='auto', distrib...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
