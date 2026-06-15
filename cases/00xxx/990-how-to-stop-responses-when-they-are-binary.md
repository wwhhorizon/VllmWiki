# vllm-project/vllm#990: How to stop responses when they are binary?

| 字段 | 值 |
| --- | --- |
| Issue | [#990](https://github.com/vllm-project/vllm/issues/990) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to stop responses when they are binary?

### Issue 正文摘录

I am trying to work with LLAMA2 HF 13B and set max_tokens = 200, however there are some questions that are only one word or binary answer. But still I always get 200 tokens even if the answer is binary say True or False. How can we control this?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: How to stop responses when they are binary? I am trying to work with LLAMA2 HF 13B and set max_tokens = 200, however there are some questions that are only one word or binary answer. But still I always get 200 tokens ev...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: still I always get 200 tokens even if the answer is binary say True or False. How can we control this?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
