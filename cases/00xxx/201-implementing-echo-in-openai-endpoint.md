# vllm-project/vllm#201: Implementing Echo in OpenAI endpoint

| 字段 | 值 |
| --- | --- |
| Issue | [#201](https://github.com/vllm-project/vllm/issues/201) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Implementing Echo in OpenAI endpoint

### Issue 正文摘录

Maybe not too urgent, but would be nice to have echo in the OpenAI interface, this can facilitate scoring (e.g., QA dataset)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: gent, but would be nice to have echo in the OpenAI interface, this can facilitate scoring (e.g., QA dataset)
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Implementing Echo in OpenAI endpoint good first issue;feature request Maybe not too urgent, but would be nice to have echo in the OpenAI interface, this can facilitate scoring (e.g., QA dataset)

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
