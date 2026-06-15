# vllm-project/vllm#18801: [Performance]: How can i improve performance further in vllm lmcache PD Disaggregate？Plz Help Me

| 字段 | 值 |
| --- | --- |
| Issue | [#18801](https://github.com/vllm-project/vllm/issues/18801) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: How can i improve performance further in vllm lmcache PD Disaggregate？Plz Help Me

### Issue 正文摘录

### Proposal to improve performance Hi guys i am newly here I have some requirement Can someone guide me? Thank you very much ### MY SITUATION 8 * H200 vllm 0.8.5 base docker image (also i have lmcache/vllm-openai:2025-05-17-v1) Qwen2.5 72B need to improve its performance in ttft, tpot, throughput by PD Disaggregate by mooncake I have try successfully by lmcache connector v1 below ` UCX_TLS=cuda_ipc,cuda_copy,tcp LMCACHE_CONFIG_FILE=/workspace/examples/lmcache/disagg_prefill_lmcache_v1/configs/lmcache-prefiller-config.yaml LMCACHE_USE_EXPERIMENTAL=True VLLM_ENABLE_V1_MULTIPROCESSING=1 VLLM_WORKER_MULTIPROC_METHOD=spawn CUDA_VISIBLE_DEVICES=0,1 VLLM_USE_V1=1 /opt/venv/bin/vllm serve /xxbucket/prod/models/QWEN-25-72B-INSTRUCT/Qwen2.5-72B-Instruct --served-model-name llm --port 8100 --max-model-len 6400 --max-num-batched-tokens 6400 --max-num-seqs 48 --block-size 128 --gpu-memory-utilization 0.95 --tensor-parallel-size 2 --max_seq_len_to_capture 6400 --enforce-eager --trust-remote-code --kv-transfer-config '{"kv_connector":"LMCacheConnectorV1","kv_role":"kv_producer","kv_connector_extra_config": {"discard_partial_chunks": false, "lmcache_rpc_port": "producer1"}}' > /prefiller.log 2>&...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: enai:2025-05-17-v1) Qwen2.5 72B need to improve its performance in ttft, tpot, throughput by PD Disaggregate by mooncake I have try successfully by lmcache connector v1 below ` UCX_TLS=cuda_ipc,cuda_copy,tcp LMCACHE_CON...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 0.8.5 base docker image (also i have lmcache/vllm-openai:2025-05-17-v1) Qwen2.5 72B need to improve its performance in ttft, tpot, throughput by PD Disaggregate by mooncake I have try successfully by lmcache connector v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: formance further in vllm lmcache PD Disaggregate？Plz Help Me performance;stale ### Proposal to improve performance Hi guys i am newly here I have some requirement Can someone guide me? Thank you very much ### MY SITUATI...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: guide me? Thank you very much ### MY SITUATION 8 * H200 vllm 0.8.5 base docker image (also i have lmcache/vllm-openai:2025-05-17-v1) Qwen2.5 72B need to improve its performance in ttft, tpot, throughput by PD Disaggrega...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: mooncake I have try successfully by lmcache connector v1 below ` UCX_TLS=cuda_ipc,cuda_copy,tcp LMCACHE_CONFIG_FILE=/workspace/examples/lmcache/disagg_prefill_lmcache_v1/configs/lmcache-prefiller-config.yaml LMCACHE_USE...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
