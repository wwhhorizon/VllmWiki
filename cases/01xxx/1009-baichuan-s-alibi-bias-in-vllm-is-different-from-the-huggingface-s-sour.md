# vllm-project/vllm#1009: baichuan's alibi bias in vllm is different from the huggingface's source code，doesn't it matter？Yes

| 字段 | 值 |
| --- | --- |
| Issue | [#1009](https://github.com/vllm-project/vllm/issues/1009) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> baichuan's alibi bias in vllm is different from the huggingface's source code，doesn't it matter？Yes

### Issue 正文摘录

here is: [-n,-n+1,......,0] * alibi_slopes huggingface's is: [0,1,.....,n] * alibi_slopes During inferring，the former need updates all cached value‘s alibi，but the latter need only updates the last one's. Doesn't it matter？Do the cached prompts' alibi keep being updated now? Need I do the following modifications, if I want to keep the same with baichuan's source code ？ https://github.com/vllm-project/vllm/issues/985#issuecomment-1711061942

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: baichuan's alibi bias in vllm is different from the huggingface's source code，doesn't it matter？Yes here is: [-n,-n+1,......,0] * alibi_slopes huggingface's is: [0,1,.....,n] * alibi_slopes During inferring，the former n...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
