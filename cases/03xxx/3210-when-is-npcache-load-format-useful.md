# vllm-project/vllm#3210: When is npcache load format useful?

| 字段 | 值 |
| --- | --- |
| Issue | [#3210](https://github.com/vllm-project/vllm/issues/3210) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> When is npcache load format useful?

### Issue 正文摘录

It has not provided a speedup to load times when compared to safetensors in my experiments, ends up being much slower than safetensors. Is there an intended usecase for it?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: When is npcache load format useful? It has not provided a speedup to load times when compared to safetensors in my experiments, ends up being much slower than safetensors. Is there an intended usecase for it?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
