# vllm-project/vllm#9356: [Bug]: llama3.2-11B-Vision-Instruct not working

| 字段 | 值 |
| --- | --- |
| Issue | [#9356](https://github.com/vllm-project/vllm/issues/9356) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: llama3.2-11B-Vision-Instruct not working

### Issue 正文摘录

### Your current environment ### Model Input Dumps INFO 10-15 02:46:25 api_server.py:166] Multiprocessing frontend to use ipc:///tmp/e45c9a02-fb52-4618-b461-49904a0cac09 for IPC Path. INFO 10-15 02:46:25 api_server.py:179] Started engine process with PID 1016869 WARNING 10-15 02:46:25 config.py:1674] Casting torch.bfloat16 to torch.float16. /model/anaconda3/envs/llm/lib/python3.11/site-packages/vllm/connections.py:8: RuntimeWarning: Failed to read commit hash: No module named 'vllm._version' from vllm.version import __version__ as VLLM_VERSION WARNING 10-15 02:46:29 config.py:1674] Casting torch.bfloat16 to torch.float16. INFO 10-15 02:46:30 config.py:887] Defaulting to use mp for distributed inference WARNING 10-15 02:46:30 config.py:380] To see benefits of async output processing, enable CUDA graph. Since, enforce-eager is enabled, async output processor cannot be used INFO 10-15 02:46:34 config.py:887] Defaulting to use mp for distributed inference WARNING 10-15 02:46:34 config.py:380] To see benefits of async output processing, enable CUDA graph. Since, enforce-eager is enabled, async output processor cannot be used INFO 10-15 02:46:34 llm_engine.py:237] Initializing an LLM en...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: (vdev) with config: model='/model/models/Llama-3.2-11B-Vision-Instruct', speculative_config=None, tokenizer='/model/models/Llama-3.2-11B-Vision-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, o...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: py:8: RuntimeWarning: Failed to read commit hash: No module named 'vllm._version' from vllm.version import __version__ as VLLM_VERSION WARNING 10-15 02:46:29 config.py:1674] Casting torch.bfloat16 to torch.float16. INFO...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ss with PID 1016869 WARNING 10-15 02:46:25 config.py:1674] Casting torch.bfloat16 to torch.float16. /model/anaconda3/envs/llm/lib/python3.11/site-packages/vllm/connections.py:8: RuntimeWarning: Failed to read commit has...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: llama3.2-11B-Vision-Instruct not working bug ### Your current environment ### Model Input Dumps INFO 10-15 02:46:25 api_server.py:166] Multiprocessing frontend to use ipc:///tmp/e45c9a02-fb52-4618-b461-49904a0cac...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
