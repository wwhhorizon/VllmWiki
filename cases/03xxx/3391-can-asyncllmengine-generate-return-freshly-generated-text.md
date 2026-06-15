# vllm-project/vllm#3391: Can AsyncLLMEngine.generate return freshly generated text?

| 字段 | 值 |
| --- | --- |
| Issue | [#3391](https://github.com/vllm-project/vllm/issues/3391) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Can AsyncLLMEngine.generate return freshly generated text?

### Issue 正文摘录

How can I make the AsyncLLMEngine.generate method call output only new generated text without including incremental text each time it's invoked? The current return is formatted as: I I like I like apple And I want it to be return like this: I like apple

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: including incremental text each time it's invoked? The current return is formatted as: I I like I like apple And I want it to be return like this: I like apple

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
