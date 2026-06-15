# vllm-project/vllm#370: Can I transform an existing Model into LLM?

| 字段 | 值 |
| --- | --- |
| Issue | [#370](https://github.com/vllm-project/vllm/issues/370) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Can I transform an existing Model into LLM?

### Issue 正文摘录

I have an modified model from `LlamaForCausalLM`, when I use `LLM(name=path/to/state_dict)` I came into problems like loading state_dict. I wonder If we can transform an exisiting model into LLM, which will help a lot such cases!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Can I transform an existing Model into LLM? I have an modified model from `LlamaForCausalLM`, when I use `LLM(name=path/to/state_dict)` I came into problems like loading state_dict. I wonder If we can transform an exisi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
