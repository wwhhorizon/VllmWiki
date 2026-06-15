# vllm-project/vllm#352: How to specify which GPU the model inference on?

| 字段 | 值 |
| --- | --- |
| Issue | [#352](https://github.com/vllm-project/vllm/issues/352) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> How to specify which GPU the model inference on?

### Issue 正文摘录

Hello, I have 4 GPUs. And when I set `tensor_parallel_size` as 2, when running the service, it would takes CUDA:0 and CUDA:1. My question is, if I want start two workers(i.e. two process that deploy two same models), how to specify my second process takes on CUDA:2 and CUDA:3? Cuz now if I just start service without any config, it will OOM.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: How to specify which GPU the model inference on? feature request Hello, I have 4 GPUs. And when I set `tensor_parallel_size` as 2, when running the service, it would takes CUDA:0 and CUDA:1. My question is, if I want st...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: How to specify which GPU the model inference on? feature request Hello, I have 4 GPUs. And when I set `tensor_parallel_size` as 2, when running the service, it would takes CUDA:0 and CUDA:1. My question is, if I want st...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: et `tensor_parallel_size` as 2, when running the service, it would takes CUDA:0 and CUDA:1. My question is, if I want start two workers(i.e. two process that deploy two same models), how to specify my second process tak...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: and CUDA:3? Cuz now if I just start service without any config, it will OOM. performance frontend_api;model_support cuda oom Hello, I have 4 GPUs. And when I set `tensor_parallel_size` as 2, when running the service, it...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: How to specify which GPU the model inference on? feature request Hello, I have 4 GPUs. And when I set `tensor_parallel_size` as 2, when running the service, it would takes CUDA:0 and CUDA:1. My question is, if I want st...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
