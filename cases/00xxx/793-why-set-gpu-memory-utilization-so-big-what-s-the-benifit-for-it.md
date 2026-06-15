# vllm-project/vllm#793: Why set gpu_memory_utilization so big? What‘s the benifit for it?

| 字段 | 值 |
| --- | --- |
| Issue | [#793](https://github.com/vllm-project/vllm/issues/793) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Why set gpu_memory_utilization so big? What‘s the benifit for it?

### Issue 正文摘录

if gpu_memory_utilization set to 0.9，nowhatever you load a model， it will occupy very huge memory

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: nifit for it? if gpu_memory_utilization set to 0.9，nowhatever you load a model， it will occupy very huge memory

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
