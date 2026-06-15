# vllm-project/vllm#40457: Add fused_topk to CI. Follow-up to 39391

| 字段 | 值 |
| --- | --- |
| Issue | [#40457](https://github.com/vllm-project/vllm/issues/40457) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Add fused_topk to CI. Follow-up to 39391

### Issue 正文摘录

#39391 was merged because want it to be fixed in v0.20. This comment left unfixed https://github.com/vllm-project/vllm/pull/39391#pullrequestreview-4144377845 : - add to CI - add `fused_topk_bias`

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Add fused_topk to CI. Follow-up to 39391 #39391 was merged because want it to be fixed in v0.20. This comment left unfixed https://github.com/vllm-project/vllm/pull/39391#pullrequestreview-4144377845 : - add to CI - add...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: Add fused_topk to CI. Follow-up to 39391 #39391 was merged because want it to be fixed in v0.20. This comment left unfixed https://github.com/vllm-project/vllm/pull/39391#pullrequestreview-4144377845 : - add to CI - add...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: comment left unfixed https://github.com/vllm-project/vllm/pull/39391#pullrequestreview-4144377845 : - add to CI - add `fused_topk_bias`

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
