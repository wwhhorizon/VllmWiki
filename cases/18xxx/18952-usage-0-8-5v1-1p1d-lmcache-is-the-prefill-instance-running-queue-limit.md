# vllm-project/vllm#18952: [Usage]: [0.8.5v1+1P1D+LMCACHE] Is the Prefill instance running queue limited to processing only one request?

| 字段 | 值 |
| --- | --- |
| Issue | [#18952](https://github.com/vllm-project/vllm/issues/18952) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: [0.8.5v1+1P1D+LMCACHE] Is the Prefill instance running queue limited to processing only one request?

### Issue 正文摘录

### My current environment ```text 2 * h20 vllm 0.8.5 + v1 + 1p1d + lmcache qwen3-8b-fp8 UCX_TLS=cuda_ipc,cuda_copy,tcp \ LMCACHE_CONFIG_FILE=$prefill_config_file \ LMCACHE_USE_EXPERIMENTAL=True \ VLLM_ENABLE_V1_MULTIPROCESSING=1 \ VLLM_WORKER_MULTIPROC_METHOD=spawn \ CUDA_VISIBLE_DEVICES=0 \ vllm serve $MODEL \ --port 8100 \ --enforce-eager \ --kv-transfer-config \ '{"kv_connector":"LMCacheConnectorV1","kv_role":"kv_producer","kv_connector_extra_config": {"discard_partial_chunks": false, "lmcache_rpc_port": "producer1"}}' UCX_TLS=cuda_ipc,cuda_copy,tcp \ LMCACHE_CONFIG_FILE=$decode_config_file \ LMCACHE_USE_EXPERIMENTAL=True \ VLLM_ENABLE_V1_MULTIPROCESSING=1 \ VLLM_WORKER_MULTIPROC_METHOD=spawn \ CUDA_VISIBLE_DEVICES=1 \ vllm serve $MODEL \ --port 8200 \ --disable-log-requests \ --enforce-eager \ --kv-transfer-config \ '{"kv_connector":"LMCacheConnectorV1","kv_role":"kv_consumer","kv_connector_extra_config": {"discard_partial_chunks": false, "lmcache_rpc_port": "consumer1"}}' python3 disagg_proxy_server.py \ --host localhost \ --port 9000 \ --prefiller-host localhost \ --prefiller-port 8100 \ --decoder-host localhost \ --decoder-port 8200 ``` My benchmark startup command: ```tex...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Usage]: [0.8.5v1+1P1D+LMCACHE] Is the Prefill instance running queue limited to processing only one request? usage;stale ### My current environment ```text 2 * h20 vllm 0.8.5 + v1 + 1p1d + lmcache qwen3-8b-fp8 UCX_TLS=...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: My current environment ```text 2 * h20 vllm 0.8.5 + v1 + 1p1d + lmcache qwen3-8b-fp8 UCX_TLS=cuda_ipc,cuda_copy,tcp \ LMCACHE_CONFIG_FILE=$prefill_config_file \ LMCACHE_USE_EXPERIMENTAL=True \ VLLM_ENABLE_V1_MULTIPROCES...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: --decoder-host localhost \ --decoder-port 8200 ``` My benchmark startup command: ```text python3 benchmark_serving.py --port 9000 --seed $(date +%s) --model /model --dataset-name random --random-input-len 7500 --random-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ```text 2 * h20 vllm 0.8.5 + v1 + 1p1d + lmcache qwen3-8b-fp8 UCX_TLS=cuda_ipc,cuda_copy,tcp \ LMCACHE_CONFIG_FILE=$prefill_config_file \ LMCACHE_USE_EXPERIMENTAL=True \ VLLM_ENABLE_V1_MULTIPROCESSING=1 \ VLLM_WORKER_MU...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: t environment ```text 2 * h20 vllm 0.8.5 + v1 + 1p1d + lmcache qwen3-8b-fp8 UCX_TLS=cuda_ipc,cuda_copy,tcp \ LMCACHE_CONFIG_FILE=$prefill_config_file \ LMCACHE_USE_EXPERIMENTAL=True \ VLLM_ENABLE_V1_MULTIPROCESSING=1 \...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
