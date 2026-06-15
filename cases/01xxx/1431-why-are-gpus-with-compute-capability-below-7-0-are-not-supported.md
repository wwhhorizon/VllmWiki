# vllm-project/vllm#1431: Why are GPUs with compute capability below 7.0 are not supported.

| 字段 | 值 |
| --- | --- |
| Issue | [#1431](https://github.com/vllm-project/vllm/issues/1431) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Why are GPUs with compute capability below 7.0 are not supported.

### Issue 正文摘录

My GPU Has a Compute capability of 6.1 Is there any chance of getting it to work with a Tesla P4?

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Why are GPUs with compute capability below 7.0 are not supported. My GPU Has a Compute capability of 6.1 Is there any chance of getting it to work with a Tesla P4?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
