# vllm-project/vllm#8242: [Bug]: GPU Memory Utilization Lower Than Expected with --enable-prefix-caching

| 字段 | 值 |
| --- | --- |
| Issue | [#8242](https://github.com/vllm-project/vllm/issues/8242) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;operator;quantization;triton |
| 症状 | build_error;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GPU Memory Utilization Lower Than Expected with --enable-prefix-caching

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Description:** When launching vllm with the --enable-prefix-caching flag, the GPU memory utilization is only around 70%, which is lower than the expected 90% based on the gpu_memory_utilization=0.9 setting. The model being used is neuralmagic/Meta-Llama-3.1-8B-Instruct-quantized.w8a8. **Steps to Reproduce:** 1. Launch vllm with the following command: ```bash nohup python -m vllm.entrypoints.openai.api_server --enable-prefix-caching --tensor-parallel-size 1 --model neuralmagic/Meta-Llama-3.1-8B-Instruct-quantized.w8a8 --trust-remote-code --enable-chunked-prefill 1>vlog 2>&1 & ``` 2. Confirm startup log ```text INFO 09-07 00:53:29 api_server.py:459] vLLM API server version 0.6.0 INFO 09-07 00:53:29 api_server.py:460] args: Namespace(allow_credentials=False, allowed_headers=['*'], allowed_methods=['*'], allowed_origins=['*'], api_key=None, block_size=16, chat_template=None, code_revision=None, collect_detailed_traces=None, cpu_offload_gb=0, device='auto', disable_async_output_proc=False, disable_custom_all_reduce=False, disable_frontend_multiprocessing=False, disable_log_requests=False, disable_log_stats=False, disable_logprobs_du...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: Memory Utilization Lower Than Expected with --enable-prefix-caching bug;stale ### Your current environment ### 🐛 Describe the bug **Description:** When launching vllm with the --enable-prefix-caching flag, the GPU memor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: artup log ```text INFO 09-07 00:53:29 api_server.py:459] vLLM API server version 0.6.0 INFO 09-07 00:53:29 api_server.py:460] args: Namespace(allow_credentials=False, allowed_headers=['*'], allowed_methods=['*'], allowe...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: setting. The model being used is neuralmagic/Meta-Llama-3.1-8B-Instruct-quantized.w8a8. **Steps to Reproduce:** 1. Launch vllm with the following command: ```bash nohup python -m vllm.entrypoints.openai.api_server --ena...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: [Bug]: GPU Memory Utilization Lower Than Expected with --enable-prefix-caching bug;stale ### Your current environment ### 🐛 Describe the bug **Description:** When launching vllm with the --enable-prefix-caching flag, th...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: an the expected 90% based on the gpu_memory_utilization=0.9 setting. The model being used is neuralmagic/Meta-Llama-3.1-8B-Instruct-quantized.w8a8. **Steps to Reproduce:** 1. Launch vllm with the following command: ```b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
