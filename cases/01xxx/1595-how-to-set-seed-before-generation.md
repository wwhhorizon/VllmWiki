# vllm-project/vllm#1595: How to set seed before generation?

| 字段 | 值 |
| --- | --- |
| Issue | [#1595](https://github.com/vllm-project/vllm/issues/1595) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to set seed before generation?

### Issue 正文摘录

I know, you can set any seed during model loading, but how specific seed can be set before each generation (without reloading model every time) or even better for every N prompt you feed to generator? Thank you in advance!

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: re request I know, you can set any seed during model loading, but how specific seed can be set before each generation (without reloading model every time) or even better for every N prompt you feed to generator? Thank y...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: on? good first issue;feature request I know, you can set any seed during model loading, but how specific seed can be set before each generation (without reloading model every time) or even better for every N prompt you...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: How to set seed before generation? good first issue;feature request I know, you can set any seed during model loading, but how specific seed can be set before each generation (without reloading model every time) or even...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
