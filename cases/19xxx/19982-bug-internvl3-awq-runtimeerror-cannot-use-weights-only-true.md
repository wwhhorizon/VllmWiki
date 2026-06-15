# vllm-project/vllm#19982: [Bug]: InternVL3 awq RuntimeError: Cannot use ``weights_only=True``

| 字段 | 值 |
| --- | --- |
| Issue | [#19982](https://github.com/vllm-project/vllm/issues/19982) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: InternVL3 awq RuntimeError: Cannot use ``weights_only=True``

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug when running: `vllm serve OpenGVLab/InternVL3-38B-AWQ --disable-log-requests -tp 2 --limit-mm-per-prompt '{"images": 5, "videos": 0}' --max-model-len 2000 --gpu-memory-utilization 0.85 --quantization awq --dtype half --trust-remote-code` right after `Loading pt checkpoint shards` this Runtime error occurs ``` vllm-internvl-app-1 | (VllmWorker rank=0 pid=123) vllm-internvl-app-1 | (VllmWorker rank=0 pid=123) ERROR 06-23 05:08:54 [multiproc_executor.py:435] WorkerProc failed to start. vllm-internvl-app-1 | (VllmWorker rank=0 pid=123) ERROR 06-23 05:08:54 [multiproc_executor.py:435] Traceback (most recent call last): vllm-internvl-app-1 | (VllmWorker rank=0 pid=123) ERROR 06-23 05:08:54 [multiproc_executor.py:435] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 409, in worker_main vllm-internvl-app-1 | (VllmWorker rank=0 pid=123) ERROR 06-23 05:08:54 [multiproc_executor.py:435] worker = WorkerProc(*args, **kwargs) vllm-internvl-app-1 | (VllmWorker rank=0 pid=123) ERROR 06-23 05:08:54 [multiproc_executor.py:435] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ vllm-internvl-app-1 | (VllmWorker rank=0 pid=123) E...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: InternVL3 awq RuntimeError: Cannot use ``weights_only=True`` bug ### Your current environment ### 🐛 Describe the bug when running: `vllm serve OpenGVLab/InternVL3-38B-AWQ --disable-log-requests -tp 2 --limit-mm-p...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ": 5, "videos": 0}' --max-model-len 2000 --gpu-memory-utilization 0.85 --quantization awq --dtype half --trust-remote-code` right after `Loading pt checkpoint shards` this Runtime error occurs ``` vllm-internvl-app-1 |...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 1`. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: the default value of the `weights_only` argument in `torch.load` from `False` to `True`. Re-running `torch.load` with `weights_only` set to `False` will likely succeed, but it can result in arbitrary code execution. Do...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ug when running: `vllm serve OpenGVLab/InternVL3-38B-AWQ --disable-log-requests -tp 2 --limit-mm-per-prompt '{"images": 5, "videos": 0}' --max-model-len 2000 --gpu-memory-utilization 0.85 --quantization awq --dtype half...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
