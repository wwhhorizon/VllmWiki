# vllm-project/vllm#2141: Adding LogitProcessors to VLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#2141](https://github.com/vllm-project/vllm/issues/2141) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Adding LogitProcessors to VLLM

### Issue 正文摘录

Hi! I've been using vLLM for implementing watermarking algorithms, and I've needed to have support for a LogitProcessor similar to what HuggingFace has in their library. I've added a LogitProcessor class that is called in the sampler forward pass. By default it only handles the temperature scaling, but the sampler can be modified to call more complex LogitProcessor, such as those required to implement watermarking algorithms. It would be great to have this functionality in the main vLLM project. This could also be very useful for implementing more complex sampling strategies in general. Here is a diff of what I've added to to project, the changes are pretty minor: https://github.com/vllm-project/vllm/compare/main...julien-piet:vllm:main Happy to help merge this if you think this is a feature you would like to have! Thanks, Julien

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ms, and I've needed to have support for a LogitProcessor similar to what HuggingFace has in their library. I've added a LogitProcessor class that is called in the sampler forward pass. By default it only handles the tem...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
