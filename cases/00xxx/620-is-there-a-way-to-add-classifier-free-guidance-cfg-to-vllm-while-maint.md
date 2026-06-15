# vllm-project/vllm#620: Is there a way to add classifier free guidance (CFG) to vllm while maintaining super fast inference?

| 字段 | 值 |
| --- | --- |
| Issue | [#620](https://github.com/vllm-project/vllm/issues/620) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Is there a way to add classifier free guidance (CFG) to vllm while maintaining super fast inference?

### Issue 正文摘录

I've seen there's recently been a [PR](https://github.com/huggingface/transformers/pull/24654) that incorporates classifier-free guidance to HF model.generate function and it's super useful for generation. Is there a way to incorporate this in to the vllm sampling mechanism?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: request;stale I've seen there's recently been a [PR](https://github.com/huggingface/transformers/pull/24654) that incorporates classifier-free guidance to HF model.generate function and it's super useful for generation....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e guidance (CFG) to vllm while maintaining super fast inference? feature request;stale I've seen there's recently been a [PR](https://github.com/huggingface/transformers/pull/24654) that incorporates classifier-free gui...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ation. Is there a way to incorporate this in to the vllm sampling mechanism?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
