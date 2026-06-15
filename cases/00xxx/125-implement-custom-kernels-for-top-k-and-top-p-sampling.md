# vllm-project/vllm#125: Implement custom kernels for top-k and top-p sampling

| 字段 | 值 |
| --- | --- |
| Issue | [#125](https://github.com/vllm-project/vllm/issues/125) |
| 状态 | closed |
| 标签 | help wanted;performance;stale |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Implement custom kernels for top-k and top-p sampling

### Issue 正文摘录

As mentioned in https://github.com/WoosukKwon/cacheflow/pull/81#issuecomment-1546980281, the current PyTorch-based top-k and top-p implementation is memory-inefficient. This can be improved by introducing custom kernels.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: the current PyTorch-based top-k and top-p implementation is memory-inefficient. This can be improved by introducing custom kernels.
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: Implement custom kernels for top-k and top-p sampling help wanted;performance;stale As mentioned in https://github.com/WoosukKwon/cacheflow/pull/81#issuecomment-1546980281, the current PyTorch-based top-k and top-p impl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ment custom kernels for top-k and top-p sampling help wanted;performance;stale As mentioned in https://github.com/WoosukKwon/cacheflow/pull/81#issuecomment-1546980281, the current PyTorch-based top-k and top-p implement...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
