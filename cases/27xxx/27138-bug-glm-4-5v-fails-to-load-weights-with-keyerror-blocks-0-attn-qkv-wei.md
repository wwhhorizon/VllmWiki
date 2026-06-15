# vllm-project/vllm#27138: [Bug] GLM-4.5V fails to load weights with KeyError: 'blocks.0.attn.qkv.weight'

| 字段 | 值 |
| --- | --- |
| Issue | [#27138](https://github.com/vllm-project/vllm/issues/27138) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] GLM-4.5V fails to load weights with KeyError: 'blocks.0.attn.qkv.weight'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm seeing a KeyError during `load_weights`: ``` (Worker_TP0 pid=2263963) ERROR 10-18 03:20:36 [multiproc_executor.py:628] WorkerProc failed to start. (Worker_TP0 pid=2263963) ERROR 10-18 03:20:36 [multiproc_executor.py:628] Traceback (most recent call last): (Worker_TP0 pid=2263963) ERROR 10-18 03:20:36 [multiproc_executor.py:628] File "/home/richard/Work/vllm-serve/_venv/lib/python3.10/site-packages/vllm/v1/executor/multiproc_executor.py", line 602, in worker_main (Worker_TP0 pid=2263963) ERROR 10-18 03:20:36 [multiproc_executor.py:628] worker = WorkerProc(*args, **kwargs) (Worker_TP0 pid=2263963) ERROR 10-18 03:20:36 [multiproc_executor.py:628] File "/home/richard/Work/vllm-serve/_venv/lib/python3.10/site-packages/vllm/v1/executor/multiproc_executor.py", line 457, in __init__ (Worker_TP0 pid=2263963) ERROR 10-18 03:20:36 [multiproc_executor.py:628] self.worker.load_model() (Worker_TP0 pid=2263963) ERROR 10-18 03:20:36 [multiproc_executor.py:628] File "/home/richard/Work/vllm-serve/_venv/lib/python3.10/site-packages/vllm/v1/worker/gpu_worker.py", line 229, in load_model (Worker_TP0 pid=2263963) ERROR 10-18 03:20:36 [multiproc_e...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: 3:20:36 [multiproc_executor.py:628] self.model_runner.load_model(eep_scale_up=eep_scale_up) (Worker_TP0 pid=2263963) ERROR 10-18 03:20:36 [multiproc_executor.py:628] File "/home/richard/Work/vllm-serve/_venv/lib/python3...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: 3) ERROR 10-18 03:20:36 [multiproc_executor.py:628] self.worker.load_model() (Worker_TP0 pid=2263963) ERROR 10-18 03:20:36 [multiproc_executor.py:628] File "/home/richard/Work/vllm-serve/_venv/lib/python3.10/site-packag...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_deco...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 4.5V fails to load weights with KeyError: 'blocks.0.attn.qkv.weight' bug;stale ### Your current environment ### 🐛 Describe the bug I'm seeing a KeyError during `load_weights`: ``` (Worker_TP0 pid=2263963) ERROR 10-18 03...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
