# vllm-project/vllm#1478: OpenAI API model_check should be optional or removed

| 字段 | 值 |
| --- | --- |
| Issue | [#1478](https://github.com/vllm-project/vllm/issues/1478) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> OpenAI API model_check should be optional or removed

### Issue 正文摘录

There doesn't seem to be a good reason to check the model name since a single vLLM only serves one model. Instead I would prefer to either have the `check_model` function [1] removed or be able to turn the check off through configuration. [1] https://github.com/vllm-project/vllm/blob/v0.2.1/vllm/entrypoints/openai/api_server.py#L62

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: OpenAI API model_check should be optional or removed There doesn't seem to be a good reason to check the model name since a single vLLM only serves one model. Instead I would prefer to either have the `check_model` func...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
