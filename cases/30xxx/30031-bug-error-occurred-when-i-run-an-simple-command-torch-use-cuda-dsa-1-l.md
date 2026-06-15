# vllm-project/vllm#30031: [Bug]: Error occurred when I run an simple command: "TORCH_USE_CUDA_DSA=1 LMCACHE_CHUNK_SIZE=8 vllm serve /home/nbw/model/Qwen2-0.5B/  --port 8000 --kv-transfer-config '{"kv_connector":"LMCacheConnectorV1", "kv_role":"kv_both"}'"

| 字段 | 值 |
| --- | --- |
| Issue | [#30031](https://github.com/vllm-project/vllm/issues/30031) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error occurred when I run an simple command: "TORCH_USE_CUDA_DSA=1 LMCACHE_CHUNK_SIZE=8 vllm serve /home/nbw/model/Qwen2-0.5B/  --port 8000 --kv-transfer-config '{"kv_connector":"LMCacheConnectorV1", "kv_role":"kv_both"}'"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The error is shown as below: ``` (APIServer pid=6908) INFO 12-04 23:05:25 [api_server.py:1772] vLLM API server version 0.12.0 (APIServer pid=6908) INFO 12-04 23:05:25 [utils.py:253] non-default args: {'model_tag': '/home/nbw/model/Qwen2-0.5B/', 'model': '/home/nbw/model/Qwen2-0.5B/', 'kv_transfer_config': KVTransferConfig(kv_connector='LMCacheConnectorV1', engine_id='823fba11-9ea2-4f1f-902e-9825b65f3377', kv_buffer_device='cuda', kv_buffer_size=1000000000.0, kv_role='kv_both', kv_rank=None, kv_parallel_size=1, kv_ip='127.0.0.1', kv_port=14579, kv_connector_extra_config={}, kv_connector_module_path=None, enable_permute_local_kv=False)} (APIServer pid=6908) INFO 12-04 23:05:25 [model.py:637] Resolved architecture: Qwen2ForCausalLM (APIServer pid=6908) INFO 12-04 23:05:25 [model.py:1750] Using max model len 32768 (APIServer pid=6908) INFO 12-04 23:05:25 [scheduler.py:228] Chunked prefill is enabled with max_num_batched_tokens=2048. (APIServer pid=6908) WARNING 12-04 23:05:25 [vllm.py:896] Turning off hybrid kv cache manager because `--kv-transfer-config` is set. This will reduce the performance of vLLM on LLMs with sliding window at...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: erver pid=6908) INFO 12-04 23:05:25 [api_server.py:1772] vLLM API server version 0.12.0 (APIServer pid=6908) INFO 12-04 23:05:25 [utils.py:253] non-default args: {'model_tag': '/home/nbw/model/Qwen2-0.5B/', 'model': '/h...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: command: "TORCH_USE_CUDA_DSA=1 LMCACHE_CHUNK_SIZE=8 vllm serve /home/nbw/model/Qwen2-0.5B/ --port 8000 --kv-transfer-config '{"kv_connector":"LMCacheConnectorV1", "kv_role":"kv_both"}'" bug;stale ### Your current enviro...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: config '{"kv_connector":"LMCacheConnectorV1", "kv_role":"kv_both"}'" bug;stale ### Your current environment ### 🐛 Describe the bug The error is shown as below: ``` (APIServer pid=6908) INFO 12-04 23:05:25 [api_server.py...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
