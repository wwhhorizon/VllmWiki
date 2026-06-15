# vllm-project/vllm#1635: Prompt caching

| 字段 | 值 |
| --- | --- |
| Issue | [#1635](https://github.com/vllm-project/vllm/issues/1635) |
| 状态 | closed |
| 标签 |  |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Prompt caching

### Issue 正文摘录

I saw other folks proposed the feature of caching overlapping prompts for reuse. For example, when the system prompt includes few-shot examples (long), encoding it every request is not efficient. This newly released paper maybe useful: https://huggingface.co/papers/2311.04934.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: includes few-shot examples (long), encoding it every request is not efficient. This newly released paper maybe useful: https://huggingface.co/papers/2311.04934.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: quest is not efficient. This newly released paper maybe useful: https://huggingface.co/papers/2311.04934.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: n the system prompt includes few-shot examples (long), encoding it every request is not efficient. This newly released paper maybe useful: https://huggingface.co/papers/2311.04934.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
