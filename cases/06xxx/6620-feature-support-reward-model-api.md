# vllm-project/vllm#6620: [Feature]: support reward model API

| 字段 | 值 |
| --- | --- |
| Issue | [#6620](https://github.com/vllm-project/vllm/issues/6620) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: support reward model API

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Does VLLM support rapid deployment of RM services? Or convenient custom APIs? It seems that currently there are only chat/completion/embedding APIs. As a newcomer to inference acceleration, any help would be beneficial. We want to use vllm to accelerate RM API for the remote RM feature of OpenRLHF. https://github.com/OpenRLHF/OpenRLHF/pull/361/ ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: support reward model API feature request;stale ### 🚀 The feature, motivation and pitch Does VLLM support rapid deployment of RM services? Or convenient custom APIs? It seems that currently there are only chat...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: support reward model API feature request;stale ### 🚀 The feature, motivation and pitch Does VLLM support rapid deployment of RM services? Or convenient custom APIs? It seems that currently there are only chat...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: g APIs. As a newcomer to inference acceleration, any help would be beneficial. We want to use vllm to accelerate RM API for the remote RM feature of OpenRLHF. https://github.com/OpenRLHF/OpenRLHF/pull/361/ ### Alternati...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
