# vllm-project/vllm#18951: [Usage]: V1+1P1D+Lmcahe prefill  running queue only processes one request at a time, others stuck in waiting queue 

| 字段 | 值 |
| --- | --- |
| Issue | [#18951](https://github.com/vllm-project/vllm/issues/18951) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: V1+1P1D+Lmcahe prefill  running queue only processes one request at a time, others stuck in waiting queue 

### Issue 正文摘录

### Your current environment ```text MY SITUATION 2 * h20 vllm 0.8.5 qwen3-8b-fp8 UCX_TLS=cuda_ipc,cuda_copy,tcp \ LMCACHE_CONFIG_FILE=$prefill_config_file \ LMCACHE_USE_EXPERIMENTAL=True \ VLLM_ENABLE_V1_MULTIPROCESSING=1 \ VLLM_WORKER_MULTIPROC_METHOD=spawn \ CUDA_VISIBLE_DEVICES=0 \ vllm serve $MODEL \ --port 8100 \ --enforce-eager \ --kv-transfer-config \ '{"kv_connector":"LMCacheConnectorV1","kv_role":"kv_producer","kv_connector_extra_config": {"discard_partial_chunks": false, "lmcache_rpc_port": "producer1"}}' LMCACHE_CONFIG_FILE=$decode_config_file \ LMCACHE_USE_EXPERIMENTAL=True \ VLLM_ENABLE_V1_MULTIPROCESSING=1 \ VLLM_WORKER_MULTIPROC_METHOD=spawn \ CUDA_VISIBLE_DEVICES=1 \ vllm serve $MODEL \ --port 8200 \ --disable-log-requests \ --enforce-eager \ --kv-transfer-config \ '{"kv_connector":"LMCacheConnectorV1","kv_role":"kv_consumer","kv_connector_extra_config": {"discard_partial_chunks": false, "lmcache_rpc_port": "consumer1"}}' python3 disagg_proxy_server.py \ --host localhost \ --port 9000 \ --prefiller-host localhost \ --prefiller-port 8100 \ --decoder-host localhost \ --decoder-port 8200 MY PROBLEM I'm encountering an issue where the prefill instance running queue ca...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Usage]: V1+1P1D+Lmcahe prefill running queue only processes one request at a time, others stuck in waiting queue usage ### Your current environment ```text MY SITUATION 2 * h20 vllm 0.8.5 qwen3-8b-fp8 UCX_TLS=cuda_ipc,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ge ### Your current environment ```text MY SITUATION 2 * h20 vllm 0.8.5 qwen3-8b-fp8 UCX_TLS=cuda_ipc,cuda_copy,tcp \ LMCACHE_CONFIG_FILE=$prefill_config_file \ LMCACHE_USE_EXPERIMENTAL=True \ VLLM_ENABLE_V1_MULTIPROCES...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: `` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: vironment ```text MY SITUATION 2 * h20 vllm 0.8.5 qwen3-8b-fp8 UCX_TLS=cuda_ipc,cuda_copy,tcp \ LMCACHE_CONFIG_FILE=$prefill_config_file \ LMCACHE_USE_EXPERIMENTAL=True \ VLLM_ENABLE_V1_MULTIPROCESSING=1 \ VLLM_WORKER_M...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: er requests remain stuck in the waiting queue. This significantly limits throughput. ![Image](https://github.com/user-attachments/assets/b23750f3-e097-4a62-abc9-38c33f89c9d2) In contrast to the decoder instance, which c...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
