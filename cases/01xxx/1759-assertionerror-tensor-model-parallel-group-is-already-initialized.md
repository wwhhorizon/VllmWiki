# vllm-project/vllm#1759: AssertionError: tensor model parallel group is already initialized

| 字段 | 值 |
| --- | --- |
| Issue | [#1759](https://github.com/vllm-project/vllm/issues/1759) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> AssertionError: tensor model parallel group is already initialized

### Issue 正文摘录

I want to do inference on a single-gpu, the assertion error arise.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: AssertionError: tensor model parallel group is already initialized I want to do inference on a single-gpu, the assertion error arise.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
