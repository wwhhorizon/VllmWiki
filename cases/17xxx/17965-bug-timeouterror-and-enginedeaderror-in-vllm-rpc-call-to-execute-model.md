# vllm-project/vllm#17965: [Bug]: TimeoutError and EngineDeadError in vLLM: RPC Call to execute_model Timed Out and EngineCore Failure

| 字段 | 值 |
| --- | --- |
| Issue | [#17965](https://github.com/vllm-project/vllm/issues/17965) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 39; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TimeoutError and EngineDeadError in vLLM: RPC Call to execute_model Timed Out and EngineCore Failure

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` File "/root/anaconda3/envs/vllm_0.8.5/lib/python3.12/contextlib.py", line 137, in __enter__ return next(self.gen) ^^^^^^^^^^^^^^ File "/root/anaconda3/envs/vllm_0.8.5/lib/python3.12/site-packages/vllm/distributed/device_communicators/shm_broadcast.py", line 443, in acquire_read raise TimeoutError TimeoutError The above exception was the direct cause of the following exception: Traceback (most recent call last): File "/root/anaconda3/envs/vllm_0.8.5/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/root/anaconda3/envs/vllm_0.8.5/lib/python3.12/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/root/anaconda3/envs/vllm_0.8.5/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 400, in run_engine_core raise e File "/root/anaconda3/envs/vllm_0.8.5/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 389, in run_engine_core engine_core.run_busy_loop() File "/root/anaconda3/envs/vllm_0.8.5/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 413, in run_busy_loop self._process_engine_step() File "/root/anaconda3/envs/vllm_0.8.5/lib/pyt...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support cuda;operator;triton build_error;crash env_dependency Your current envir...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: TimeoutError and EngineDeadError in vLLM: RPC Call to execute_model Timed Out and EngineCore Failure bug ### Your current environment ### 🐛 Describe the bug ``` File "/root/anaconda3/envs/vllm_0.8.5/lib/python3.1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: re.py", line 203, in step output = self.model_executor.execute_model(scheduler_output) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/root/anaconda3/envs/vllm_0.8.5/lib/python3.12/site-packages/vllm/v1/execu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: buted_parallel;frontend_api;hardware_porting;model_support cuda;operator;triton build_error;crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
