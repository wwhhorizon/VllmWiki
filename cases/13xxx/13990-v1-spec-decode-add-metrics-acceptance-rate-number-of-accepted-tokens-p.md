# vllm-project/vllm#13990: [V1] [Spec Decode] Add metrics (acceptance rate, number of accepted tokens per step) for V1 rejection sampler

| 字段 | 值 |
| --- | --- |
| Issue | [#13990](https://github.com/vllm-project/vllm/issues/13990) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [V1] [Spec Decode] Add metrics (acceptance rate, number of accepted tokens per step) for V1 rejection sampler

### Issue 正文摘录

We need to give a more clear definition of accepted tokens, generated tokens, bonus tokens, and acceptance rate for V1 compared to V0. We need to track those metrics in the rejection sampler.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [V1] [Spec Decode] Add metrics (acceptance rate, number of accepted tokens per step) for V1 rejection sampler We need to give a more clear definition of accepted tokens, generated tokens, bonus tokens, and acceptance ra...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
