# vllm-project/vllm#1610: Can S-Lora be integrated into vLLM?

| 字段 | 值 |
| --- | --- |
| Issue | [#1610](https://github.com/vllm-project/vllm/issues/1610) |
| 状态 | closed |
| 标签 |  |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Can S-Lora be integrated into vLLM?

### Issue 正文摘录

https://github.com/S-LoRA/S-LoRA They call it 'unified paging' and don't require the model to be merged before doing inference. This would be really useful for serving Mixture of Expert models for example or a service that requires multiple different fine-tuned lora adapters based on the same base model. And needless to say there has been a lot of request for lora deployments

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: b.com/S-LoRA/S-LoRA They call it 'unified paging' and don't require the model to be merged before doing inference. This would be really useful for serving Mixture of Expert models for example or a service that requires...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: fore doing inference. This would be really useful for serving Mixture of Expert models for example or a service that requires multiple different fine-tuned lora adapters based on the same base model. And needless to say...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: sed on the same base model. And needless to say there has been a lot of request for lora deployments

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
