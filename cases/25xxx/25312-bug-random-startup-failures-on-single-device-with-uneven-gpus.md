# vllm-project/vllm#25312: [Bug]: Random startup failures on single device with uneven GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#25312](https://github.com/vllm-project/vllm/issues/25312) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Random startup failures on single device with uneven GPUs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I was running `vllm serve Qwen3-235B-A22B-Instruct` with 12 GPUs on one machine, random RuntimeError occur: ``` (Worker_PP1 pid=189019) ERROR 09-20 20:27:35 [multiproc_executor.py:654] WorkerProc hit an exception. (Worker_PP1 pid=189019) ERROR 09-20 20:27:35 [multiproc_executor.py:654] Traceback (most recent call last): (Worker_PP1 pid=189019) ERROR 09-20 20:27:35 [multiproc_executor.py:654] File "/root/swift_50/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 649, in worker_busy_loop (Worker_PP1 pid=189019) ERROR 09-20 20:27:35 [multiproc_executor.py:654] output = func(*args, **kwargs) (Worker_PP1 pid=189019) ERROR 09-20 20:27:35 [multiproc_executor.py:654] ^^^^^^^^^^^^^^^^^^^^^ (Worker_PP1 pid=189019) ERROR 09-20 20:27:35 [multiproc_executor.py:654] File "/root/swift_50/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context (Worker_PP1 pid=189019) ERROR 09-20 20:27:35 [multiproc_executor.py:654] return func(*args, **kwargs) (Worker_PP1 pid=189019) ERROR 09-20 20:27:35 [multiproc_executor.py:654] ^^^^^^^^^^^^^^^^^^^^^ (Worker_PP1 pid=189019) ERROR 09-20 20:27:35 [mu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 9019) ERROR 09-20 20:27:35 [multiproc_executor.py:654] output = self.compiled_callable(*args, **kwargs) (Worker_PP1 pid=189019) ERROR 09-20 20:27:35 [multiproc_executor.py:654] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (W...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 54] File "/root/swift_50/lib/python3.11/site-packages/vllm/compilation/cuda_graph.py", line 119, in __call__ (Worker_PP1 pid=189019) ERROR 09-20 20:27:35 [multiproc_executor.py:654] return self.runnable(*args, **kwargs)...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Random startup failures on single device with uneven GPUs bug;stale ### Your current environment ### 🐛 Describe the bug When I was running `vllm serve Qwen3-235B-A22B-Instruct` with 12 GPUs on one machine, random...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ) ERROR 09-20 20:27:35 [multiproc_executor.py:654] self.model_runner.profile_run() (Worker_PP1 pid=189019) ERROR 09-20 20:27:35 [multiproc_executor.py:654] File "/root/swift_50/lib/python3.11/site-packages/vllm/v1/worke...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ot/swift_50/lib/python3.11/site-packages/vllm/compilation/cuda_piecewise_backend.py", line 90, in __call__ (Worker_PP1 pid=189019) ERROR 09-20 20:27:35 [multiproc_executor.py:654] return self.compiled_graph_for_general_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
