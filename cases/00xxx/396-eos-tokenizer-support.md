# vllm-project/vllm#396: EOS tokenizer support. 

| 字段 | 值 |
| --- | --- |
| Issue | [#396](https://github.com/vllm-project/vllm/issues/396) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> EOS tokenizer support. 

### Issue 正文摘录

This is really cool stuff. I was using vicuna api server so far, it worked great for me. I would like to explore this now, and I was wondering how you were taking care of the eos token problem, as different models have different tokens as eos. if you are, can you point me to the list of models you are supporting?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ondering how you were taking care of the eos token problem, as different models have different tokens as eos. if you are, can you point me to the list of models you are supporting?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
