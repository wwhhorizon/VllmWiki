# vllm-project/vllm#18152: [Performance]: Worse prefilling with unified triton attention

| 字段 | 值 |
| --- | --- |
| Issue | [#18152](https://github.com/vllm-project/vllm/issues/18152) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache |
| 子分类 | latency_reg |
| Operator 关键词 | attention;kernel;triton |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Performance]: Worse prefilling with unified triton attention

### Issue 正文摘录

### Proposal to improve performance ### Report of performance regression When I used the kernel updated with #16828, I witnessed a huge prefilling (TTFT) performance drop on A100@40GB. For an 8k token sequence, the old chunked prefilling kernel costs ~600ms while the new one uses 1500ms. Is there any configuration I should set for this kernel? Thanks!

## 现有链接修复摘要

#16828 [Kernel] Unified Triton kernel that doesn't distinguish between prefill + decode

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]: Worse prefilling with unified triton attention performance ### Proposal to improve performance ### Report of performance regression When I used the kernel updated with #16828, I witnessed a huge prefillin...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Performance]: Worse prefilling with unified triton attention performance ### Proposal to improve performance ### Report of performance regression When I used the kernel updated with #16828, I witnessed a huge prefillin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed with #16828, I witnessed a huge prefilling (TTFT) performance drop on A100@40GB. For an 8k token sequence, the old chunked prefilling kernel costs ~600ms while the new one uses 1500ms. Is there any configuration I sh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: filling kernel costs ~600ms while the new one uses 1500ms. Is there any configuration I should set for this kernel? Thanks! performance attention_kv_cache attention;kernel;triton #16828 [Kernel] Unified Triton kernel th...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: rformance ### Proposal to improve performance ### Report of performance regression When I used the kernel updated with #16828, I witnessed a huge prefilling (TTFT) performance drop on A100@40GB. For an 8k token sequence...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#16828](https://github.com/vllm-project/vllm/pull/16828) | mentioned | 0.45 | [Kernel] Unified Triton kernel that doesn't distinguish between prefill + decode | report of performance regression when i used the kernel updated with #16828, i witnessed a huge prefilling (ttft) performance drop on a100@40gb. for an 8k token sequence, the old… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
