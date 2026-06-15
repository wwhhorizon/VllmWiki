# vllm-project/vllm#34869: [Bug]: Deepseek V3.1 NVFP4 Weight Loading Fails

| 字段 | 值 |
| --- | --- |
| Issue | [#34869](https://github.com/vllm-project/vllm/issues/34869) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Deepseek V3.1 NVFP4 Weight Loading Fails

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` vllm serve nvidia/DeepSeek-V3.1-NVFP4 -tp=4 ``` ``` Loading safetensors checkpoint shards: 0% Completed | 0/163 [00:00<?, ?it/s] ERROR 02-19 04:18:41 [multiproc_executor.py:783] WorkerProc failed to start. ERROR 02-19 04:18:41 [multiproc_executor.py:783] Traceback (most recent call last): ERROR 02-19 04:18:41 [multiproc_executor.py:783] File "/vllm/vllm/v1/executor/multiproc_executor.py", line 754, in worker_main ERROR 02-19 04:18:41 [multiproc_executor.py:783] worker = WorkerProc(*args, **kwargs) ERROR 02-19 04:18:41 [multiproc_executor.py:783] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 02-19 04:18:41 [multiproc_executor.py:783] File "/vllm/vllm/v1/executor/multiproc_executor.py", line 580, in __init__ ERROR 02-19 04:18:41 [multiproc_executor.py:783] self.worker.load_model() ERROR 02-19 04:18:41 [multiproc_executor.py:783] File "/vllm/vllm/v1/worker/gpu_worker.py", line 324, in load_model ERROR 02-19 04:18:41 [multiproc_executor.py:783] self.model_runner.load_model(eep_scale_up=eep_scale_up) ERROR 02-19 04:18:41 [multiproc_executor.py:783] File "/vllm/vllm/v1/worker/gpu_model_runner.py", line 4147, in load_model ERROR 02-19 04:18:41...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Deepseek V3.1 NVFP4 Weight Loading Fails bug ### Your current environment ### 🐛 Describe the bug ``` vllm serve nvidia/DeepSeek-V3.1-NVFP4 -tp=4 ``` ``` Loading safetensors checkpoint shards: 0% Completed | 0/163...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: __ ERROR 02-19 04:18:41 [multiproc_executor.py:783] self.worker.load_model() ERROR 02-19 04:18:41 [multiproc_executor.py:783] File "/vllm/vllm/v1/worker/gpu_worker.py", line 324, in load_model ERROR 02-19 04:18:41 [mult...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: at ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
