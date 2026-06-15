# vllm-project/vllm#8219: [Bug]: vLLM v0.6.1 Instability issue under load.

| 字段 | 值 |
| --- | --- |
| Issue | [#8219](https://github.com/vllm-project/vllm/issues/8219) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | cache;cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM v0.6.1 Instability issue under load.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I did a load test on vLLM v0.6.0 based on the conversation history. I've run the test about 3 times, and I've always encountered the issue. I'm not sure if this issue appears after GPU cache usage reaches 100%, but so far it's been reproduced during load after GPU cache usage reaches 100%. ``` ERROR 09-05 17:22:27 async_llm_engine.py:63] Engine background task failed ERROR 09-05 17:22:27 async_llm_engine.py:63] Traceback (most recent call last): ERROR 09-05 17:22:27 async_llm_engine.py:63] File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 53, in _log_task_completion ERROR 09-05 17:22:27 async_llm_engine.py:63] return_value = task.result() ERROR 09-05 17:22:27 async_llm_engine.py:63] File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 939, in run_engine_loop ERROR 09-05 17:22:27 async_llm_engine.py:63] result = task.result() ERROR 09-05 17:22:27 async_llm_engine.py:63] File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 868, in engine_step ERROR 09-05 17:22:27 async_llm_engine.py:63] request_outputs = await self.engine.step_async(v...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: el_input_tensors ERROR 09-05 17:22:27 async_llm_engine.py:63] return builder.build() # type: ignore ERROR 09-05 17:22:27 async_llm_engine.py:63] File "/usr/local/lib/python3.10/dist-packages/vllm/worker/model_runner.py"...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ceive, sender) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 715, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/routing...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ync ERROR 09-05 17:22:27 async_llm_engine.py:63] output = await self.model_executor.execute_model_async( ERROR 09-05 17:22:27 async_llm_engine.py:63] File "/usr/local/lib/python3.10/dist-packages/vllm/executor/distribut...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ine 868, in engine_step ERROR 09-05 17:22:27 async_llm_engine.py:63] request_outputs = await self.engine.step_async(virtual_engine) ERROR 09-05 17:22:27 async_llm_engine.py:63] File "/usr/local/lib/python3.10/dist-packa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: n=1 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
