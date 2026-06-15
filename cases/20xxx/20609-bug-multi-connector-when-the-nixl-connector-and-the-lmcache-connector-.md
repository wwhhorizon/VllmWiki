# vllm-project/vllm#20609: [Bug]: [multi connector] when the Nixl Connector and the LMCache Connector coexist, the PD disaggregation fails.

| 字段 | 值 |
| --- | --- |
| Issue | [#20609](https://github.com/vllm-project/vllm/issues/20609) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [multi connector] when the Nixl Connector and the LMCache Connector coexist, the PD disaggregation fails.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using both the nixl connector and lmcache connector simultaneously, the Decode instance reports an error indicating 'engine_id not found'. Below is my startup command: ```shell VLLM_LOGGING_LEVEL=DEBUG LMCACHE_CHUNK_SIZE=256 LMCACHE_LOCAL_CPU=True LMCACHE_MAX_LOCAL_CPU_SIZE=30.0 LMCACHE_LOG_LEVEL=INFO CUDA_VISIBLE_DEVICES=0,1 VLLM_NIXL_SIDE_CHANNEL_PORT=5559 vllm serve /models/Qwen3-1.7B --served-model-name "qwen3" --port 8100 --disable-log-requests --gpu-memory-utilization 0.9 --tensor-parallel-size 2 --kv-transfer-config '{"kv_connector":"MultiConnector","kv_role":"kv_both","kv_connector_extra_config":{"connectors":[{"kv_connector":"NixlConnector","kv_role":"kv_both"},{"kv_connector":"LMCacheConnectorV1","kv_role":"kv_both"}]}}' VLLM_LOGGING_LEVEL=DEBUG LMCACHE_CHUNK_SIZE=256 LMCACHE_LOCAL_CPU=True LMCACHE_MAX_LOCAL_CPU_SIZE=30.0 LMCACHE_LOG_LEVEL=INFO CUDA_VISIBLE_DEVICES=2,3 VLLM_NIXL_SIDE_CHANNEL_PORT=5659 vllm serve /weights/Qwen3-1.7B --served-model-name "qwen3" --port 8200 --disable-log-requests --gpu-memory-utilization 0.9 --tensor-parallel-size 2 --kv-transfer-config '{"kv_connector":"MultiConnector","kv_role":"kv_...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: using both the nixl connector and lmcache connector simultaneously, the Decode instance reports an error indicating 'engine_id not found'. Below is my startup command: ```shell VLLM_LOGGING_LEVEL=DEBUG LMCACHE_CHUNK_SIZ...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: FO CUDA_VISIBLE_DEVICES=0,1 VLLM_NIXL_SIDE_CHANNEL_PORT=5559 vllm serve /models/Qwen3-1.7B --served-model-name "qwen3" --port 8100 --disable-log-requests --gpu-memory-utilization 0.9 --tensor-parallel-size 2 --kv-transf...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: HE_LOCAL_CPU=True LMCACHE_MAX_LOCAL_CPU_SIZE=30.0 LMCACHE_LOG_LEVEL=INFO CUDA_VISIBLE_DEVICES=0,1 VLLM_NIXL_SIDE_CHANNEL_PORT=5559 vllm serve /models/Qwen3-1.7B --served-model-name "qwen3" --port 8100 --disable-log-requ...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 598-0 from remote engine d8db2325-17b3-424e-a45b-2ec1bb58d71f. Num local_block_ids: 4. Num remote_block_ids: 4. (VllmWorker rank=0 pid=98473) DEBUG 07-08 02:13:53 [nixl_connector.py:472] Querying master rank metadata on...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
