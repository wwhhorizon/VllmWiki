# vllm-project/vllm#1856: [v0.2.3] Release Tracker

| 字段 | 值 |
| --- | --- |
| Issue | [#1856](https://github.com/vllm-project/vllm/issues/1856) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [v0.2.3] Release Tracker

### Issue 正文摘录

**ETA**: Nov 30th - Dec 2nd. ## Major changes * Refactoring on Worker, InputMetadata, and Attention * Fix TP support for AWQ models * Support Prometheus metrics * Fix Baichuan & Baichuan 2 ## PRs to be merged before the release - [x] Chat Template #1756 - [x] ~#1707~ (We have to solve AWQ perf first, which might be possible in time). - [x] ~#1662~ (use the new one instead) - [x] #1890 - [x] #1852

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: **: Nov 30th - Dec 2nd. ## Major changes * Refactoring on Worker, InputMetadata, and Attention * Fix TP support for AWQ models * Support Prometheus metrics * Fix Baichuan & Baichuan 2 ## PRs to be merged before the rele...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ctoring on Worker, InputMetadata, and Attention * Fix TP support for AWQ models * Support Prometheus metrics * Fix Baichuan & Baichuan 2 ## PRs to be merged before the release - [x] Chat Template #1756 - [x] ~#1707~ (We...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
