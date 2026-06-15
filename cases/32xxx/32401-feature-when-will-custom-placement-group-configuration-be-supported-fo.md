# vllm-project/vllm#32401: [Feature]: when will custom placement group configuration be supported for DP

| 字段 | 值 |
| --- | --- |
| Issue | [#32401](https://github.com/vllm-project/vllm/issues/32401) |
| 状态 | open |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: when will custom placement group configuration be supported for DP

### Issue 正文摘录

https://github.com/vllm-project/vllm/blob/1e584823f8f9f7b8504c90dfa7689061537280da/vllm/v1/engine/utils.py#L843 For PP, it can inherit the current context's pg configuration. For DP , when will custom placement group configuration be supported.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: when will custom placement group configuration be supported for DP stale https://github.com/vllm-project/vllm/blob/1e584823f8f9f7b8504c90dfa7689061537280da/vllm/v1/engine/utils.py#L843 For PP, it can inherit...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ure]: when will custom placement group configuration be supported for DP stale https://github.com/vllm-project/vllm/blob/1e584823f8f9f7b8504c90dfa7689061537280da/vllm/v1/engine/utils.py#L843 For PP, it can inherit the c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
