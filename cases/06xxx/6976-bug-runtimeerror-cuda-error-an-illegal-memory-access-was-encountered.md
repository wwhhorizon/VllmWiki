# vllm-project/vllm#6976: [Bug]: RuntimeError: CUDA error: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#6976](https://github.com/vllm-project/vllm/issues/6976) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | attention;cuda;quantization |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: CUDA error: an illegal memory access was encountered

### Issue 正文摘录

### Your current environment vllm docker v0.5.0post1, GPU: 4090 cuda driver: Driver Version: 535.86.10 model: qwen1.5-14b-chat-AWQ, with enable-prefix-caching ### 🐛 Describe the bug ERROR 07-31 15:13:06 async_llm_engine.py:61] Engine background task failed ERROR 07-31 15:13:06 async_llm_engine.py:61] Traceback (most recent call last): ERROR 07-31 15:13:06 async_llm_engine.py:61] File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 51, in _log_task_completion ERROR 07-31 15:13:06 async_llm_engine.py:61] return_value = task.result() ERROR 07-31 15:13:06 async_llm_engine.py:61] File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 548, in run_engine_loop ERROR 07-31 15:13:06 async_llm_engine.py:61] has_requests_in_progress = await asyncio.wait_for( ERROR 07-31 15:13:06 async_llm_engine.py:61] File "/usr/lib/python3.10/asyncio/tasks.py", line 445, in wait_for ERROR 07-31 15:13:06 async_llm_engine.py:61] return fut.result() ERROR 07-31 15:13:06 async_llm_engine.py:61] File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 522, in engine_step ERROR 07-31 15:13:06 async_llm_engine.py:61] request_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: gal memory access was encountered bug ### Your current environment vllm docker v0.5.0post1, GPU: 4090 cuda driver: Driver Version: 535.86.10 model: qwen1.5-14b-chat-AWQ, with enable-prefix-caching ### 🐛 Describe the bug...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: llm_engine.py:61] output = self.model_runner.execute_model(seq_group_metadata_list, ERROR 07-31 15:13:06 async_llm_engine.py:61] File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 115, in de...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: lm docker v0.5.0post1, GPU: 4090 cuda driver: Driver Version: 535.86.10 model: qwen1.5-14b-chat-AWQ, with enable-prefix-caching ### 🐛 Describe the bug ERROR 07-31 15:13:06 async_llm_engine.py:61] Engine background task...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: in run_engine_loop ERROR 07-31 15:13:06 async_llm_engine.py:61] has_requests_in_progress = await asyncio.wait_for( ERROR 07-31 15:13:06 async_llm_engine.py:61] File "/usr/lib/python3.10/asyncio/tasks.py", line 445, in w...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ne.py:61] File "/usr/local/lib/python3.10/dist-packages/vllm/attention/backends/flash_attn.py", line 339, in forward ERROR 07-31 15:13:06 async_llm_engine.py:61] output[:num_prefill_tokens] = flash_attn_varlen_func( ERR...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
