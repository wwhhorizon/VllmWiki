# vllm-project/vllm#13255: [Usage]: Multiple card issues

| 字段 | 值 |
| --- | --- |
| Issue | [#13255](https://github.com/vllm-project/vllm/issues/13255) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;triton |
| 症状 | oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Multiple card issues

### Issue 正文摘录

### Your current environment My machine has two Tesla P100 16G computing cards. Nvidia driver, cuda, and cudnn have all been installed. My vllm startup code is as follows: ![Image](https://github.com/user-attachments/assets/5770133d-6089-41d7-ab73-11c987c67f0e) ``` [rank0]: torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised: [rank0]: RuntimeError: Found Tesla P100-PCIE-16GB which is too old to be supported by the triton GPU compiler, which is used as the backend. Triton only supports devices of CUDA Capability >= 7.0, but your device is of CUDA capability 6.0 ``` If I change this: ![Image](https://github.com/user-attachments/assets/2cf0b0d4-7c0c-44bc-a03c-3ed65c5e4ad2) `ERROR 02-14 11:08:20 multiproc_worker_utils.py:242] torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 270.00 MiB. GPU 1 has a total capacity of 15.89 GiB of which 110.50 MiB is free. Including non-PyTorch memory, this process has 15.77 GiB memory in use. Of the allocated memory 15.44 GiB is allocated by PyTorch, and 20.58 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentat...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: a P100 16G computing cards. Nvidia driver, cuda, and cudnn have all been installed. My vllm startup code is as follows: ![Image](https://github.com/user-attachments/assets/5770133d-6089-41d7-ab73-11c987c67f0e) ``` [rank...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: nment My machine has two Tesla P100 16G computing cards. Nvidia driver, cuda, and cudnn have all been installed. My vllm startup code is as follows: ![Image](https://github.com/user-attachments/assets/5770133d-6089-41d7...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ets/5770133d-6089-41d7-ab73-11c987c67f0e) ``` [rank0]: torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised: [rank0]: RuntimeError: Found Tesla P100-PCIE-16GB which is too old to be supported by the triton...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: asked questions. performance model_support;scheduler_memory cuda;triton oom env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for re...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
