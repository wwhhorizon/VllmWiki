# vllm-project/vllm#26567: [Refactor][MLA]: Independently pass q_nope & q_rope

| 字段 | 值 |
| --- | --- |
| Issue | [#26567](https://github.com/vllm-project/vllm/issues/26567) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Refactor][MLA]: Independently pass q_nope & q_rope

### Issue 正文摘录

### 🚀 The feature, motivation and pitch This PR: https://github.com/vllm-project/vllm/pull/25103 shows custom op for MLA Original issue (https://github.com/vllm-project/vllm/issues/24620) wants to > pass q_nope and q_rope independently instead of concatenated. This will require a sizable refactor in order to split the two in every backend, so that both are passed truly independently. This issue tracks progress towards this task, the current pr is this: https://github.com/vllm-project/vllm/pull/28368 cc @ProExpertProg

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Refactor][MLA]: Independently pass q_nope & q_rope feature request;stale ### 🚀 The feature, motivation and pitch This PR: https://github.com/vllm-project/vllm/pull/25103 shows custom op for MLA Original issue (https://...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: This will require a sizable refactor in order to split the two in every backend, so that both are passed truly independently. This issue tracks progress towards this task, the current pr is this: https://github.com/vllm...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: rent pr is this: https://github.com/vllm-project/vllm/pull/28368 cc @ProExpertProg

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
