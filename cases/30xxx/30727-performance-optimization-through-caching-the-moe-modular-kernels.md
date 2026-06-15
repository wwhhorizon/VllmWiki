# vllm-project/vllm#30727: [Performance] Optimization through caching the moe modular kernels

| 字段 | 值 |
| --- | --- |
| Issue | [#30727](https://github.com/vllm-project/vllm/issues/30727) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance] Optimization through caching the moe modular kernels

### Issue 正文摘录

> I'm not a fan of how hardcoded this is and I'd like it to apply to all modular kernels, but it is a great find to see that it actually makes a difference in performance. @bnellnm could you help prioritize finding a generalized solution to this problem? _Originally posted by @mgoin in https://github.com/vllm-project/vllm/pull/30718#pullrequestreview-3580446279_ Let's discuss the further refactor and optimizaton here. CC: @mgoin @bnellnm

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Performance] Optimization through caching the moe modular kernels > I'm not a fan of how hardcoded this is and I'd like it to apply to all modular kernels, but it is a great find to see that it actually makes a differe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: posted by @mgoin in https://github.com/vllm-project/vllm/pull/30718#pullrequestreview-3580446279_ Let's discuss the further refactor and optimizaton here. CC: @mgoin @bnellnm

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
