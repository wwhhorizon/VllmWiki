# vllm-project/vllm#3225: Add Support for QLORA/QA-QLORA weights which are not merged

| 字段 | 值 |
| --- | --- |
| Issue | [#3225](https://github.com/vllm-project/vllm/issues/3225) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Add Support for QLORA/QA-QLORA weights which are not merged

### Issue 正文摘录

currently only original LORA is supported as not fused adapter, I hope to be able to add the support for QLORA/QA-LORA support for the adapters, without fusing with the base model.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Add Support for QLORA/QA-QLORA weights which are not merged feature request;stale currently only original LORA is supported as not fused adapter, I hope to be able to add the support for QLORA/QA-LORA support for the ad...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: for QLORA/QA-LORA support for the adapters, without fusing with the base model.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
