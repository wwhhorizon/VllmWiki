# vllm-project/vllm#2364: Compute perplexity/logits for the prompt

| 字段 | 值 |
| --- | --- |
| Issue | [#2364](https://github.com/vllm-project/vllm/issues/2364) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Compute perplexity/logits for the prompt

### Issue 正文摘录

I'd like to use Phi-2 to compute perplexity of the prompts over an entire dataset. Is there an API for this? In the short term, I'm happy to fork https://github.com/vllm-project/vllm/blob/d0215a58e78572d91dadafe9d832a2db89b09a13/vllm/model_executor/models/phi_1_5.py if you provide pointer on how to do that. Also happy to later contribute back an API that works for all causal models.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: com/vllm-project/vllm/blob/d0215a58e78572d91dadafe9d832a2db89b09a13/vllm/model_executor/models/phi_1_5.py if you provide pointer on how to do that. Also happy to later contribute back an API that works for all causal mo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Compute perplexity/logits for the prompt stale I'd like to use Phi-2 to compute perplexity of the prompts over an entire dataset. Is there an API for this? In the short term, I'm happy to fork https://github.com/vllm-pr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
