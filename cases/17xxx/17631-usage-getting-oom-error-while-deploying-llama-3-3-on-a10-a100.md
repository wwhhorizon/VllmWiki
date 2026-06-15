# vllm-project/vllm#17631: [Usage]: Getting OOM error while deploying llama 3.3 on A10 & A100

| 字段 | 值 |
| --- | --- |
| Issue | [#17631](https://github.com/vllm-project/vllm/issues/17631) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 |  |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error;crash;mismatch;oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Getting OOM error while deploying llama 3.3 on A10 & A100

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm (VllmWorker rank=0 pid=467) (VllmWorker rank=2 pid=504) ERROR 05-04 12:23:00 [multiproc_executor.py:380] WorkerProc hit an exception: %s (VllmWorker rank=2 pid=504) ERROR 05-04 12:23:00 [multiproc_executor.py:380] Traceback (most recent call last): (VllmWorker rank=2 pid=504) ERROR 05-04 12:23:00 [multiproc_executor.py:380] File "/opt/conda/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 375, in worker_busy_loop (VllmWorker rank=2 pid=504) ERROR 05-04 12:23:00 [multiproc_executor.py:380] output = func(*args, **kwargs) (VllmWorker rank=2 pid=504) ERROR 05-04 12:23:00 [multiproc_executor.py:380] ^^^^^^^^^^^^^^^^^^^^^ (VllmWorker rank=2 pid=504) ERROR 05-04 12:23:00 [multiproc_executor.py:380] File "/opt/conda/lib/python3.11/site-packages/vllm/v1/worker/gpu_worker.py", line 216, in compile_or_warm_up_model (VllmWorker rank=2 pid=504) ERROR 05-04 12:23:00 [multiproc_executor.py:380] self.model_runner.capture_model() (VllmWorker rank=2 pid=504) ERROR 05-04 12:23:00 [multiproc_executor.py:380] File "/opt/conda/lib/python3.11/site-packages/vllm/v1/w...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: lib/python3.11/site-packages/vllm/v1/worker/gpu_worker.py", line 216, in compile_or_warm_up_model (VllmWorker rank=2 pid=504) ERROR 05-04 12:23:00 [multiproc_executor.py:380] self.model_runner.capture_model() (VllmWorke...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Usage]: Getting OOM error while deploying llama 3.3 on A10 & A100 usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm (VllmWorker rank=0 pid=467) (Vll...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Getting OOM error while deploying llama 3.3 on A10 & A100 usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm (VllmWorker rank=0 pid=467) (Vll...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: or.py:380] File "/opt/conda/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 745, in _fn (VllmWorker rank=2 pid=504) ERROR 05-04 12:23:00 [multiproc_executor.py:380] return fn(*args, **kwargs) (VllmWorker...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: py:380] File "/opt/conda/lib/python3.11/site-packages/vllm/compilation/backends.py", line 677, in __call__ (VllmWorker rank=2 pid=504) ERROR 05-04 12:23:00 [multiproc_executor.py:380] with torch.cuda.graph(cudagraph, po...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
