# vllm-project/vllm#6307: [Feature]: Is there any plan to support Cross-Layer Attention (CLA) ?

| 字段 | 值 |
| --- | --- |
| Issue | [#6307](https://github.com/vllm-project/vllm/issues/6307) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Is there any plan to support Cross-Layer Attention (CLA) ?

### Issue 正文摘录

The Cross-Layer Attention (CLA) proposed by MIT recently can significantly reduce runtime memory usage. Does vLLM have any plans to support it? Thanks! Cross-Layer Attention paper: https://arxiv.org/abs/2405.12981

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ure]: Is there any plan to support Cross-Layer Attention (CLA) ? feature request;stale The Cross-Layer Attention (CLA) proposed by MIT recently can significantly reduce runtime memory usage. Does vLLM have any plans to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
