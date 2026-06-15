# vllm-project/vllm#424: A matching Triton is not available, some optimizations will not be enabled.

| 字段 | 值 |
| --- | --- |
| Issue | [#424](https://github.com/vllm-project/vllm/issues/424) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> A matching Triton is not available, some optimizations will not be enabled.

### Issue 正文摘录

Why is this paragraph printed in the output log? How to fix it? ![image](https://github.com/vllm-project/vllm/assets/16505966/3e07d7d6-0fb5-4cd4-8c53-6cde368eb1c6)

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: A matching Triton is not available, some optimizations will not be enabled. Why is this paragraph printed in the output log? How to fix it? ![image](https://github.com/vllm-project/vllm/assets/16505966/3e07d7d6-0fb5-4cd...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
