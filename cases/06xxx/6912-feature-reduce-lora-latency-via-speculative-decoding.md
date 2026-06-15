# vllm-project/vllm#6912: [Feature]: Reduce LoRA latency via speculative decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#6912](https://github.com/vllm-project/vllm/issues/6912) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Reduce LoRA latency via speculative decoding

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The speculative decoding framework allows the target model to have LoRAs, however the work to set up batch expansion has not yet been done. We can implement batch expansion for LoRA and allow speculative decoding for LoRA. The work required is basically to implement batch expansion but pass through the LoRA arguments. See "Let’s talk about code" in the following notes: https://docs.google.com/document/d/1z4Tgb1FcDr3YXvFPelyn-T-DEnLqqrlrxRi3TvIyAmg/edit I expect this to work well for larger models (e.g. 70B) but more difficult with smaller models due to latency constraints and vLLM overheads. Perhaps with a speculator like ngram / eagle / mlpspeculator it can work for 7b models as well. Note this work does not include applying LoRA to the speculator; that can be a future work. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Reduce LoRA latency via speculative decoding feature request;stale ### 🚀 The feature, motivation and pitch The speculative decoding framework allows the target model to have LoRAs, however the work to set up...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: t this to work well for larger models (e.g. 70B) but more difficult with smaller models due to latency constraints and vLLM overheads. Perhaps with a speculator like ngram / eagle / mlpspeculator it can work for 7b mode...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tivation and pitch The speculative decoding framework allows the target model to have LoRAs, however the work to set up batch expansion has not yet been done. We can implement batch expansion for LoRA and allow speculat...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Feature]: Reduce LoRA latency via speculative decoding feature request;stale ### 🚀 The feature, motivation and pitch The speculative decoding framework allows the target model to have LoRAs, however the work to set up...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
