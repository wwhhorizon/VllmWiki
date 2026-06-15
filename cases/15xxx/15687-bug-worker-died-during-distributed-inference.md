# vllm-project/vllm#15687: [Bug]: Worker died during distributed inference

| 字段 | 值 |
| --- | --- |
| Issue | [#15687](https://github.com/vllm-project/vllm/issues/15687) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Worker died during distributed inference

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I deployed VLLM+Ray using containers on two nodes. The ray cluster information is as follows: ```text ======== Autoscaler status: 2025-03-28 00:38:24.697168 ======== Node status --------------------------------------------------------------- Active: 1 node_0e1b24bf0116d75c041dc6d1ce6ff498a5a0fd7013613c601d63ab1c 1 node_3a8b52b1966cd168bdb3ea3b9daa84dfeda5686e037cd5d2345f95f3 Pending: (no pending nodes) Recent failures: (no failures) Resources --------------------------------------------------------------- Usage: 0.0/360.0 CPU 0.0/16.0 GPU 0B/3.39TiB memory 0B/372.53GiB object_store_memory Demands: (no resource demands) ``` I use the following command to run the Deepseek model: ```bash python3 -m vllm.entrypoints.openai.api_server --port 18011 --model /models/snapshots/4c1f24cc10a2a1894304c7ab52edd9710c047571 --tensor-parallel-size 16 --gpu-memory-utilization 0.92 --dtype auto --served-model-name deepseekv3 --max-num-seqs 40 --max-model-len 16384 --enable-chunked-prefill --enable-prefix-caching --trust-remote-code ``` The error message is as follows: ```text INFO 03-27 22:16:27 [__init__.py:239] Automatically detected platform cud...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: o nodes. The ray cluster information is as follows: ```text ======== Autoscaler status: 2025-03-28 00:38:24.697168 ======== Node status --------------------------------------------------------------- Active: 1 node_0e1b...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Worker died during distributed inference bug;ray;stale ### Your current environment ### 🐛 Describe the bug I deployed VLLM+Ray using containers on two nodes. The ray cluster information is as follows: ```text ===...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: al development! INFO 03-27 22:16:29 [api_server.py:1018] vLLM API server version 0.8.3.dev82+gcec8c7d7 INFO 03-27 22:16:29 [api_server.py:1019] args: Namespace(host=None, port=18011, uvicorn_log_level='info', disable_uv...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: _block_manager=True, num_lookahead_slots=0, seed=None, swap_space=4, cpu_offload_gb=0, gpu_memory_utilization=0.92, num_gpu_blocks_override=None, max_num_batched_tokens=None, max_num_partial_prefills=1, max_long_partial...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: None, port=18011, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapter...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
