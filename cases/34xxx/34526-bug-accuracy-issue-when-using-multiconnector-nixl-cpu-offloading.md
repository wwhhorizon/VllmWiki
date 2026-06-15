# vllm-project/vllm#34526: [Bug]: accuracy issue when using multiconnector(Nixl+cpu offloading)

| 字段 | 值 |
| --- | --- |
| Issue | [#34526](https://github.com/vllm-project/vllm/issues/34526) |
| 状态 | closed |
| 标签 | bug;kv-connector |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: accuracy issue when using multiconnector(Nixl+cpu offloading)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Observing accuracy issues when running gpu-gpu multiconnector using Nixl+CPU_offloading for PD case. Setup - latest vllm - hardware a100 and h200 command below is simialr for prefill and decode instances except for port and ip changes. ``` BASE_CMD="UCX_TLS=ib,rc,cuda_copy NIXL_LOG_LEVEL=debug VLLM_LOGGING_LEVEL=INFO UCX_MEMTYPE_CACHE=0 VLLM_USE_V1=1 \ VLLM_KV_CACHE_LAYOUT=HND VLLM_NIXL_DEVICE_TO_DEVICE=1 UCX_NET_DEVICES=all \ VLLM_LOGGING_LEVEL=DEBUG CUDA_VISIBLE_DEVICES=$GPU_ID VLLM_NIXL_SIDE_CHANNEL_HOST=$SIDE_CHANNEL_HOST VLLM_NIXL_SIDE_CHANNEL_PORT=$SIDE_CHANNEL_PORT \ vllm serve $model_name \ --port $PORT \ --gpu-memory-utilization 0.40 \ --tensor-parallel-size $PREFILL_TP_SIZE \ --long_prefill_token_threshold 8192 \ --max-num-batched-tokens 65536 \ --max-model-len 65536 \ --max-num-seqs 128 \ --disable-log-requests \ --no-enable-prefix-caching \ --kv-transfer-config '{\"kv_connector\":\"MultiConnector\",\"kv_role\":\"kv_both\",\"kv_connector_extra_config\":{\"connectors\":[{\"kv_connector\":\"NixlConnector\",\"kv_role\":\"kv_both\",\"kv_connector_extra_config\":{\"enforce_handshake_compat\":false}},{\"kv_connector\":\"Offl...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: using Nixl+CPU_offloading for PD case. Setup - latest vllm - hardware a100 and h200 command below is simialr for prefill and decode instances except for port and ip changes. ``` BASE_CMD="UCX_TLS=ib,rc,cuda_copy NIXL_LO...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ING_LEVEL=INFO UCX_MEMTYPE_CACHE=0 VLLM_USE_V1=1 \ VLLM_KV_CACHE_LAYOUT=HND VLLM_NIXL_DEVICE_TO_DEVICE=1 UCX_NET_DEVICES=all \ VLLM_LOGGING_LEVEL=DEBUG CUDA_VISIBLE_DEVICES=$GPU_ID VLLM_NIXL_SIDE_CHANNEL_HOST=$SIDE_CHAN...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: OST VLLM_NIXL_SIDE_CHANNEL_PORT=$SIDE_CHANNEL_PORT \ vllm serve $model_name \ --port $PORT \ --gpu-memory-utilization 0.40 \ --tensor-parallel-size $PREFILL_TP_SIZE \ --long_prefill_token_threshold 8192 \ --max-num-batc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: up - latest vllm - hardware a100 and h200 command below is simialr for prefill and decode instances except for port and ip changes. ``` BASE_CMD="UCX_TLS=ib,rc,cuda_copy NIXL_LOG_LEVEL=debug VLLM_LOGGING_LEVEL=INFO UCX_...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [Bug]: accuracy issue when using multiconnector(Nixl+cpu offloading) bug;kv-connector ### Your current environment ### 🐛 Describe the bug Observing accuracy issues when running gpu-gpu multiconnector using Nixl+CPU_offl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
