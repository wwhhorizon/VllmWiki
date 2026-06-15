# vllm-project/vllm#434: Finetuned Flan-T5

| 字段 | 值 |
| --- | --- |
| Issue | [#434](https://github.com/vllm-project/vllm/issues/434) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Finetuned Flan-T5

### Issue 正文摘录

Hi vllm team, I know you guys are extremely busy with many action items. vLLM is now becoming a must when you run LLM. I plan to use a finetuned FLAN-T5 model. My question is: - Do you support FLAN-T5 like models? - How do we use finetuned models as opposed to off the shelf HF models? Thanks a lot for your kind answers.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Finetuned Flan-T5 new-model Hi vllm team, I know you guys are extremely busy with many action items. vLLM is now becoming a must when you run LLM. I plan to use a finetuned FLAN-T5 model. My question is: - Do you suppor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
