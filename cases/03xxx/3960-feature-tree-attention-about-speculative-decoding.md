# vllm-project/vllm#3960: [Feature]: Tree attention about Speculative Decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#3960](https://github.com/vllm-project/vllm/issues/3960) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Tree attention about Speculative Decoding

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I want to implement tree attention for vllm mentioned in [RoadMap](https://github.com/vllm-project/vllm/issues/3861). But I don’t know whether I should implement it based on paged-attention kernel implemented in vllm or FlashInfer due to I found we plan to replace this kernel in this [PR.](https://github.com/vllm-project/vllm/pull/2772) ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Tree attention about Speculative Decoding feature request;stale ### 🚀 The feature, motivation and pitch I want to implement tree attention for vllm mentioned in [RoadMap](https://github.com/vllm-project/vllm/...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ould implement it based on paged-attention kernel implemented in vllm or FlashInfer due to I found we plan to replace this kernel in this [PR.](https://github.com/vllm-project/vllm/pull/2772) ### Alternatives _No respon...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
