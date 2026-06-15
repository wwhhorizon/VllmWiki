# vllm-project/vllm#1436: Bug: Aquila2 (e.g. 34B 16k) needs linear rope_scaling added

| 字段 | 值 |
| --- | --- |
| Issue | [#1436](https://github.com/vllm-project/vllm/issues/1436) |
| 状态 | closed |
| 标签 |  |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Bug: Aquila2 (e.g. 34B 16k) needs linear rope_scaling added

### Issue 正文摘录

https://github.com/FlagAI-Open/Aquila2#base-model-performance

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ds linear rope_scaling added https://github.com/FlagAI-Open/Aquila2#base-model-performance

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
