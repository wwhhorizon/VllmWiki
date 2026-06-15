# vllm-project/vllm#4303: [Feature]: batched parallel decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#4303](https://github.com/vllm-project/vllm/issues/4303) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: batched parallel decoding

### Issue 正文摘录

### 🚀 The feature, motivation and pitch [Parallel/Jacobi decoding](https://arxiv.org/abs/2305.10427) improves inference efficiency by breaking the sequential nature of conventional auto-regressive decoding. Recent works [[1](https://arxiv.org/pdf/2307.15337.pdf), [2](https://arxiv.org/pdf/2402.02057.pdf), [3](https://arxiv.org/abs/2403.00835)] have found opportunities in this direction and efficiency improvements parallel decoding could bring. Our team (@nanjiangwill, @Viol2000, @zhisbug) is interested in implementing this feature and supporting batched parallel decoding for efficient serving on vllm. This could be a complementary feature to the speculative decoding features the vllm team is supporting: 1. in high request-rate regime, using draft models/tree-based verification could introduce additional overhead that hurts serving latency. 2. in such cases, batched parallel decoding could be adopted to bring consistently speedup without the need for draft models. 3. Alternative to speculative decoding depending users' needs. Future implementations could also potentially bring the two together. 4. Expedite research efforts in this general direction. ### Alternatives _No response_ #...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: batched parallel decoding feature request;stale ### 🚀 The feature, motivation and pitch [Parallel/Jacobi decoding](https://arxiv.org/abs/2305.10427) improves inference efficiency by breaking the sequential na...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: acobi decoding](https://arxiv.org/abs/2305.10427) improves inference efficiency by breaking the sequential nature of conventional auto-regressive decoding. Recent works [[1](https://arxiv.org/pdf/2307.15337.pdf), [2](ht...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ntations could also potentially bring the two together. 4. Expedite research efforts in this general direction. ### Alternatives _No response_ ### Additional context _No response_
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: the vllm team is supporting: 1. in high request-rate regime, using draft models/tree-based verification could introduce additional overhead that hurts serving latency. 2. in such cases, batched parallel decoding could b...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ased verification could introduce additional overhead that hurts serving latency. 2. in such cases, batched parallel decoding could be adopted to bring consistently speedup without the need for draft models. 3. Alternat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
