# vllm-project/vllm#1833: How can multi GPU be utilized sequentially in VLLM?

| 字段 | 值 |
| --- | --- |
| Issue | [#1833](https://github.com/vllm-project/vllm/issues/1833) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How can multi GPU be utilized sequentially in VLLM?

### Issue 正文摘录

I have two A40 GPU with a total of 96GB of memory. The startup model requires 70GB, which should be bootable.But VLLM is used to start, the memory of both GPU reaches 48GB at the same time, an error message stating insufficient memory is reported.Please help,Thank you!

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: both GPU reaches 48GB at the same time, an error message stating insufficient memory is reported.Please help,Thank you!
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: in VLLM? I have two A40 GPU with a total of 96GB of memory. The startup model requires 70GB, which should be bootable.But VLLM is used to start, the memory of both GPU reaches 48GB at the same time, an error message sta...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
