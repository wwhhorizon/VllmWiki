# vllm-project/vllm#485: Flash Attention V2

| 字段 | 值 |
| --- | --- |
| Issue | [#485](https://github.com/vllm-project/vllm/issues/485) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Flash Attention V2

### Issue 正文摘录

https://github.com/Dao-AILab/flash-attention Flash attention v2 was released claiming 2x speedups. Making an issue to remind myself to have a look at it. And also if anyone else wants to try implement it.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: Flash Attention V2 feature request https://github.com/Dao-AILab/flash-attention Flash attention v2 was released claiming 2x speedups. Making an issue to remind myself to have a look at it. And also if anyone else wants
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: king an issue to remind myself to have a look at it. And also if anyone else wants to try implement it.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Flash Attention V2 feature request https://github.com/Dao-AILab/flash-attention Flash attention v2 was released claiming 2x speedups. Making an issue to remind myself to have a look at it. And also if anyone else wants...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
