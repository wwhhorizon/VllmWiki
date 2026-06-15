# vllm-project/vllm#33625: [Feature]: improve sleep mode to not break torch.cuda memory counters

| 字段 | 值 |
| --- | --- |
| Issue | [#33625](https://github.com/vllm-project/vllm/issues/33625) |
| 状态 | open |
| 标签 | feature request;unstale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: improve sleep mode to not break torch.cuda memory counters

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently when vllm is used in conjunction with other gpu programs, e.g. RL (verl+vllm) and the sleep mode is used, we end up with very bogus `torch.cuda` memory counters. The `torch.cuda` memory reporting is all broken in that situation, since vllm somehow frees up all the kv-cache and weights when put to "sleep" (because we need the same gpu's mem to be free to do a training step) but torch isn't the wiser the freeing happened - the same gpus are shared between inference and training - each loading and releasing all memory it uses - so only one of them used at a time. So when vllm did its unloading `torch.cuda` still reports `memory_allocated()` from vllm's run, even though it has been actually freed, which makes it quite difficult to debug memory-related problems. The other weird related thing is that `torch.cuda.memory_reserved` and `torch.cuda.max_memory_reserved` report: 198.68 GB and 199 GB on H200, so there are only 140GB! How could it possibly report more than the physical size of the memory? (and in this particular use case vllm's memory usage was about 60GB so the diff with 200-60=140GB checks out) So the workaround proposed here...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: l other counters are still wrong, and getting just Used memory is insufficient when dealing with memory issues. Is it possible to fix the sleep mode to correctly tell `torch.cuda` that tensors used by vllm have been fre...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ure]: improve sleep mode to not break torch.cuda memory counters feature request;unstale ### 🚀 The feature, motivation and pitch Currently when vllm is used in conjunction with other gpu programs, e.g. RL (verl+vllm) an...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Feature]: improve sleep mode to not break torch.cuda memory counters feature request;unstale ### 🚀 The feature, motivation and pitch Currently when vllm is used in conjunction with other gpu programs, e.g. RL (verl+vll...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ing is all broken in that situation, since vllm somehow frees up all the kv-cache and weights when put to "sleep" (because we need the same gpu's mem to be free to do a training step) but torch isn't the wiser the freei...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
