# vllm-project/vllm#23230: [Bug]: CUDA out of memory when runing nvidia/NVIDIA-Nemotron-Nano-9B-v2 with vllm 0.10.1 on GPU L40S

| 字段 | 值 |
| --- | --- |
| Issue | [#23230](https://github.com/vllm-project/vllm/issues/23230) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;triton |
| 症状 | crash;oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA out of memory when runing nvidia/NVIDIA-Nemotron-Nano-9B-v2 with vllm 0.10.1 on GPU L40S

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug My command: ``` vllm serve nvidia/NVIDIA-Nemotron-Nano-9B-v2 \ --trust-remote-code \ --mamba_ssm_cache_dtype float32 ``` I use L40S and vllm==0.10.1 to deploy nvidia/NVIDIA-Nemotron-Nano-9B-v2, but OOM occurred. Here are the logs: ``` INFO 08-20 03:09:59 [default_loader.py:262] Loading weights took 2.66 seconds INFO 08-20 03:10:00 [model_runner.py:1112] Model loading took 16.5557 GiB and 2.803817 seconds ERROR 08-20 03:10:01 [engine.py:467] CUDA out of memory. Tried to allocate 33.75 GiB. GPU 0 has a total capacity of 44.40 GiB of which 26.88 GiB is free. Including non-PyTorch memory, this process has 17.52 GiB memory in use. Of the allocated memory 17.03 GiB is allocated by PyTorch, and 6.95 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation. See documentation for Memory Management (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables) ERROR 08-20 03:10:01 [engine.py:467] Traceback (most recent call last): ERROR 08-20 03:10:01 [engine.py:467] File "/home/qingfu/py312/lib/python3.12/site-packag...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: CUDA out of memory when runing nvidia/NVIDIA-Nemotron-Nano-9B-v2 with vllm 0.10.1 on GPU L40S bug ### Your current environment ### 🐛 Describe the bug My command: ``` vllm serve nvidia/NVIDIA-Nemotron-Nano-9B-v2 \
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ] CUDA out of memory. Tried to allocate 33.75 GiB. GPU 0 has a total capacity of 44.40 GiB of which 26.88 GiB is free. Including non-PyTorch memory, this process has 17.52 GiB memory in use. Of the allocated memory 17.0...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: IA-Nemotron-Nano-9B-v2 \ --trust-remote-code \ --mamba_ssm_cache_dtype float32 ``` I use L40S and vllm==0.10.1 to deploy nvidia/NVIDIA-Nemotron-Nano-9B-v2, but OOM occurred. Here are the logs: ``` INFO 08-20 03:09:59 [d...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: lt_loader.py:262] Loading weights took 2.66 seconds INFO 08-20 03:10:00 [model_runner.py:1112] Model loading took 16.5557 GiB and 2.803817 seconds ERROR 08-20 03:10:01 [engine.py:467] CUDA out of memory. Tried to alloca...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ilable_blocks ERROR 08-20 03:10:01 [engine.py:467] self.model_runner.profile_run() ERROR 08-20 03:10:01 [engine.py:467] File "/home/qingfu/py312/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 116, in dec...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
