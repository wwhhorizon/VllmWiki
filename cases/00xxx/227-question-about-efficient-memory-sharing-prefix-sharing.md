# vllm-project/vllm#227: Question about efficient memory sharing (prefix sharing)

| 字段 | 值 |
| --- | --- |
| Issue | [#227](https://github.com/vllm-project/vllm/issues/227) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Question about efficient memory sharing (prefix sharing)

### Issue 正文摘录

I have a question about the feature of efficient memory sharing. Does different sequences that sharing the same system prompt but splicing different user-input texts share the computation and memory for the same system prompt? For example, here are two input sequences: 1. You are a kind robot. How's the weather today. 2. You are a kind robot. Tell me a story. Would this two input sequences share the computation and memory for the same system prompt of " You are a kind robot. "?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Question about efficient memory sharing (prefix sharing) feature request I have a question about the feature of efficient memory sharing. Does different sequences that sharing the same system prompt but splicing differe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Question about efficient memory sharing (prefix sharing) feature request I have a question about the feature of efficient memory sharing. Does different sequences that sharing the same system prompt but splicing differe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
