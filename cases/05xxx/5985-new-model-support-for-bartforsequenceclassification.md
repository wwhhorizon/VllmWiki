# vllm-project/vllm#5985: [New Model]: support for BartForSequenceClassification

| 字段 | 值 |
| --- | --- |
| Issue | [#5985](https://github.com/vllm-project/vllm/issues/5985) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: support for BartForSequenceClassification

### Issue 正文摘录

### The model to consider. Hi! Is there any plan on supporting https://huggingface.co/facebook/bart-large-mnli on vllm? When I try to run it it says "BartForSequenceClassification" is not supported now, do you know any alternatives or if I'm doing something wrong? Thank you ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting the model you want? _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: support for BartForSequenceClassification new-model;stale ### The model to consider. Hi! Is there any plan on supporting https://huggingface.co/facebook/bart-large-mnli on vllm? When I try to run it it says...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: support for BartForSequenceClassification new-model;stale ### The model to consider. Hi! Is there any plan on supporting https://huggingface.co/facebook/bart-large-mnli on vllm? When I try to run it it says...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
