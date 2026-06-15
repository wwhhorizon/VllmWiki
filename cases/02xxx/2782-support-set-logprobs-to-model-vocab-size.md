# vllm-project/vllm#2782: support set logprobs to model vocab size

| 字段 | 值 |
| --- | --- |
| Issue | [#2782](https://github.com/vllm-project/vllm/issues/2782) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> support set logprobs to model vocab size

### Issue 正文摘录

set logprobs to model vocab size is hard, some model can use len(tokenizer), some use tokenizer.vocab_size, some will raise an error. so need to support set logprobs to model vocab size

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: support set logprobs to model vocab size stale set logprobs to model vocab size is hard, some model can use len(tokenizer), some use tokenizer.vocab_size, some will raise an error. so need to support set logprobs to mod...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: support set logprobs to model vocab size stale set logprobs to model vocab size is hard, some model can use len(tokenizer), some use tokenizer.vocab_size, some will raise an error. so need to support set logprobs to mod...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
