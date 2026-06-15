# vllm-project/vllm#22453: [Bug]: Qwen3 V1 custom rotary embedding ops breaks torch compile graph

| 字段 | 值 |
| --- | --- |
| Issue | [#22453](https://github.com/vllm-project/vllm/issues/22453) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3 V1 custom rotary embedding ops breaks torch compile graph

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug It seems on V1, by default the rotary_embedding is using the native forward path (pure torch) When we enable the custom op path it will invoke the `forward_cuda` and causes the following error: ``` [1;36m(VllmWorker TP1 pid=26571)[0;0m ERROR 08-07 12:16:03 [multiproc_executor.py:596] Traceback (most recent call last): [1;36m(VllmWorker TP1 pid=26571)[0;0m ERROR 08-07 12:16:03 [multiproc_executor.py:596] File "/app/tritonmrope/vllm/vllm/v1/executor/multiproc_executor.py", line 591, in worker_busy_loop [1;36m(VllmWorker TP1 pid=26571)[0;0m ERROR 08-07 12:16:03 [multiproc_executor.py:596] output = func(*args, **kwargs) [1;36m(VllmWorker TP1 pid=26571)[0;0m ERROR 08-07 12:16:03 [multiproc_executor.py:596] File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 116, in decorate_context [1;36m(VllmWorker TP1 pid=26571)[0;0m ERROR 08-07 12:16:03 [multiproc_executor.py:596] return func(*args, **kwargs) [1;36m(VllmWorker TP1 pid=26571)[0;0m ERROR 08-07 12:16:03 [multiproc_executor.py:596] File "/app/tritonmrope/vllm/vllm/v1/worker/gpu_worker.py", line 243, in determine_available_memory [1;36m(VllmWorke...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Qwen3 V1 custom rotary embedding ops breaks torch compile graph bug;stale ### Your current environment ### 🐛 Describe the bug It seems on V1, by default the rotary_embedding is using the native forward path (pure...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3 V1 custom rotary embedding ops breaks torch compile graph bug;stale ### Your current environment ### 🐛 Describe the bug It seems on V1, by default the rotary_embedding is using the native forward path (pure...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: m ERROR 08-07 12:16:03 [multiproc_executor.py:596] self.model_runner.profile_run() [1;36m(VllmWorker TP1 pid=26571)[0;0m ERROR 08-07 12:16:03 [multiproc_executor.py:596] File "/app/tritonmrope/vllm/vllm/v1/worker/gpu_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: re torch) When we enable the custom op path it will invoke the `forward_cuda` and causes the following error: ``` [1;36m(VllmWorker TP1 pid=26571)[0;0m ERROR 08-07 12:16:03 [multiproc_executor.py:596] Traceback (most...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ug]: Qwen3 V1 custom rotary embedding ops breaks torch compile graph bug;stale ### Your current environment ### 🐛 Describe the bug It seems on V1, by default the rotary_embedding is using the native forward path (pure t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
