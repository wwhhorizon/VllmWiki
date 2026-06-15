# vllm-project/vllm#824: How do init mul-instances on mul-gpus for concurrency request on server?

| 字段 | 值 |
| --- | --- |
| Issue | [#824](https://github.com/vllm-project/vllm/issues/824) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How do init mul-instances on mul-gpus for concurrency request on server?

### Issue 正文摘录

eg CUDA_VISIBLE_DEVICES=gpus XXXXX (init model server) ?

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: do init mul-instances on mul-gpus for concurrency request on server? eg CUDA_VISIBLE_DEVICES=gpus XXXXX (init model server) ?
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: concurrency request on server? eg CUDA_VISIBLE_DEVICES=gpus XXXXX (init model server) ?
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: How do init mul-instances on mul-gpus for concurrency request on server? eg CUDA_VISIBLE_DEVICES=gpus XXXXX (init model server) ?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
