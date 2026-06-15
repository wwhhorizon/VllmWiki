# vllm-project/vllm#2143: Use LRU cache for CUDA Graphs

| 字段 | 值 |
| --- | --- |
| Issue | [#2143](https://github.com/vllm-project/vllm/issues/2143) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Use LRU cache for CUDA Graphs

### Issue 正文摘录

another way to save memory is to use LRUcache for this map, and capture it on demand. _Originally posted by @scv119 in https://github.com/vllm-project/vllm/pull/1926#discussion_r1427594126_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Use LRU cache for CUDA Graphs feature request;stale another way to save memory is to use LRUcache for this map, and capture it on demand. _Originally posted by @scv119 in https://github.com/vllm-project/vllm/pull/1926#d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Use LRU cache for CUDA Graphs feature request;stale another way to save memory is to use LRUcache for this map, and capture it on demand. _Originally posted by @scv119 in https://github.com/vllm-project/vllm/pull/1926#d...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
