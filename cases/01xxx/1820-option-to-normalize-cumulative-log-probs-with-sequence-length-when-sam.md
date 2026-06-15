# vllm-project/vllm#1820: Option to normalize cumulative log probs with sequence length when sampling with best_of?

| 字段 | 值 |
| --- | --- |
| Issue | [#1820](https://github.com/vllm-project/vllm/issues/1820) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Option to normalize cumulative log probs with sequence length when sampling with best_of?

### Issue 正文摘录

Right now, the completions returned with `best_of` are selected based on highest cumulative logprob, but that biases responses towards shorter sequences. It would be great if vLLM supported normalization methods for selecting these best_of responses, such as: - Dividing by # of completion tokens - Dividing by byte length - Normalizing by unconditional likelihoods See https://blog.eleuther.ai/multiple-choice-normalization/, https://arxiv.org/pdf/2001.09977.pdf

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ative log probs with sequence length when sampling with best_of? feature request;stale Right now, the completions returned with `best_of` are selected based on highest cumulative logprob, but that biases responses towar...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
