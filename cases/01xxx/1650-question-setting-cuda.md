# vllm-project/vllm#1650: Question! setting cuda !

| 字段 | 值 |
| --- | --- |
| Issue | [#1650](https://github.com/vllm-project/vllm/issues/1650) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Question! setting cuda !

### Issue 正文摘录

Hi! I am glad to you open this project!! I am novice about LLM. And I just try the example/offline_inference.py But I got below message: ```shell torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 2.93 GiB (GPU 0; 79.15 GiB total capacity; 52.98 GiB already allocated; 1.03 GiB free; 53.00 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation. See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF ``` My Server 4 A100, but when I run no option, it is set cuda device 0, right? because other code is runnign cuda device 0. So how can I change device?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: DA out of memory. Tried to allocate 2.93 GiB (GPU 0; 79.15 GiB total capacity; 52.98 GiB already allocated; 1.03 GiB free; 53.00 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting ma...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Question! setting cuda ! Hi! I am glad to you open this project!! I am novice about LLM. And I just try the example/offline_inference.py But I got below message: ```shell torch.cuda.OutOfMemoryError: CUDA out of memory....
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: how can I change device? performance frontend_api;scheduler_memory cuda oom env_dependency Hi!
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ign cuda device 0. So how can I change device? performance frontend_api;scheduler_memory cuda oom env_dependency Hi!

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
