# vllm-project/vllm#6348: [Feature]: FlashAttention 3 support

| 字段 | 值 |
| --- | --- |
| Issue | [#6348](https://github.com/vllm-project/vllm/issues/6348) |
| 状态 | closed |
| 标签 | help wanted;feature request |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: FlashAttention 3 support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch As you know, FA3 promises 1.5x~ improvements https://github.com/Dao-AILab/flash-attention/commit/7ef24848cf2f855077cef88fe122775b727dcd74 ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Feature]: FlashAttention 3 support help wanted;feature request ### 🚀 The feature, motivation and pitch As you know, FA3 promises 1.5x~ improvements https://github.com/Dao-AILab/flash-attention/commit/7ef24848cf2f855077...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: FlashAttention 3 support help wanted;feature request ### 🚀 The feature, motivation and pitch As you know, FA3 promises 1.5x~ improvements https://github.com/Dao-AILab/flash-attention/commit/7ef24848cf2f855077...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
