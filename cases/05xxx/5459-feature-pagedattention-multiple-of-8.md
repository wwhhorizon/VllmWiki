# vllm-project/vllm#5459: [Feature]: PagedAttention multiple of 8

| 字段 | 值 |
| --- | --- |
| Issue | [#5459](https://github.com/vllm-project/vllm/issues/5459) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: PagedAttention multiple of 8

### Issue 正文摘录

This is more of a informative question than a direct feature request. From my understanding, currently PagedAttention only allows head dimensions being multiples of 16, is this correct? What efforts would be required to also allow multiples of 8? Thanks

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: PagedAttention multiple of 8 feature request;stale This is more of a informative question than a direct feature request. From my understanding, currently PagedAttention only allows head dimensions being multi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: : PagedAttention multiple of 8 feature request;stale This is more of a informative question than a direct feature request. From my understanding, currently PagedAttention only allows head dimensions being multiples of 1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
