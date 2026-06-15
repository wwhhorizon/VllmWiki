# vllm-project/vllm#8404: [Misc]: Memory Order in Custom Allreduce

| 字段 | 值 |
| --- | --- |
| Issue | [#8404](https://github.com/vllm-project/vllm/issues/8404) |
| 状态 | closed |
| 标签 |  |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Memory Order in Custom Allreduce

### Issue 正文摘录

# Memory Order in Custom Allreduce In custom allreduce, i notice that `Signal*` has a `volatile` qualifier. And there are no memory fence in `start_sync` function. I want to know that can `volatile` will make right memory order? The `start_sync` program order is: 1. set start flag to other GPU's Signal 2. read start flag from local GPU's Signal 3. allreduce(pull data from other GPU) In my opinion, without memory fence, the step 3 may be visible before Step 2 or 1.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
