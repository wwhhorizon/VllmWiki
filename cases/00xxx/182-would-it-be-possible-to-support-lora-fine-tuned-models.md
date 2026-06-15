# vllm-project/vllm#182: Would it be possible to support LoRA fine-tuned models?

| 字段 | 值 |
| --- | --- |
| Issue | [#182](https://github.com/vllm-project/vllm/issues/182) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 47; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Would it be possible to support LoRA fine-tuned models?

### Issue 正文摘录

How easy or difficult it would be to support LoRA fine-tuned models? Would it need big changes to the vLLM engine or is it something that can be done at the higher level by modifying the model?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Would it be possible to support LoRA fine-tuned models? feature request How easy or difficult it would be to support LoRA fine-tuned models? Would it need big changes to the vLLM engine or is it something that can be do...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Would it be possible to support LoRA fine-tuned models? feature request How easy or difficult it would be to support LoRA fine-tuned models? Would it need big changes to the vLLM engine or is it something that can be do...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
