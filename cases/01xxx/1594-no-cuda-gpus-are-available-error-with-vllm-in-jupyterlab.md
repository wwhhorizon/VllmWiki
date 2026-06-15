# vllm-project/vllm#1594: No CUDA GPUs are available Error with vLLM in JupyterLab 

| 字段 | 值 |
| --- | --- |
| Issue | [#1594](https://github.com/vllm-project/vllm/issues/1594) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> No CUDA GPUs are available Error with vLLM in JupyterLab 

### Issue 正文摘录

Hello, I have been facing a various errors regarding running the vLLM on GCP with JupyterLab. The set of errors as as follow: - No CUDA GPUs are available - CUDA out of memory. Tried to allocate 150.00 MiB (GPU 0; 14.58 GiB total capacity; 13.94 GiB already allocated; 17.31 MiB free; 13.94 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation. See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF Please, I need help!

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: GPUs are available Error with vLLM in JupyterLab Hello, I have been facing a various errors regarding running the vLLM on GCP with JupyterLab. The set of errors as as follow: - No CUDA GPUs are available - CUDA out of m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: No CUDA GPUs are available Error with vLLM in JupyterLab Hello, I have been facing a various errors regarding running the vLLM on GCP with JupyterLab. The set of errors as as follow: - No CUDA GPUs are available - CUDA
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: _CUDA_ALLOC_CONF Please, I need help! performance scheduler_memory cuda oom Hello,
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Management and PYTORCH_CUDA_ALLOC_CONF Please, I need help! performance scheduler_memory cuda oom Hello,

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
