# vllm-project/vllm#6685: [Usage]: logprobs variable in SamplingParams from ChatCompletionRequest class

| 字段 | 值 |
| --- | --- |
| Issue | [#6685](https://github.com/vllm-project/vllm/issues/6685) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: logprobs variable in SamplingParams from ChatCompletionRequest class

### Issue 正文摘录

I have noticed that the logprobs variable could be set to a boolean (top_logprobs) in this line https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/openai/protocol.py#L254. Is not supposed to be an integer which displays the number of log probabilities to return per output token?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: logprobs variable in SamplingParams from ChatCompletionRequest class usage I have noticed that the logprobs variable could be set to a boolean (top_logprobs) in this line https://github.com/vllm-project/vllm/bl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
