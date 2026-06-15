# vllm-project/vllm#1211: Support per-request seed

| 字段 | 值 |
| --- | --- |
| Issue | [#1211](https://github.com/vllm-project/vllm/issues/1211) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support per-request seed

### Issue 正文摘录

Although part of that problem is that there's no per-request seed, something we also really need. _Originally posted by @TheBloke in https://github.com/vllm-project/vllm/issues/866#issuecomment-1703815608_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Support per-request seed feature request Although part of that problem is that there's no per-request seed, something we also really need. _Originally posted by @TheBloke in https://github.com/vllm-project/vllm/issues/8...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
