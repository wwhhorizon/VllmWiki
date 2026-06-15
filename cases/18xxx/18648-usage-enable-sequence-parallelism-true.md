# vllm-project/vllm#18648: [Usage]: enable_sequence_parallelism=True

| 字段 | 值 |
| --- | --- |
| Issue | [#18648](https://github.com/vllm-project/vllm/issues/18648) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;frontend_api;model_support |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;kernel;operator |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: enable_sequence_parallelism=True

### Issue 正文摘录

### Your current environment L40 & H20 ### How would you like to use vllm (VllmWorker rank=0 pid=185081) ERROR 05-24 13:52:18 [multiproc_executor.py:522] WorkerProc hit an exception. (VllmWorker rank=0 pid=185081) ERROR 05-24 13:52:18 [multiproc_executor.py:522] Traceback (most recent call last): (VllmWorker rank=0 pid=185081) ERROR 05-24 13:52:18 [multiproc_executor.py:522] File "/data/private/vllm/vllm/v1/executor/multiproc_executor.py", line 517, in worker_busy_loop (VllmWorker rank=0 pid=185081) ERROR 05-24 13:52:18 [multiproc_executor.py:522] output = func(*args, **kwargs) (VllmWorker rank=0 pid=185081) ERROR 05-24 13:52:18 [multiproc_executor.py:522] File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 116, in decorate_context (VllmWorker rank=0 pid=185081) ERROR 05-24 13:52:18 [multiproc_executor.py:522] return func(*args, **kwargs) (VllmWorker rank=0 pid=185081) ERROR 05-24 13:52:18 [multiproc_executor.py:522] File "/data/private/vllm/vllm/v1/worker/gpu_worker.py", line 185, in determine_available_memory (VllmWorker rank=0 pid=185081) ERROR 05-24 13:52:18 [multiproc_executor.py:522] self.model_runner.profile_run() (VllmWorker rank=0 pid=185081) E...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 5081) ERROR 05-24 13:52:18 [multiproc_executor.py:522] output = self.compiled_callable(*args, **kwargs) (VllmWorker rank=0 pid=185081) ERROR 05-24 13:52:18 [multiproc_executor.py:522] File "/usr/local/lib/python3.10/dis...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: =0 pid=185081) ERROR 05-24 13:52:18 [multiproc_executor.py:522] self.model_runner.profile_run() (VllmWorker rank=0 pid=185081) ERROR 05-24 13:52:18 [multiproc_executor.py:522] File "/data/private/vllm/vllm/v1/worker/gpu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Usage]: enable_sequence_parallelism=True usage ### Your current environment L40 & H20 ### How would you like to use vllm (VllmWorker rank=0 pid=185081) ERROR 05-24 13:52:18 [multiproc_executor.py:522] WorkerProc hit an...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ) ERROR 05-24 13:52:18 [multiproc_executor.py:522] self.model_runner.profile_run() (VllmWorker rank=0 pid=185081) ERROR 05-24 13:52:18 [multiproc_executor.py:522] File "/data/private/vllm/vllm/v1/worker/gpu_model_runner...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: =0 pid=185081) ERROR 05-24 13:52:18 [multiproc_executor.py:522] self.dispatch_table[inst.opcode](self, inst) (VllmWorker rank=0 pid=185081) ERROR 05-24 13:52:18 [multiproc_executor.py:522] File "/usr/local/lib/python3.1...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
