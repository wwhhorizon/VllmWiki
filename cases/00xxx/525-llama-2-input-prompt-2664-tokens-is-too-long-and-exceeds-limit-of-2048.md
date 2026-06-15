# vllm-project/vllm#525: LlaMA 2: Input prompt (2664 tokens) is too long and exceeds limit of 2048/2560

| 字段 | 值 |
| --- | --- |
| Issue | [#525](https://github.com/vllm-project/vllm/issues/525) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> LlaMA 2: Input prompt (2664 tokens) is too long and exceeds limit of 2048/2560

### Issue 正文摘录

As we all know, LlaMA 2 can support a maximum context length of 4096 tokens, but the current code will report an warning then return empty string: ``` CompletionOutput(index=0, text='', token_ids=[], cumulative_logprob=0.0, logprobs=[], finish_reason=length) ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: LlaMA 2: Input prompt (2664 tokens) is too long and exceeds limit of 2048/2560 bug As we all know, LlaMA 2 can support a maximum context length of 4096 tokens, but the current code will report an warning then return empt

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
