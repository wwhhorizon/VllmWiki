# vllm-project/vllm#1857: How to retrieve the LLM hidden state?

| 字段 | 值 |
| --- | --- |
| Issue | [#1857](https://github.com/vllm-project/vllm/issues/1857) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to retrieve the LLM hidden state?

### Issue 正文摘录

Hi, I'm using ChatGLM3 as an encoder to encode sentences, and vllm is deployed to speed up the process. ChatGLM3 contains a transformer encoder to generate hidden state (with shape L x D where L is #.tokens and D is the dimensionality), and a linear 'decoder' to generate next token. I want to use the hidden state of the final input token to represent the sentence. I have carefully read the source code of vllm, but I can't find a clear solution for my requirement, unless drastically revise the code. Is there any api or configuration that can meet my requirement? Or do you have any suggestion for implementing my requirement? Best regards.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: my requirement, unless drastically revise the code. Is there any api or configuration that can meet my requirement? Or do you have any suggestion for implementing my requirement? Best regards.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: pe L x D where L is #.tokens and D is the dimensionality), and a linear 'decoder' to generate next token. I want to use the hidden state of the final input token to represent the sentence. I have carefully read the sour...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
