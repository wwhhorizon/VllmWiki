# vllm-project/vllm#25039: [Bug]: Failed to run qwen3 next fp8 with TP on Ampere GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#25039](https://github.com/vllm-project/vllm/issues/25039) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;fp8;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Failed to run qwen3 next fp8 with TP on Ampere GPU

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Got following error using tp=4. ``` (Worker_TP1_EP1 pid=910004) ERROR 09-17 11:07:00 [multiproc_executor.py:597] WorkerProc failed to start. (Worker_TP1_EP1 pid=910004) ERROR 09-17 11:07:00 [multiproc_executor.py:597] Traceback (most recent call last): (Worker_TP1_EP1 pid=910004) ERROR 09-17 11:07:00 [multiproc_executor.py:597] File "/data/lijinghui/uv_projects/.venv/lib/python3.13/site-packages/vllm/v1/executor/multiproc_executor.py", line 571, in worker_main (Worker_TP1_EP1 pid=910004) ERROR 09-17 11:07:00 [multiproc_executor.py:597] worker = WorkerProc(*args, **kwargs) (Worker_TP1_EP1 pid=910004) ERROR 09-17 11:07:00 [multiproc_executor.py:597] File "/data/lijinghui/uv_projects/.venv/lib/python3.13/site-packages/vllm/v1/executor/multiproc_executor.py", line 437, in __init__ (Worker_TP1_EP1 pid=910004) ERROR 09-17 11:07:00 [multiproc_executor.py:597] self.worker.load_model() (Worker_TP1_EP1 pid=910004) ERROR 09-17 11:07:00 [multiproc_executor.py:597] ~~~~~~~~~~~~~~~~~~~~~~^^ (Worker_TP1_EP1 pid=910004) ERROR 09-17 11:07:00 [multiproc_executor.py:597] File "/data/lijinghui/uv_projects/.venv/lib/python3.13/site-packages/vllm/v1/w...

## 现有链接修复摘要

#68 Fix a bug in attention kernel

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Failed to run qwen3 next fp8 with TP on Ampere GPU bug;stale ### Your current environment ### 🐛 Describe the bug Got following error using tp=4. ``` (Worker_TP1_EP1 pid=910004) ERROR 09-17 11:07:00 [multiproc_exe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Failed to run qwen3 next fp8 with TP on Ampere GPU bug;stale ### Your current environment ### 🐛 Describe the bug Got following error using tp=4. ``` (Worker_TP1_EP1 pid=910004) ERROR 09-17 11:07:00 [multiproc_exe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding cuda;fp8;operator;quantization;triton...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Failed to run qwen3 next fp8 with TP on Ampere GPU bug;stale ### Your current environment ### 🐛 Describe the bug Got following error using tp=4. ``` (Worker_TP1_EP1 pid=910004) ERROR 09-17 11:07:00 [multiproc_exe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Failed to run qwen3 next fp8 with TP on Ampere GPU bug;stale ### Your current environment ### 🐛 Describe the bug Got following error using tp=4. ``` (Worker_TP1_EP1 pid=910004) ERROR 09-17 11:07:00 [multiproc_exe...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#68](https://github.com/vllm-project/vllm/pull/68) | mentioned | 0.45 | Fix a bug in attention kernel | https://huggingface.co/devquasar/qwen.qwen3-next-80b-a3b-instruct-fp8/discussions/1#68c7c89fd0c6560e15443c6e) ### before submitting a new issue... - [x] make sure you already sear… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
