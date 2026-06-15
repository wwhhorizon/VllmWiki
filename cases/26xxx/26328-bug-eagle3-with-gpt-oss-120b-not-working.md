# vllm-project/vllm#26328: [Bug]: EAGLE3 with gpt-oss-120b not working

| 字段 | 值 |
| --- | --- |
| Issue | [#26328](https://github.com/vllm-project/vllm/issues/26328) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;gemm_linear;model_support;quantization;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | operator;quantization |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: EAGLE3 with gpt-oss-120b not working

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I add the speculative decoding bits, I start getting an error: ``` (APIServer pid=2) DEBUG 10-06 18:54:29 [v1/engine/utils.py:776] Waiting for 1 local, 0 remote core engine proc(s) to start. (Worker_TP1 pid=530) INFO 10-06 18:54:29 [v1/worker/gpu_model_runner.py:2641] Loading drafter model... (Worker_TP0 pid=529) INFO 10-06 18:54:29 [v1/worker/gpu_model_runner.py:2641] Loading drafter model... (Worker_TP1 pid=530) ERROR 10-06 18:54:30 [v1/executor/multiproc_executor.py:597] WorkerProc failed to start. (Worker_TP1 pid=530) ERROR 10-06 18:54:30 [v1/executor/multiproc_executor.py:597] Traceback (most recent call last): (Worker_TP1 pid=530) ERROR 10-06 18:54:30 [v1/executor/multiproc_executor.py:597] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 571, in worker_main (Worker_TP1 pid=530) ERROR 10-06 18:54:30 [v1/executor/multiproc_executor.py:597] worker = WorkerProc(*args, **kwargs) (Worker_TP1 pid=530) ERROR 10-06 18:54:30 [v1/executor/multiproc_executor.py:597] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP1 pid=530) ERROR 10-06 18:54:30 [v1/executor/multiproc_executor.py:597] File "/usr/lo...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: EAGLE3 with gpt-oss-120b not working bug;stale ### Your current environment ### 🐛 Describe the bug When I add the speculative decoding bits, I start getting an error: ``` (APIServer pid=2) DEBUG 10-06 18:54:29 [v...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: executor/multiproc_executor.py:597] self.model_runner.load_model(eep_scale_up=eep_scale_up) (Worker_TP1 pid=530) ERROR 10-06 18:54:30 [v1/executor/multiproc_executor.py:597] File "/usr/local/lib/python3.12/dist-packages...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: EAGLE3 with gpt-oss-120b not working bug;stale ### Your current environment ### 🐛 Describe the bug When I add the speculative decoding bits, I start getting an error: ``` (APIServer pid=2) DEBUG 10-06 18:54:29 [v...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: uvloop/__init__.py", line 109, in run (APIServer pid=2) return __asyncio.run( (APIServer pid=2) ^^^^^^^^^^^^^^ (APIServer pid=2) File "/usr/lib/python3.12/asyncio/runners.py", line 195, in run (APIServer pid=2) return r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: I am just wondering if there is anything I should try. I am using dual H100 GPUs ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
