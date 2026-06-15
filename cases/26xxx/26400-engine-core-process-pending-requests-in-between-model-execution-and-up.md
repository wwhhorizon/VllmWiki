# vllm-project/vllm#26400: [Engine Core] Process pending requests in-between model execution and update_from_outputs

| 字段 | 值 |
| --- | --- |
| Issue | [#26400](https://github.com/vllm-project/vllm/issues/26400) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Engine Core] Process pending requests in-between model execution and update_from_outputs

### Issue 正文摘录

I think the reason we've encountered an abort after a request is finished (see #25067) is likely that in the core model loop, abort (and other new) requests aren't processed between the model execution / forward pass and the call to `scheduler.update_from_outputs()` which handles the request completion including notifying the scheduler. We should probably look at changing it to process pending requests in-between so that in this case, the request status will have already been updated to ABORTED when it's passed to `request_finished()` (and then the nixl connector will return `async_save=False` so the blocks will be freed immediately. _Originally posted by @njhill in https://github.com/vllm-project/vllm/pull/25067#discussion_r2412406761_

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: quest_finished()` (and then the nixl connector will return `async_save=False` so the blocks will be freed immediately. _Originally posted by @njhill in https://github.com/vllm-project/vllm/pull/25067#discussion_r2412406...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Engine Core] Process pending requests in-between model execution and update_from_outputs I think the reason we've encountered an abort after a request is finished (see #25067) is likely that in the core model loop, abo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Engine Core] Process pending requests in-between model execution and update_from_outputs I think the reason we've encountered an abort after a request is finished (see #25067) is likely that in the core model loop, abo...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
