# vllm-project/vllm#918: What is the supported input length for qwen？

| 字段 | 值 |
| --- | --- |
| Issue | [#918](https://github.com/vllm-project/vllm/issues/918) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> What is the supported input length for qwen？

### Issue 正文摘录

What is the supported input length for qwen? The maximum length supported by qwen model is 8K, but the vllm support is not so large, is there any plan to support this?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: What is the supported input length for qwen？ What is the supported input length for qwen? The maximum length supported by qwen model is 8K, but the vllm support is not so large, is there any plan to support this?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
