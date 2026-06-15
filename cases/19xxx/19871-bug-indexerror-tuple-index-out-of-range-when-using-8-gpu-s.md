# vllm-project/vllm#19871: [Bug]: 'IndexError: tuple index out of range' when using 8 gpu's

| 字段 | 值 |
| --- | --- |
| Issue | [#19871](https://github.com/vllm-project/vllm/issues/19871) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 'IndexError: tuple index out of range' when using 8 gpu's

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Greetings, I have 8 H100 80G. When running the command: `vllm serve gaunernst/gemma-3-27b-it-int4-awq --gpu-memory-utilization 0.95 --max-model-len 6144 --limit-mm-per-prompt image=0,video=0 --pipeline-parallel-size 2 --dtype bfloat16 --port 8000 --served_model_name gemma-3-27b-it` , everything runs fine but when setting the --pipeline-parallel-size to 8, I'm seeing following error when running a simple curl (as described in the vllm quickstart) ``` (VllmWorker rank=1 pid=37378) ERROR 06-19 14:49:55 [multiproc_executor.py:527] WorkerProc hit an exception. (VllmWorker rank=1 pid=37378) ERROR 06-19 14:49:55 [multiproc_executor.py:527] Traceback (most recent call last): (VllmWorker rank=1 pid=37378) ERROR 06-19 14:49:55 [multiproc_executor.py:527] File "/root/venv/lib/python3.12/site-packages/vllm/v1/executor/multiproc_executor.py", line 522, in worker_busy_loop (VllmWorker rank=1 pid=37378) ERROR 06-19 14:49:55 [multiproc_executor.py:527] output = func(*args, **kwargs) (VllmWorker rank=1 pid=37378) ERROR 06-19 14:49:55 [multiproc_executor.py:527] ^^^^^^^^^^^^^^^^^^^^^ (VllmWorker rank=1 pid=37378) ERROR 06-19 14:49:55 [multiproc_ex...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: 00 80G. When running the command: `vllm serve gaunernst/gemma-3-27b-it-int4-awq --gpu-memory-utilization 0.95 --max-model-len 6144 --limit-mm-per-prompt image=0,video=0 --pipeline-parallel-size 2 --dtype bfloat16 --port...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: 'IndexError: tuple index out of range' when using 8 gpu's bug;stale ### Your current environment ### 🐛 Describe the bug Greetings, I have 8 H100 80G. When running the command: `vllm serve gaunernst/gemma-3-27b-it...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;gemm;operator;qua...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: our current environment ### 🐛 Describe the bug Greetings, I have 8 H100 80G. When running the command: `vllm serve gaunernst/gemma-3-27b-it-int4-awq --gpu-memory-utilization 0.95 --max-model-len 6144 --limit-mm-per-prom...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: s, I have 8 H100 80G. When running the command: `vllm serve gaunernst/gemma-3-27b-it-int4-awq --gpu-memory-utilization 0.95 --max-model-len 6144 --limit-mm-per-prompt image=0,video=0 --pipeline-parallel-size 2 --dtype b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
