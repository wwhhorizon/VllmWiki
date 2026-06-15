# vllm-project/vllm#1940: How to enable data parallelism with multiple gpus for inference?

| 字段 | 值 |
| --- | --- |
| Issue | [#1940](https://github.com/vllm-project/vllm/issues/1940) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to enable data parallelism with multiple gpus for inference?

### Issue 正文摘录

I know you can achieve tensor parallelism with tensor_parallel_size=2 when using multi-gpus, was wondering if its possible to enable data parallelism as well. I tried making concurrent requests using multi-threading but that came with a host of runtime issues.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: How to enable data parallelism with multiple gpus for inference? I know you can achieve tensor parallelism with tensor_parallel_size=2 when using multi-gpus, was wondering if its possible to enable data parallelism as w...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: s possible to enable data parallelism as well. I tried making concurrent requests using multi-threading but that came with a host of runtime issues.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
