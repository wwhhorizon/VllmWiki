# vllm-project/vllm#1495: How to implement a disk cache? Or better ideas? 

| 字段 | 值 |
| --- | --- |
| Issue | [#1495](https://github.com/vllm-project/vllm/issues/1495) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to implement a disk cache? Or better ideas? 

### Issue 正文摘录

I have a lot of large and similar prompt prefixes across requests. As an optimization, I am toying with the idea to cache kv on disk and load the cache from disk depending on the prefix. Any design inputs on how to go about doing this? Open to any suggestions, maybe you have better ideas where to optimize.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: better ideas? I have a lot of large and similar prompt prefixes across requests. As an optimization, I am toying with the idea to cache kv on disk and load the cache from disk depending on the prefix. Any design inputs...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
