# vllm-project/vllm#7655: [Misc]: OOM (CUDA Out Of Memory) when running LLMs in WSL using vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#7655](https://github.com/vllm-project/vllm/issues/7655) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;kernel;quantization |
| 症状 | oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Misc]: OOM (CUDA Out Of Memory) when running LLMs in WSL using vLLM

### Issue 正文摘录

**Environment:** * WSL version: 2.2.4.0 * Kernel version: 5.15.153.1-2 * WSLg version: 1.0.61 * MSRDC version: 1.2.5326 * Direct3D version: 1.611.1-81528511 * DXCore version: 10.0.26091.1-240325-1447.ge-release * Windows version: 10.0.22631.2861 * RTX3050, 4GBs VRAM, 40 GBs RAM * CUDA Version: 12.1 **vLLM version:** 0.5.4 **Problem:** When running Qwen2 in WSL using vLLM, I encounter a CUDA Out Of Memory (OOM) error. **Commands and errors:** * `cmd1:` ```shell vllm serve Qwen/Qwen2-7B-Instruct-GPTQ-Int4 --gpu-memory-utilization 0.99 --quantization "gptq" ``` ```shell File "/home/ubuntu/.local/lib/python3.10/site-packages/torch/utils/_device.py", line 79, in __torch_function__ return func(*args, **kwargs) torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 34.00 MiB. GPU 0 has a total capacity of 4.00 GiB of which 0 bytes is free. Including non-PyTorch memory, this process has 17179869184.00 GiB memory in use. Of the allocated memory 3.35 GiB is allocated by PyTorch, and 125.23 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation. See documentation for Me...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: t Of Memory) when running LLMs in WSL using vLLM **Environment:** * WSL version: 2.2.4.0 * Kernel version: 5.15.153.1-2 * WSLg version: 1.0.61 * MSRDC version: 1.2.5326 * Direct3D version: 1.611.1-81528511 * DXCore vers...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: nd errors:** * `cmd1:` ```shell vllm serve Qwen/Qwen2-7B-Instruct-GPTQ-Int4 --gpu-memory-utilization 0.99 --quantization "gptq" ``` ```shell File "/home/ubuntu/.local/lib/python3.10/site-packages/torch/utils/_device.py"...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Misc]: OOM (CUDA Out Of Memory) when running LLMs in WSL using vLLM **Environment:** * WSL version: 2.2.4.0 * Kernel version: 5.15.153.1-2 * WSLg version: 1.0.61 * MSRDC version: 1.2.5326 * Direct3D version: 1.611.1-81...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Misc]: OOM (CUDA Out Of Memory) when running LLMs in WSL using vLLM **Environment:** * WSL version: 2.2.4.0 * Kernel version: 5.15.153.1-2 * WSLg version: 1.0.61 * MSRDC version: 1.2.5326 * Direct3D version: 1.611.1-81...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: CUDA Version: 12.1 **vLLM version:** 0.5.4 **Problem:** When running Qwen2 in WSL using vLLM, I encounter a CUDA Out Of Memory (OOM) error. **Commands and errors:** * `cmd1:` ```shell vllm serve Qwen/Qwen2-7B-Instruct-G...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
