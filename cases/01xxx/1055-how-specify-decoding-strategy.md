# vllm-project/vllm#1055: How specify decoding strategy?

| 字段 | 值 |
| --- | --- |
| Issue | [#1055](https://github.com/vllm-project/vllm/issues/1055) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How specify decoding strategy?

### Issue 正文摘录

Hi, thanks for the good work. I'm wondering how to specify decoding strategy? For example, in transformers generate function, I can specify logits_processor. However, it seems not supported in vllm as shown in https://github.com/vllm-project/vllm/blob/main/vllm/sampling_params.py. Thanks in advance for your help.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: How specify decoding strategy? Hi, thanks for the good work. I'm wondering how to specify decoding strategy? For example, in transformers generate function, I can specify logits_processor. However, it seems not supporte...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
