# vllm-project/vllm#8372: [Bug]: OOM when running llama3.1-8B-Instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#8372](https://github.com/vllm-project/vllm/issues/8372) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OOM when running llama3.1-8B-Instruct

### Issue 正文摘录

### Your current environment Hello, I'm trying to download llama3.1-8B-Instruct to my PC and each time i try, i get the following error: ```bash [rank0]: torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 1002.00 MiB. GPU 0 has a total capacity of 15.59 GiB of which 940.12 MiB is free. Including non-PyTorch memory, this process has 14.30 GiB memory in use. Of the allocated memory 14.01 GiB is allocated by PyTorch, and 15.49 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation. See documentation for Memory Management (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables) ``` The code i'm running to download the model: ```python from vllm import LLM llm = LLM(model="meta-llama/Meta-Llama-3.1-8B-Instruct") ``` I have CUDA 12.6, cuDNN and the latest GPU drivers installed. This is the output of `nvidia-smi` when trying to download the model: ```bash Wed Sep 11 18:17:23 2024 +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 560.35.03 Driver Version: 560.35.03 CUDA Version: 12.6 | |-------...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: CUDA out of memory. Tried to allocate 1002.00 MiB. GPU 0 has a total capacity of 15.59 GiB of which 940.12 MiB is free. Including non-PyTorch memory, this process has 14.30 GiB memory in use. Of the allocated memory 14....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ry, i get the following error: ```bash [rank0]: torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 1002.00 MiB. GPU 0 has a total capacity of 15.59 GiB of which 940.12 MiB is free. Including non-PyTorch memor...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: OOM when running llama3.1-8B-Instruct bug;stale ### Your current environment Hello, I'm trying to download llama3.1-8B-Instruct to my PC and each time i try, i get the following error: ```bash [rank0]: torch.OutO...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: OOM when running llama3.1-8B-Instruct bug;stale ### Your current environment Hello, I'm trying to download llama3.1-8B-Instruct to my PC and each time i try, i get the following error: ```bash [rank0]: torch.OutO...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: OOM when running llama3.1-8B-Instruct bug;stale ### Your current environment Hello, I'm trying to download llama3.1-8B-Instruct to my PC and each time i try, i get the following error: ```bash [rank0]: torch.OutO...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
