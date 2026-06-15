# vllm-project/vllm#2613: How to get the logits of the first generated text?

| 字段 | 值 |
| --- | --- |
| Issue | [#2613](https://github.com/vllm-project/vllm/issues/2613) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to get the logits of the first generated text?

### Issue 正文摘录

I simply aim to obtain the logit value corresponding to the first token generated in each request , rather than acquiring sampled tokens. For example, for A/B/C/D tokens, how to retrieve the logit values of these specific tokens？ In huggingface model, the code be like: `logits = self.model(input_ids=input_ids,).logits[:,-1].flatten()`

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tokens, how to retrieve the logit values of these specific tokens？ In huggingface model, the code be like: `logits = self.model(input_ids=input_ids,).logits[:,-1].flatten()`
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ample, for A/B/C/D tokens, how to retrieve the logit values of these specific tokens？ In huggingface model, the code be like: `logits = self.model(input_ids=input_ids,).logits[:,-1].flatten()`
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: btain the logit value corresponding to the first token generated in each request , rather than acquiring sampled tokens. For example, for A/B/C/D tokens, how to retrieve the logit values of these specific tokens？ In hug...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
