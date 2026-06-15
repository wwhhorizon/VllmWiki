# vllm-project/vllm#6993: [Feature]: Is it possible to control whether to use speculative decoding when making a request?

| 字段 | 值 |
| --- | --- |
| Issue | [#6993](https://github.com/vllm-project/vllm/issues/6993) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Is it possible to control whether to use speculative decoding when making a request?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch It looks like I need to decide whether to enable speculative decoding when loading the model. However, it seems that it is not appropriate to use speculative decoding in all input scenarios, especially when speculating by matching n-grams in the prompt. Is it possible to control whether to use speculative decoding when making a request? ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Is it possible to control whether to use speculative decoding when making a request? feature request;stale ### 🚀 The feature, motivation and pitch It looks like I need to decide whether to enable speculative...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: stale ### 🚀 The feature, motivation and pitch It looks like I need to decide whether to enable speculative decoding when loading the model. However, it seems that it is not appropriate to use speculative decoding in all...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: I need to decide whether to enable speculative decoding when loading the model. However, it seems that it is not appropriate to use speculative decoding in all input scenarios, especially when speculating by matching n-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
