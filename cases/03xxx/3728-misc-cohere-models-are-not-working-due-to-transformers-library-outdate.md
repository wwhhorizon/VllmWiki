# vllm-project/vllm#3728: [Misc]: Cohere models are not working due to transformers library outdated?

| 字段 | 值 |
| --- | --- |
| Issue | [#3728](https://github.com/vllm-project/vllm/issues/3728) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Cohere models are not working due to transformers library outdated?

### Issue 正文摘录

### Anything you want to discuss about vllm. Got error --- ValueError: The checkpoint you are trying to load has model type `cohere` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: . This could be because of an issue with the checkpoint, or because your version of Transformers is out of date.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: to load has model type `cohere` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Misc]: Cohere models are not working due to transformers library outdated? stale ### Anything you want to discuss about vllm. Got error --- ValueError: The checkpoint you are trying to load has model type `cohere` but...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: sc]: Cohere models are not working due to transformers library outdated? stale ### Anything you want to discuss about vllm. Got error --- ValueError: The checkpoint you are trying to load has model type `cohere` but Tra...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
