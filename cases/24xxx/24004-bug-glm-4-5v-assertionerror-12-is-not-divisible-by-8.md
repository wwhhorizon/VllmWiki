# vllm-project/vllm#24004: [Bug]: GLM-4.5V - AssertionError: 12 is not divisible by 8

| 字段 | 值 |
| --- | --- |
| Issue | [#24004](https://github.com/vllm-project/vllm/issues/24004) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GLM-4.5V - AssertionError: 12 is not divisible by 8

### Issue 正文摘录

### Your current environment For GLM-4.5V, startup is failing with error `AssertionError: 12 is not divisible by 8` vLLM: `v0.10.1.1` transformers: `transformers-v4.55.0-GLM-4.5V-preview` tensor_parallel_size=8 pipeline_parallel_size=1 ### 🐛 Describe the bug Full stack trace During startup ``` #033[1;36m(VllmWorker TP2 pid=415)#033[0;0m ERROR 08-31 04:18:45 [multiproc_executor.py:559] WorkerProc failed to start.#015 -- #033[1;36m(VllmWorker TP2 pid=415)#033[0;0m ERROR 08-31 04:18:45 [multiproc_executor.py:559] Traceback (most recent call last):#015 #033[1;36m(VllmWorker TP2 pid=415)#033[0;0m ERROR 08-31 04:18:45 [multiproc_executor.py:559] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 533, in worker_main#015 #033[1;36m(VllmWorker TP2 pid=415)#033[0;0m ERROR 08-31 04:18:45 [multiproc_executor.py:559] worker = WorkerProc(*args, **kwargs)#015 #033[1;36m(VllmWorker TP2 pid=415)#033[0;0m ERROR 08-31 04:18:45 [multiproc_executor.py:559] ^^^^^^^^^^^^^^^^^^^^^^^^^^^#015 #033[1;36m(VllmWorker TP2 pid=415)#033[0;0m ERROR 08-31 04:18:45 [multiproc_executor.py:559] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.p...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 0m ERROR 08-31 04:18:45 [multiproc_executor.py:559] self.worker.load_model()#015 #033[1;36m(VllmWorker TP2 pid=415)#033[0;0m ERROR 08-31 04:18:45 [multiproc_executor.py:559] File "/usr/local/lib/python3.12/dist-packages...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 4:18:45 [multiproc_executor.py:559] self.model_runner.load_model(eep_scale_up=eep_scale_up)#015 #033[1;36m(VllmWorker TP2 pid=415)#033[0;0m ERROR 08-31 04:18:45 [multiproc_executor.py:559] File "/usr/local/lib/python3.1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 033[0;0m ERROR 08-31 04:18:45 [multiproc_executor.py:559] Glm4vVisionBlock(#015 #033[1;36m(VllmWorker TP2 pid=415)#033[0;0m ERROR 08-31 04:18:45 [multiproc_executor.py:559] File "/usr/local/lib/python3.12/dist-packages/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: GLM-4.5V - AssertionError: 12 is not divisible by 8 bug;stale ### Your current environment For GLM-4.5V, startup is failing with error `AssertionError: 12 is not divisible by 8` vLLM: `v0.10.1.1` transformers: `t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
