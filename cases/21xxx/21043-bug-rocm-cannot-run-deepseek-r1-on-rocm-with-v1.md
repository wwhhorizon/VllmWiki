# vllm-project/vllm#21043: [Bug]: [ROCm]Cannot run DeepSeek-R1 on ROCm with V1

| 字段 | 值 |
| --- | --- |
| Issue | [#21043](https://github.com/vllm-project/vllm/issues/21043) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel |
| 症状 | crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [ROCm]Cannot run DeepSeek-R1 on ROCm with V1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug when I run **deepseek-r1 with V1 on ROCm6.3, TP=8, PP=4**, got the error below: Traceback (most recent call last): File "/opt/conda/envs/py_3.10/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/opt/conda/envs/py_3.10/lib/python3.10/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/opt/conda/envs/py_3.10/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 590, in run_engine_core raise e File "/opt/conda/envs/py_3.10/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 579, in run_engine_core engine_core.run_busy_loop() File "/opt/conda/envs/py_3.10/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 606, in run_busy_loop self._process_engine_step() File "/opt/conda/envs/py_3.10/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 631, in _process_engine_step outputs, model_executed = self.step_fn() File "/opt/conda/envs/py_3.10/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 267, in step_with_batch_queue future = self.model_executor.execute_model(scheduler_output) File "/opt/conda/envs/py_3.10/lib/python3.10/site-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ted_executor.py", line 57, in execute_model self.forward_dag = self._compiled_ray_dag(enable_asyncio=False) File "/opt/conda/envs/py_3.10/lib/python3.10/site-packages/vllm/executor/ray_distributed_executor.py", line 614...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: [ROCm]Cannot run DeepSeek-R1 on ROCm with V1 bug;stale ### Your current environment ### 🐛 Describe the bug when I run **deepseek-r1 with V1 on ROCm6.3, TP=8, PP=4**, got the error below: Traceback (most recent ca...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: [ROCm]Cannot run DeepSeek-R1 on ROCm with V1 bug;stale ### Your current environment ### 🐛 Describe the bug when I run **deepseek-r1 with V1 on ROCm6.3, TP=8, PP=4**, got the error below: Traceback (most recent ca...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ute_model self.forward_dag = self._compiled_ray_dag(enable_asyncio=False) File "/opt/conda/envs/py_3.10/lib/python3.10/site-packages/vllm/executor/ray_distributed_executor.py", line 614, in _compiled_ray_dag return forw...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: /vllm/v1/engine/core.py", line 631, in _process_engine_step outputs, model_executed = self.step_fn() File "/opt/conda/envs/py_3.10/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 267, in step_with_batch_queue...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
