# vllm-project/vllm#299: Support Multiple Models

| 字段 | 值 |
| --- | --- |
| Issue | [#299](https://github.com/vllm-project/vllm/issues/299) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 104; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support Multiple Models

### Issue 正文摘录

- Allow user to specify multiple models to download when loading server - Allow user to switch between models - Allow user to load multiple models on the cluster (nice to have)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Support Multiple Models feature request - Allow user to specify multiple models to download when loading server - Allow user to switch between models - Allow user to load multiple models on the cluster (nice to have)
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Support Multiple Models feature request - Allow user to specify multiple models to download when loading server - Allow user to switch between models - Allow user to load multiple models on the cluster (nice to have)
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Support Multiple Models feature request - Allow user to specify multiple models to download when loading server - Allow user to switch between models - Allow user to load multiple models on the cluster (nice to have)

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
