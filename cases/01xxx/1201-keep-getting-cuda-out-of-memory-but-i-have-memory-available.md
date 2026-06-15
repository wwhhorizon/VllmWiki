# vllm-project/vllm#1201: Keep getting CUDA out of memory but I have memory available!

| 字段 | 值 |
| --- | --- |
| Issue | [#1201](https://github.com/vllm-project/vllm/issues/1201) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Keep getting CUDA out of memory but I have memory available!

### Issue 正文摘录

torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 1.74 GiB (GPU 0; 47.54 GiB total capacity; 31.64 GiB already allocated; 1.03 GiB free; 31.66 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation. See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF +-----------------------------------------------------------------------------+ | NVIDIA-SMI 525.125.06 Driver Version: 525.125.06 CUDA Version: 12.0 | |-------------------------------+----------------------+----------------------+ | GPU Name Persistence-M| Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap| Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |===============================+======================+======================| | 0 NVIDIA RTX A6000 On | 00000000:4F:00.0 Off | Off | | 30% 25C P8 22W / 300W | 13936MiB / 49140MiB | 0% Default | | | | N/A | +-------------------------------+----------------------+----------------------+ +-----------------------------------------------------------------------------+ | Processes: | | GPU GI CI PID Type Process name GPU Memory | | ID ID Usage | |==============...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: DA out of memory. Tried to allocate 1.74 GiB (GPU 0; 47.54 GiB total capacity; 31.64 GiB already allocated; 1.03 GiB free; 31.66 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting ma...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Keep getting CUDA out of memory but I have memory available! torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 1.74 GiB (GPU 0; 47.54 GiB total capacity; 31.64 GiB already allocated; 1.03 GiB free; 31.6...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: | | GPU GI CI PID Type Process name GPU Memory | | ID ID Usage | |=============================================================================| +----------------------------------------------
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: --------------------------------------------------+ performance ci_build;scheduler_memory cuda oom env_dependency torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 1.74 GiB (GPU 0; 47.54 GiB total capac...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
