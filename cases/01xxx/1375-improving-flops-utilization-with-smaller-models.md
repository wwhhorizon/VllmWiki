# vllm-project/vllm#1375: Improving FLOPS utilization with smaller models

| 字段 | 值 |
| --- | --- |
| Issue | [#1375](https://github.com/vllm-project/vllm/issues/1375) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Improving FLOPS utilization with smaller models

### Issue 正文摘录

Hello! We've been using VLLM to run some batch inference tasks and are huge fans of the experience so far. However, some of the models we're using are on the smaller end ( 7B) we're able to consistently hit 90%+ utilization. Do you have any tips for optimizing utilization for these smaller models? I've tried tweaking the max cached sequences/tokens and the block size, but those don't seem to make much of a difference.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Improving FLOPS utilization with smaller models Hello! We've been using VLLM to run some batch inference tasks and are huge fans of the experience so far. However, some of the models we're using are on the smaller end (...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ller models? I've tried tweaking the max cached sequences/tokens and the block size, but those don't seem to make much of a difference.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Improving FLOPS utilization with smaller models Hello! We've been using VLLM to run some batch inference tasks and are huge fans of the experience so far. However, some of the models we're using are on the smaller end (...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
