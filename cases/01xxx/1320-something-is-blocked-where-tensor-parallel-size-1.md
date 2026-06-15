# vllm-project/vllm#1320: Something is blocked where tensor_parallel_size > 1

| 字段 | 值 |
| --- | --- |
| Issue | [#1320](https://github.com/vllm-project/vllm/issues/1320) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Something is blocked where tensor_parallel_size > 1

### Issue 正文摘录

Something is blocked where tensor_parallel_size > 1 The displayed content is： Started a local Ray instance. and nothing else it is work where tensor_parallel_size == 1 I set NCCL_IGNORE_DISABLED_P2P=1. it is error before I set NCCL_IGNORE_DISABLED_P2P=1.

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: Something is blocked where tensor_parallel_size > 1 Something is blocked where tensor_parallel_size > 1 The displayed content is： Started a local Ray instance. and nothing else it is work where tensor_parallel_size == 1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
