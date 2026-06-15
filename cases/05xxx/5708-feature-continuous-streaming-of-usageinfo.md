# vllm-project/vllm#5708: [Feature]: Continuous streaming of `UsageInfo`

| 字段 | 值 |
| --- | --- |
| Issue | [#5708](https://github.com/vllm-project/vllm/issues/5708) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Continuous streaming of `UsageInfo`

### Issue 正文摘录

### 🚀 The feature, motivation and pitch **TLDR:** We would like an option we can enable to continuously stream the `UsageInfo` when using the streaming completions API. This solves a number of "accounting" problems encountered while trying to do accurate performance evaluation. **Motivation:** We are working on performance evaluation for vLLM's more advanced features (chunked prefill, speculative decoding) and have run into a few problems that we feel would be solved by adding a simple new feature. Our benchmarking framework [fmperf](https://github.com/fmperf-project/fmperf) computes ITL by measuring the latency between consequence streaming responses, in addition it computes throughput by inspecting each streaming response and counting the number of tokens in it. Currently vLLM provides no information about how many tokens are contained within each response. In most situation, it is just a single token. However, there are few scenarios where this is not the case: 1. When chunked prefill is enabled and a prompt gets chunked across multiple iterations, the first few responses may contain zero tokens. There is no special indication that this has happened beyond just an empty string...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: accounting" problems encountered while trying to do accurate performance evaluation. **Motivation:** We are working on performance evaluation for vLLM's more advanced features (chunked prefill, speculative decoding) and...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Continuous streaming of `UsageInfo` feature request ### 🚀 The feature, motivation and pitch **TLDR:** We would like an option we can enable to continuously stream the `UsageInfo` when using the streaming comp...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rations, the first few responses may contain zero tokens. There is no special indication that this has happened beyond just an empty string `""` being returned. We have found scenarios when `""` is actually valid token,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rformance implications for speculative decoding. We have considered an architectural change to fmperf where instead of counting the tokens for each streaming response, we simply wait until the final response has been re...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: se and counting the number of tokens in it. Currently vLLM provides no information about how many tokens are contained within each response. In most situation, it is just a single token. However, there are few scenarios...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
