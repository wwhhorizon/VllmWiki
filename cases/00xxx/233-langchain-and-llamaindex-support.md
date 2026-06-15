# vllm-project/vllm#233: LangChain and LlamaIndex support

| 字段 | 值 |
| --- | --- |
| Issue | [#233](https://github.com/vllm-project/vllm/issues/233) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> LangChain and LlamaIndex support

### Issue 正文摘录

Excellent job, it made my LLM blazing fast. I tried it on T4 (16GB vRAM) and it seems to lower inference time from 36 secs to just 9 secs. I then tried to use it along with LangChain and LlamaIndex but I got the following error: ValidationError: 1 validation error for LLMChain llm value is not a valid dict (type=type_error.dict) Can you please provide any guidance?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: LangChain and LlamaIndex support Excellent job, it made my LLM blazing fast. I tried it on T4 (16GB vRAM) and it seems to lower inference time from 36 secs to just 9 secs. I then tried to use it along with LangChain and...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
