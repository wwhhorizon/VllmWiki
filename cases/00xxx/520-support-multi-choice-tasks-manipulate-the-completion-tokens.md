# vllm-project/vllm#520: Support Multi-choice Tasks (Manipulate the completion tokens)

| 字段 | 值 |
| --- | --- |
| Issue | [#520](https://github.com/vllm-project/vllm/issues/520) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support Multi-choice Tasks (Manipulate the completion tokens)

### Issue 正文摘录

Hi, I have noticed my previous failures now. [#Previous Failures](https://github.com/vllm-project/vllm/discussions/504) That is, for some multi-choice tasks, e.g., multi-choice sentence completions, in most common-sense reasoning tasks, we do need to manipulate the completion tokens, instead of current Samplingparams which generate token-by-token on LLMs themselves. `That is, autoregressive LMs will adjust their logprobs each step with different inputs. For MC tasks, we do need to input the correct prefix to LMs.` How can we enable so?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
