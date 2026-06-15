# vllm-project/vllm#9783: [Bug]: Attempting to profile VLLM with TPU errors

| 字段 | 值 |
| --- | --- |
| Issue | [#9783](https://github.com/vllm-project/vllm/issues/9783) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Attempting to profile VLLM with TPU errors

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am running a docker container to test out profiling and `vllm serve` errors when asked for a profile. Profiling should return 404 if it's not supported yet (but I would love to see it get some traction!). Error stack trace: ``` ERROR 10-29 01:21:42 engine.py:165] AttributeError("'TPUExecutor' object has no attribute '_run_workers'") ERROR 10-29 01:21:42 engine.py:165] Traceback (most recent call last): ERROR 10-29 01:21:42 engine.py:165] File "/workspace/vllm/vllm/engine/multiprocessing/engine.py", line 163, in start ERROR 10-29 01:21:42 engine.py:165] self.run_engine_loop() ERROR 10-29 01:21:42 engine.py:165] File "/workspace/vllm/vllm/engine/multiprocessing/engine.py", line 223, in run_engine_loop ERROR 10-29 01:21:42 engine.py:165] self.handle_new_input() ERROR 10-29 01:21:42 engine.py:165] File "/workspace/vllm/vllm/engine/multiprocessing/engine.py", line 274, in handle_new_input ERROR 10-29 01:21:42 engine.py:165] raise e ERROR 10-29 01:21:42 engine.py:165] File "/workspace/vllm/vllm/engine/multiprocessing/engine.py", line 264, in handle_new_input ERROR 10-29 01:21:42 engine.py:165] self...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Model Input Dumps _No response_ ### 🐛 Describe the bug I am running a docker container to test out profiling and `vllm serve` errors when asked for a profile. Profiling should return 404 if it's not supported yet (but I...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: Attempting to profile VLLM with TPU errors bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am running a docker container to test out profiling and `vllm serve`...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ceive, sender) File "/usr/local/lib/python3.10/site-packages/starlette/routing.py", line 715, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.10/site-packages/starlette/routing...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: file VLLM with TPU errors bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am running a docker container to test out profiling and `vllm serve` errors when asked for a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Attempting to profile VLLM with TPU errors bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am running a docker container to test out profiling and `vllm serve`...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
