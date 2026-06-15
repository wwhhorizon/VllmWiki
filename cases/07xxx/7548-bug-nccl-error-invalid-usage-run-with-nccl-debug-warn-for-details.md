# vllm-project/vllm#7548: [Bug]: NCCL error: invalid usage (run with NCCL_DEBUG=WARN for details)

| 字段 | 值 |
| --- | --- |
| Issue | [#7548](https://github.com/vllm-project/vllm/issues/7548) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: NCCL error: invalid usage (run with NCCL_DEBUG=WARN for details)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug LLM model is: Qwen/Qwen2-72B-Instruct Execute command is: ```nvidia- NCCL_DEBUG=WARN python3 -m vllm.entrypoints.openai.api_server --model=/workspace/atom/1/local_model/base_model/ -tp 4 ``` Error info is: ``` root@newllm201:/workspace# NCCL_DEBUG=WARN python3 -m vllm.entrypoints.openai.api_server --model=/workspace/atom/1/local_model/base_model/ -tp 4 INFO 08-15 07:47:02 api_server.py:219] vLLM API server version 0.5.3.post1 INFO 08-15 07:47:02 api_server.py:220] args: Namespace(allow_credentials=False, allowed_headers=['*'], allowed_methods=['*'], allowed_origins=['*'], api_key=None, block_size=16, chat_template=None, code_revision=None, cpu_offload_gb=0, device='auto', disable_custom_all_reduce=False, disable_log_requests=False, disable_log_stats=False, disable_logprobs_during_spec_decoding=None, disable_sliding_window=False, distributed_executor_backend=None, download_dir=None, dtype='auto', enable_chunked_prefill=None, enable_lora=False, enable_prefix_caching=False, enable_prompt_adapter=False, enforce_eager=False, engine_use_ray=False, fully_sharded_loras=False, gpu_memory_utilization=0.9, guided_decoding_backend='outlines'...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: g]: NCCL error: invalid usage (run with NCCL_DEBUG=WARN for details) bug;stale ### Your current environment ### 🐛 Describe the bug LLM model is: Qwen/Qwen2-72B-Instruct Execute command is: ```nvidia- NCCL_DEBUG=WARN pyt...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: base_model/ -tp 4 INFO 08-15 07:47:02 api_server.py:219] vLLM API server version 0.5.3.post1 INFO 08-15 07:47:02 api_server.py:220] args: Namespace(allow_credentials=False, allowed_headers=['*'], allowed_methods=['*'],...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ding_window=False, distributed_executor_backend=None, download_dir=None, dtype='auto', enable_chunked_prefill=None, enable_lora=False, enable_prefix_caching=False, enable_prompt_adapter=False, enforce_eager=False, engin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ) bug;stale ### Your current environment ### 🐛 Describe the bug LLM model is: Qwen/Qwen2-72B-Instruct Execute command is: ```nvidia- NCCL_DEBUG=WARN python3 -m vllm.entrypoints.openai.api_server --model=/workspace/atom/...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: FO 08-15 07:47:02 api_server.py:220] args: Namespace(allow_credentials=False, allowed_headers=['*'], allowed_methods=['*'], allowed_origins=['*'], api_key=None, block_size=16, chat_template=None, code_revision=None, cpu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
