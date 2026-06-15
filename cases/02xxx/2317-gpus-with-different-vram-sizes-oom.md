# vllm-project/vllm#2317: GPUs with different VRAM sizes, OOM

| 字段 | 值 |
| --- | --- |
| Issue | [#2317](https://github.com/vllm-project/vllm/issues/2317) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;operator |
| 症状 | oom |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> GPUs with different VRAM sizes, OOM

### Issue 正文摘录

I have a 24Gb 3090 and a 8Gb 3070 GPU that I would like to combine for inference purposes. I tried running ```python -u -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8000 --model teknium/OpenHermes-2-Mistral-7B --tensor-parallel-size 2``` but it seems to me that the code is trying to split the load uniformly between the two GPUs, and I get an OOM error on the smaller one. Is there a way I can specify the size of each one so that I get no OOM errors? For reference, the last lines of the error: ``` File "/home/carlo/code/projects/vllm-experiments/.venv/lib/python3.11/site-packages/xformers/ops/fmha/flash.py", line 120, in _flash_fwd out = query.new_empty(query.shape[0], query.shape[1], value.shape[2]) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 128.00 MiB. GPU 1 has a total capacty of 7.79 GiB of which 20.69 MiB is free. Including non-PyTorch memory, this process has 7.75 GiB memory in use. Of the allocated memory 7.45 GiB is allocated by PyTorch, and 8.61 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting max_split_size_mb to avoid fr...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: GPUs, and I get an OOM error on the smaller one. Is there a way I can specify the size of each one so that I get no OOM errors? For reference, the last lines of the error: ``` File "/home/carlo/code/projects/vllm-experi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: t the load uniformly between the two GPUs, and I get an OOM error on the smaller one. Is there a way I can specify the size of each one so that I get no OOM errors? For reference, the last lines of the error: ``` File "...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: GPUs with different VRAM sizes, OOM I have a 24Gb 3090 and a 8Gb 3070 GPU that I would like to combine for inference purposes. I tried running ```python -u -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 800...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: on -u -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8000 --model teknium/OpenHermes-2-Mistral-7B --tensor-parallel-size 2``` but it seems to me that the code is trying to split the load uniformly between t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: TORCH_CUDA_ALLOC_CONF ``` performance distributed_parallel;model_support;scheduler_memory cuda;operator oom env_dependency;shape I have a 24Gb 3090 and a 8Gb 3070 GPU that I would like to combine for inference purposes.

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
