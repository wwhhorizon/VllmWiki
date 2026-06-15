# vllm-project/vllm#7461: [Feature]: early-stop in mooncake

| 字段 | 值 |
| --- | --- |
| Issue | [#7461](https://github.com/vllm-project/vllm/issues/7461) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: early-stop in mooncake

### Issue 正文摘录

### 🚀 The feature, motivation and pitch has vllm realized early-stopping? that is, abort the request when the computation/memory resource is not available. I noticed there is timeout-abort func in vllm v0.5.4, but does vllm can abort request actively without needing user to quit the request? the feature is realized in . ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: early-stop in mooncake feature request ### 🚀 The feature, motivation and pitch has vllm realized early-stopping? that is, abort the request when the computation/memory resource is not available. I noticed the...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
