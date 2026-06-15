# vllm-project/vllm#31483: [RFC]: a efficient adaptive rejection sampling for accelerating speculative decoding.

| 字段 | 值 |
| --- | --- |
| Issue | [#31483](https://github.com/vllm-project/vllm/issues/31483) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: a efficient adaptive rejection sampling for accelerating speculative decoding.

### Issue 正文摘录

### Motivation. Description: This proposal introduces an enhancement to the rejection sampling mechanism at the core of speculative decoding. The current method relies on a fixed, context-independent random threshold, which leads to a significant "random rejection" problem. In high-uncertainty generation scenarios, plausible candidate tokens proposed by the draft model are frequently rejected merely because their acceptance ratio falls slightly below this fixed threshold due to random chance. This wastes the computational effort spent on verifying subsequent draft tokens and severely limits the acceleration potential of speculative decoding for creative or open-ended tasks. Motivation: We observe a dramatic drop in draft acceptance rates as generation uncertainty increases—from over 80% at temperature=0 to only around 30% at temperature=1. This efficiency loss stems from the fixed threshold's inability to account for the intrinsic uncertainty of the target model's predictions at different generation steps. There is a clear need for an adaptive threshold mechanism that is aware of the model's confidence. Such a mechanism could intelligently relax acceptance criteria in high-uncerta...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: This proposal introduces an enhancement to the rejection sampling mechanism at the core of speculative decoding. The current method relies on a fixed, context-independent random threshold, which leads to a significant "...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: a efficient adaptive rejection sampling for accelerating speculative decoding. RFC ### Motivation. Description: This proposal introduces an enhancement to the rejection sampling mechanism at the core of speculati...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: rios, reducing wasteful rejections and substantially improving inference throughput without significantly compromising output quality. ### Proposed Change. Proposed Solution: https://arxiv.org/abs/2512.13194 propose the...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: negligible accuractony drop (e.g., <=0.84% on GSM8K) in tasks requiring precision. 3、Easy Integration: Requires no modifications to model architectures. It can be seamlessly integrated into existing speculative decoding...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [RFC]: a efficient adaptive rejection sampling for accelerating speculative decoding. RFC ### Motivation. Description: This proposal introduces an enhancement to the rejection sampling mechanism at the core of speculati...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
