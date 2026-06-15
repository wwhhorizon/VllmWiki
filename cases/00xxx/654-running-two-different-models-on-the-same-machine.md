# vllm-project/vllm#654: Running two different models on the same machine

| 字段 | 值 |
| --- | --- |
| Issue | [#654](https://github.com/vllm-project/vllm/issues/654) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Running two different models on the same machine

### Issue 正文摘录

I want to run two different models on the same machine. Right now, I'm declaring two different `AsyncLLMEngine` objects such that the respective `gpu_memory_utilizations` add up to 1 but I'm getting CUDA OOM errors. What would be the right way to do this? Thanks!

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: hat the respective `gpu_memory_utilizations` add up to 1 but I'm getting CUDA OOM errors. What would be the right way to do this? Thanks! performance frontend_api cuda oom I want to run two different models on the same...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: he respective `gpu_memory_utilizations` add up to 1 but I'm getting CUDA OOM errors. What would be the right way to do this? Thanks! performance frontend_api cuda oom I want to run two different models on the same machi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Running two different models on the same machine feature request I want to run two different models on the same machine. Right now, I'm declaring two different `AsyncLLMEngine` objects such that the respective `gpu_memo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Running two different models on the same machine feature request I want to run two different models on the same machine. Right now, I'm declaring two different `AsyncLLMEngine` objects such that the respective `gpu_memo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
