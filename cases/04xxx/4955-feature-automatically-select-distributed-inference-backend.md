# vllm-project/vllm#4955: [Feature]: automatically select distributed inference backend

| 字段 | 值 |
| --- | --- |
| Issue | [#4955](https://github.com/vllm-project/vllm/issues/4955) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: automatically select distributed inference backend

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ray is kind of an overkill for single gpu case, but is currently the only choice for multi-node inference. we can add an `auto` backend, that checks the world size and the number of gpus available in the node, if this fits within this node, we can use multiprocessing, otherwise we can use ray. this will help performance a lot. @njhill do you have any bandwidth for this? ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: automatically select distributed inference backend feature request ### 🚀 The feature, motivation and pitch ray is kind of an overkill for single gpu case, but is currently the only choice for multi-node infer...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: automatically select distributed inference backend feature request ### 🚀 The feature, motivation and pitch ray is kind of an overkill for single gpu case, but is currently the only choice for multi-node infer...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
