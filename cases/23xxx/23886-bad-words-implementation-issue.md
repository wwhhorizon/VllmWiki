# vllm-project/vllm#23886: bad words implementation issue

| 字段 | 值 |
| --- | --- |
| Issue | [#23886](https://github.com/vllm-project/vllm/issues/23886) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> bad words implementation issue

### Issue 正文摘录

The current implementation considers leading spaces, but there's a condition that adding a leading space doesn't change the number of token ids, which to me seems unnecessary and could lead to undesirable results. For example, when using deepseek-r1-distilled-32b model, adding "describe" to bad_words does not prevent " describe" being generated, as " described" has 1 token but "described" has 2 tokens. I suggest removing the conditions checking that the number of word ids are the same and also that first token should be different. https://github.com/vllm-project/vllm/blob/d3d2aad5a2a06b0ea22ae09cb0c6fb6912fa64d8/vllm/logits_process.py#L42

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: o undesirable results. For example, when using deepseek-r1-distilled-32b model, adding "describe" to bad_words does not prevent " describe" being generated, as " described" has 1 token but "described" has 2 tokens. I su...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: bad words implementation issue stale The current implementation considers leading spaces, but there's a condition that adding a leading space doesn't change the number of token ids, which to me seems unnecessary and cou...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
