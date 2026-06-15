# vllm-project/vllm#28220: [Bug]: Find the root cause of SHARED_EXPERTS_STREAM fail

| 字段 | 值 |
| --- | --- |
| Issue | [#28220](https://github.com/vllm-project/vllm/issues/28220) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Find the root cause of SHARED_EXPERTS_STREAM fail

### Issue 正文摘录

In #28180 there was implemented workaround for `apply_repetition_penalties` fail. Need to investigate the root cause. All preliminary details in #28180

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: Find the root cause of SHARED_EXPERTS_STREAM fail bug In #28180 there was implemented workaround for `apply_repetition_penalties` fail. Need to investigate the root cause. All preliminary details in #28180

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
