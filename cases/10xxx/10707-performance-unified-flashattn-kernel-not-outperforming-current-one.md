# vllm-project/vllm#10707: [Performance]: Unified flashattn kernel not outperforming current one

| 字段 | 值 |
| --- | --- |
| Issue | [#10707](https://github.com/vllm-project/vllm/issues/10707) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Unified flashattn kernel not outperforming current one

### Issue 正文摘录

### Proposal to improve performance While working on https://github.com/vllm-project/vllm/pull/9291/, I experimented with unifying prefills and decodes processing in a single forward call (through the `flash_attn_varlen_func` API), while currently we separate the two by "splitting" the flattened 1d tokens tensor (size n_prefills+n_decodes). The unification is meaningful when chunked prefill is enabled, as it will allow mixed prefill-decodes batches to be scheduled. Following the change, @sroy745 found no speedup in his benchmarks with the new version using a single kernel call, which is quite baffling. I believe we should give the fused version another try in a separate PR, investigating the causes of the unexpected slowdown, as in theory this should be a low-hanging fruit in terms of performance optimization. The plan would be to rebase the changes introduced prior to this commit https://github.com/vllm-project/vllm/pull/9291/commits/2a9d8f1e48646eb79431c72b608bb2f44532666c#diff-c310ada35beeefacf4f019051ceaffeb471117d5d5b8be51610d80c7632c6bdcL657-L678 and benchmark performance once again to set the baseline, then take it from there. No need to focus on spec decoding from the star...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: nce]: Unified flashattn kernel not outperforming current one performance;stale ### Proposal to improve performance While working on https://github.com/vllm-project/vllm/pull/9291/, I experimented with unifying prefills...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: o be scheduled. Following the change, @sroy745 found no speedup in his benchmarks with the new version using a single kernel call, which is quite baffling. I believe we should give the fused version another try in a sep...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ing the change, @sroy745 found no speedup in his benchmarks with the new version using a single kernel call, which is quite baffling. I believe we should give the fused version another try in a separate PR, investigatin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
