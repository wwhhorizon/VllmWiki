# vllm-project/vllm#5796: Serving inference requests based on caching

| 字段 | 值 |
| --- | --- |
| Issue | [#5796](https://github.com/vllm-project/vllm/issues/5796) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Serving inference requests based on caching

### Issue 正文摘录

### Anything you want to discuss about vllm. I am trying to see if we want to enable/disable cache that can be used of inference requests.For example one user asks a question on something how can that be used for figure similar kind of requests based on cache ..do I need to enable —prefix-caching flag. second question where does vllm saves the cache ..is it in physical disk ? Can someone please answer above questions

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Serving inference requests based on caching stale ### Anything you want to discuss about vllm. I am trying to see if we want to enable/disable cache that can be used of inference requests.For example one user asks a que...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
