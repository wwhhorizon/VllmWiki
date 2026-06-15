# vllm-project/vllm#24803: [Bug]: AttributeError: 'FusedMoE' object has no attribute 'moe' when trying to run Qwen3-Next

| 字段 | 值 |
| --- | --- |
| Issue | [#24803](https://github.com/vllm-project/vllm/issues/24803) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'FusedMoE' object has no attribute 'moe' when trying to run Qwen3-Next

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When trying to run Intel's quantized Qwen3-Next ( https://huggingface.co/Intel/Qwen3-Next-80B-A3B-Instruct-int4-mixed-AutoRound ) I'm getting this error: ``` (Worker_TP0 pid=517059) ERROR 09-13 08:02:17 [multiproc_executor.py:600] WorkerProc failed to start. (Worker_TP0 pid=517059) ERROR 09-13 08:02:17 [multiproc_executor.py:600] Traceback (most recent call last): (Worker_TP0 pid=517059) ERROR 09-13 08:02:17 [multiproc_executor.py:600] File "/home/drros/vllm/.venv/lib/python3.12/site-packages/vllm/v1/executor/multiproc_executor.py", line 574, in worker_main (Worker_TP0 pid=517059) ERROR 09-13 08:02:17 [multiproc_executor.py:600] worker = WorkerProc(*args, **kwargs) (Worker_TP0 pid=517059) ERROR 09-13 08:02:17 [multiproc_executor.py:600] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP0 pid=517059) ERROR 09-13 08:02:17 [multiproc_executor.py:600] File "/home/drros/vllm/.venv/lib/python3.12/site-packages/vllm/v1/executor/multiproc_executor.py", line 440, in __init__ (Worker_TP0 pid=517059) ERROR 09-13 08:02:17 [multiproc_executor.py:600] self.worker.load_model() (Worker_TP0 pid=517059) ERROR 09-13 08:02:17 [multiproc_executor.py:600] File "/...

## 现有链接修复摘要

#24818 Fix: Correct FusedMoE layer reference in auto_round quantization

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: rrent environment ### 🐛 Describe the bug When trying to run Intel's quantized Qwen3-Next ( https://huggingface.co/Intel/Qwen3-Next-80B-A3B-Instruct-int4-mixed-AutoRound ) I'm getting this error: ``` (Worker_TP0 pid=5170...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ributeError: 'FusedMoE' object has no attribute 'moe' when trying to run Qwen3-Next bug;stale ### Your current environment ### 🐛 Describe the bug When trying to run Intel's quantized Qwen3-Next ( https://huggingface.co/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 2/site-packages/vllm/model_executor/layers/quantization/kernels/mixed_precision/bitblas.py", line 177, in process_weights_after_loading (Worker_TP0 pid=517502) ERROR 09-13 08:55:08 [multiproc_executor.py:600] None if qu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: usedMoE' object has no attribute 'moe' when trying to run Qwen3-Next bug;stale ### Your current environment ### 🐛 Describe the bug When trying to run Intel's quantized Qwen3-Next ( https://huggingface.co/Intel/Qwen3-Nex...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 95` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#24818](https://github.com/vllm-project/vllm/pull/24818) | closes_keyword | 0.95 | Fix: Correct FusedMoE layer reference in auto_round quantization | fix the issue #24803 Model：[Qwen3-Next-80B-A3B-Instruct-int4-mixed AutoRound](https://huggingface.co/Intel/Qwen3-Next-80B-A3B-Instruct-int4-mixed-AutoRound) ## Test Plan Hardware |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
