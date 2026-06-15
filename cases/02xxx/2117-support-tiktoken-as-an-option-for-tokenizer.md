# vllm-project/vllm#2117: Support tiktoken as an option for tokenizer

| 字段 | 值 |
| --- | --- |
| Issue | [#2117](https://github.com/vllm-project/vllm/issues/2117) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support tiktoken as an option for tokenizer

### Issue 正文摘录

I have a pretrained model that used [https://github.com/openai/tiktoken](url) as the tokenizer. However, when using the set_tokenizer function, i find that this only support tokenizer from HuggingFace, is there a way to support tiktoken in my case?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ken as an option for tokenizer feature request;stale I have a pretrained model that used [https://github.com/openai/tiktoken](url) as the tokenizer. However, when using the set_tokenizer function, i find that this only...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Support tiktoken as an option for tokenizer feature request;stale I have a pretrained model that used [https://github.com/openai/tiktoken](url) as the tokenizer. However, when using the set_tokenizer function, i find th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
