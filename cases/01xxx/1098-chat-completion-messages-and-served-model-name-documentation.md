# vllm-project/vllm#1098: Chat completion messages and `--served-model-name` documentation

| 字段 | 值 |
| --- | --- |
| Issue | [#1098](https://github.com/vllm-project/vllm/issues/1098) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Chat completion messages and `--served-model-name` documentation

### Issue 正文摘录

Should we include in the documentation that the `--served-model-name` must match the conversation templates registered by `fastchat` in order to resolve the chat completion messages when using `messages` input format?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Chat completion messages and `--served-model-name` documentation Should we include in the documentation that the `--served-model-name` must match the conversation templates registered by `fastchat` in order to resolve t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
