# vllm-project/vllm#28950: [Bug]: assert when offloading to cpu

| 字段 | 值 |
| --- | --- |
| Issue | [#28950](https://github.com/vllm-project/vllm/issues/28950) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: assert when offloading to cpu

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running llm-d-benchmark with vllm/vllm-openai:v0.11.0 configured for offloading as follows I am hitting an assert in vllm. ``` --kv-transfer-config '{"kv_connector":"OffloadingConnector","kv_role":"kv_both","kv_connector_extra_config":{"block_size": 256, "num_cpu_blocks": 1000}}' ``` The precise failure is ``` (EngineCore_DP0 pid=143) WARNING 11-18 07:48:24 [worker.py:116] Exception in ('CPU', 'GPU') transfer 235: AssertionError() (EngineCore_DP0 pid=143) WARNING 11-18 07:48:24 [worker.py:116] Traceback (most recent call last): (EngineCore_DP0 pid=143) WARNING 11-18 07:48:24 [worker.py:116] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/kv_offload/worker/worker.py", line 114, in transfer_async (EngineCore_DP0 pid=143) WARNING 11-18 07:48:24 [worker.py:116] success = handler.transfer_async(job_id, spec) (EngineCore_DP0 pid=143) WARNING 11-18 07:48:24 [worker.py:116] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=143) WARNING 11-18 07:48:24 [worker.py:116] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/kv_offload/worker/cpu_gpu.py", line 129, in transfer_async (EngineCore_DP0 pid=143) WARNING 11-18 07:48:24...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: or V1 LLM engine (v0.11.0) with config: model='meta-llama/Llama-3.1-8B', speculative_config=None, tokenizer='meta-llama/Llama-3.1-8B', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=No...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: xtra_config":{"block_size": 256, "num_cpu_blocks": 1000}}' ``` The precise failure is ``` (EngineCore_DP0 pid=143) WARNING 11-18 07:48:24 [worker.py:116] Exception in ('CPU', 'GPU') transfer 235: AssertionError() (Engin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: Describe the bug Running llm-d-benchmark with vllm/vllm-openai:v0.11.0 configured for offloading as follows I am hitting an assert in vllm. ``` --kv-transfer-config '{"kv_connector":"OffloadingConnector","kv_role":"kv_b...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_con...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
