# vllm-project/vllm#7817: [Usage]: When debugging with vLLM, a CUDA error occurs.

| 字段 | 值 |
| --- | --- |
| Issue | [#7817](https://github.com/vllm-project/vllm/issues/7817) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;scheduler_memory |
| 子分类 | runtime_err |
| Operator 关键词 | attention;cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: When debugging with vLLM, a CUDA error occurs.

### Issue 正文摘录

### vllm latest I add some logger in /vllm/model_executor/models/llama.py ,I want to print the attention ,like that if I start llm server,the error is [rank0]: During handling of the above exception, another exception occurred: [rank0]: Traceback (most recent call last): [rank0]: File "/usr/local/bin/vllm", line 8, in [rank0]: sys.exit(main()) [rank0]: File "/usr/local/lib/python3.10/dist-packages/vllm/scripts.py", line 148, in main [rank0]: args.dispatch_function(args) [rank0]: File "/usr/local/lib/python3.10/dist-packages/vllm/scripts.py", line 28, in serve [rank0]: run_server(args) [rank0]: File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/api_server.py", line 231, in run_server [rank0]: if llm_engine is not None else AsyncLLMEngine.from_engine_args( [rank0]: File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 467, in from_engine_args [rank0]: engine = cls( [rank0]: File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 381, in __init__ [rank0]: self.engine = self._init_engine(*args, **kwargs) [rank0]: File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 548, in _i...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: error: operation failed due to a previous error during capture [rank0]: Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.** ### How would you like to use vllm I want to debug vllm development attention...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ver.py", line 231, in run_server [rank0]: if llm_engine is not None else AsyncLLMEngine.from_engine_args( [rank0]: File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 467, in from_engine...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: DA error occurs. usage;stale ### vllm latest I add some logger in /vllm/model_executor/models/llama.py ,I want to print the attention ,like that if I start llm server,the error is [rank0]: During handling of the above e...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: When debugging with vLLM, a CUDA error occurs. usage;stale ### vllm latest I add some logger in /vllm/model_executor/models/llama.py ,I want to print the attention ,like that if I start llm server,the error is...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 3.10/dist-packages/vllm/scripts.py", line 148, in main [rank0]: args.dispatch_function(args) [rank0]: File "/usr/local/lib/python3.10/dist-packages/vllm/scripts.py", line 28, in serve [rank0]: run_server(args) [rank0]:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
