# vllm-project/vllm#3742: request for Pytorch 2.2

| 字段 | 值 |
| --- | --- |
| Issue | [#3742](https://github.com/vllm-project/vllm/issues/3742) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> request for Pytorch 2.2

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Pytorch 2.2 ### Alternatives Pytorch 2.1 ### Additional context Pytorch 2.2 is the fasted twice as fast with flash attention :D motivated by discussion here: https://github.com/vllm-project/vllm/issues/2747

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: .1 ### Additional context Pytorch 2.2 is the fasted twice as fast with flash attention :D motivated by discussion here: https://github.com/vllm-project/vllm/issues/2747
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: request for Pytorch 2.2 feature request ### 🚀 The feature, motivation and pitch Pytorch 2.2 ### Alternatives Pytorch 2.1 ### Additional context Pytorch 2.2 is the fasted twice as fast with flash attention :D motiva

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
