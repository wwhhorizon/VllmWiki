# vllm-project/vllm#7442: [Feature]: sliding window attention for odd layers

| 字段 | 值 |
| --- | --- |
| Issue | [#7442](https://github.com/vllm-project/vllm/issues/7442) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: sliding window attention for odd layers

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Thanks for fixing the soft-capping issue of the Gemma 2 models in the last release! I noticed there's still a [comment](https://github.com/vllm-project/vllm/blob/6aa33cb2ddd769e764a3312627cab5bffaa383cc/vllm/model_executor/models/gemma2.py#L143) and a warning when serving Gemma 2 models. Are there any plans to support sliding window attention for odd layers? Additionally, do we have any benchmarks on the performance impact of not using sliding windows on these layers? Cc @WoosukKwon ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: e, motivation and pitch Thanks for fixing the soft-capping issue of the Gemma 2 models in the last release! I noticed there's still a [comment](https://github.com/vllm-project/vllm/blob/6aa33cb2ddd769e764a3312627cab5bff...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: sliding window attention for odd layers feature request;stale ### 🚀 The feature, motivation and pitch Thanks for fixing the soft-capping issue of the Gemma 2 models in the last release! I noticed there's stil...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: e, motivation and pitch Thanks for fixing the soft-capping issue of the Gemma 2 models in the last release! I noticed there's still a [comment](https://github.com/vllm-project/vllm/blob/6aa33cb2ddd769e764a3312627cab5bff...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: rt sliding window attention for odd layers? Additionally, do we have any benchmarks on the performance impact of not using sliding windows on these layers? Cc @WoosukKwon ### Alternatives _No response_ ### Additional co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
