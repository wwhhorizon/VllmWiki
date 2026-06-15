# vllm-project/vllm#1765: Task was killed due to the node running low on memory 

| 字段 | 值 |
| --- | --- |
| Issue | [#1765](https://github.com/vllm-project/vllm/issues/1765) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | crash;oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Task was killed due to the node running low on memory 

### Issue 正文摘录

In my case , I deployed the vllm service on 2 GPUs A800. but when I doing mutiple requests, I meet the ray OOM error. Could you please help check this problem? my model is fine-tuned llama-70b my transformers version is 4.34.1 my cuda version is 11.8, V11.8.89 my vllm version is 0.2.1.post1 When I was doing muti requests, An error came. ERROR: Exception in ASGI application Traceback (most recent call last): File "/usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine.py", line 28, in _raise_exception_on_finish task.result() File "/usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine.py", line 351, in run_engine_loop has_requests_in_progress = await self.engine_step() File "/usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine.py", line 330, in engine_step request_outputs = await self.engine.step_async() File "/usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine.py", line 191, in step_async output = await self._run_workers_async( File "/usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine.py", line 220, in _run_workers_async all_outputs = await asyncio.gather(*all_outputs) File "/usr/lib/python3.8/asyncio/tasks.p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: elp check this problem? my model is fine-tuned llama-70b my transformers version is 4.34.1 my cuda version is 11.8, V11.8.89 my vllm version is 0.2.1.post1 When I was doing muti requests, An error came. ERROR: Exception...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Task was killed due to the node running low on memory stale In my case , I deployed the vllm service on 2 GPUs A800. but when I doing mutiple requests, I meet the ray OOM error. Could you please help check this problem?...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: receive, send) File "/usr/local/lib/python3.8/dist-packages/starlette/routing.py", line 718, in __call__ await route.handle(scope, receive, send) File "/usr/local/lib/python3.8/dist-packages/starlette/routing.py", line...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: m? my model is fine-tuned llama-70b my transformers version is 4.34.1 my cuda version is 11.8, V11.8.89 my vllm version is 0.2.1.post1 When I was doing muti requests, An error came. ERROR: Exception in ASGI application...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: , I meet the ray OOM error. Could you please help check this problem? my model is fine-tuned llama-70b my transformers version is 4.34.1 my cuda version is 11.8, V11.8.89 my vllm version is 0.2.1.post1 When I was doing...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
