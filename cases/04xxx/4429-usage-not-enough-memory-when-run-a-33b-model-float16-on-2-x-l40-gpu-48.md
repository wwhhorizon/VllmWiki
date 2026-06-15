# vllm-project/vllm#4429: [Usage]: Not enough memory when run a 33b model float16 on 2 x L40 GPU (48G) 

| 字段 | 值 |
| --- | --- |
| Issue | [#4429](https://github.com/vllm-project/vllm/issues/4429) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Not enough memory when run a 33b model float16 on 2 x L40 GPU (48G) 

### Issue 正文摘录

### Your current environment Not enough memory when run deepseek-coder-33b-instruct model on two L40 GPUs (48G) with vllm 0.4.1. Also tried --enforce-eager --gpu-memory-utilization, did not help. ``` python -m vllm.entrypoints.openai.api_server --dtype float16 --trust-remote-code --model /models/deepseek-coder-33b-instruct --served-model-name deepseek-coder-33b-instruct --port 8000 --host 0.0.0.0 --tensor-parallel-size 2 ``` It reports error: ``` ERROR 04-28 15:55:45 worker_base.py:157] Error executing method initialize_cache. This might cause deadlock in distributed execution. ERROR 04-28 15:55:45 worker_base.py:157] Traceback (most recent call last): ERROR 04-28 15:55:45 worker_base.py:157] File "/root/miniconda3/envs/deepseek/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 149, in execute_method ERROR 04-28 15:55:45 worker_base.py:157] return executor(*args, **kwargs) ERROR 04-28 15:55:45 worker_base.py:157] File "/root/miniconda3/envs/deepseek/lib/python3.10/site-packages/vllm/worker/worker.py", line 171, in initialize_cache ERROR 04-28 15:55:45 worker_base.py:157] raise_if_cache_size_invalid(num_gpu_blocks, ERROR 04-28 15:55:45 worker_base.py:157] File "/root/m...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Usage]: Not enough memory when run a 33b model float16 on 2 x L40 GPU (48G) usage;stale ### Your current environment Not enough memory when run deepseek-coder-33b-instruct model on two L40 GPUs (48G) with vllm 0.4.1. A...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: t enough memory when run a 33b model float16 on 2 x L40 GPU (48G) usage;stale ### Your current environment Not enough memory when run deepseek-coder-33b-instruct model on two L40 GPUs (48G) with vllm 0.4.1. Also tried -...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: 45 worker_base.py:157] raise ValueError("No available memory for the cache blocks. " ERROR 04-28 15:55:45 worker_base.py:157] ValueError: No available memory for the cache blocks. Try increasing `gpu_memory_utilization`...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: -28 15:55:45 worker_base.py:157] raise_if_cache_size_invalid(num_gpu_blocks, ERROR 04-28 15:55:45 worker_base.py:157] File "/root/miniconda3/envs/deepseek/lib/python3.10/site-packages/vllm/worker/worker.py", line 335, i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: Not enough memory when run a 33b model float16 on 2 x L40 GPU (48G) usage;stale ### Your current environment Not enough memory when run deepseek-coder-33b-instruct model on two L40 GPUs (48G) with vllm 0.4.1. A...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
