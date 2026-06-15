# vllm-project/vllm#30778: [RFC] DBO fallout tracking metrics

| 字段 | 值 |
| --- | --- |
| Issue | [#30778](https://github.com/vllm-project/vllm/issues/30778) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC] DBO fallout tracking metrics

### Issue 正文摘录

### 🚀 The feature, motivation and pitch (co-authored with @sallyom and Claude) ## Motivation Production WideEP deployments exhibit unpredictable throughput variance (10-50% degradation) with no clear diagnostic signal. Dual Batch Overlap (DBO) is a technique that splits batches into two micro-batches (ubatches) to overlap computation and communication, significantly improving throughput in Data-Parallel deployments. However, DBO is fragile and falls out silently when conditions aren't met—such as when the second ubatch would be empty (common at 256-token boundaries) or when DP ranks disagree on ubatching decisions. Currently, there is no instrumentation to confirm whether DBO is engaged or why it disengages. Operators cannot distinguish between DBO working as expected, falling out due to batch size alignment issues, or failing due to coordination problems across DP ranks. This makes root-causing throughput degradation nearly impossible. See [this slack thread in llm-d #sig-deepseek](https://llm-d.slack.com/archives/C08TFSU2PFY/p1765216364703649?thread_ts=1765213004.840599&cid=C08TFSU2PFY) for context ## Proposed Change Add metrics to track DBO engagement and fallout reasons. | Met...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [RFC] DBO fallout tracking metrics feature request;stale ### 🚀 The feature, motivation and pitch (co-authored with @sallyom and Claude) ## Motivation Production WideEP deployments exhibit unpredictable throughput varian...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ude) ## Motivation Production WideEP deployments exhibit unpredictable throughput variance (10-50% degradation) with no clear diagnostic signal. Dual Batch Overlap (DBO) is a technique that splits batches into two micro...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: common at 256-token boundaries) or when DP ranks disagree on ubatching decisions. Currently, there is no instrumentation to confirm whether DBO is engaged or why it disengages. Operators cannot distinguish between DBO w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: See [this slack thread in llm-d #sig-deepseek](https://llm-d.slack.com/archives/C08TFSU2PFY/p1765216364703649?thread_ts=1765213004.840599&cid=C08TFSU2PFY) for context ## Proposed Change Add metrics to track DBO engageme...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: shold - `other` - Other reasons **Label schema**: All metrics include `{model_name, engine}` labels. `dbo_active` adds `{phase}` (prefill/decode). `dbo_fallout_total` adds `{reason}`. `ubatch_token_count` adds `{ubatch_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
