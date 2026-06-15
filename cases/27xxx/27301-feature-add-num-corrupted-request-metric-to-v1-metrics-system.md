# vllm-project/vllm#27301: [Feature]: Add num_corrupted_request metric to V1 metrics system.

| 字段 | 值 |
| --- | --- |
| Issue | [#27301](https://github.com/vllm-project/vllm/issues/27301) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add num_corrupted_request metric to V1 metrics system.

### Issue 正文摘录

### Description Currently, vLLM internally tracks a corrupted_requests_counter metric whenever a request produces invalid outputs (NaNs) due to model, engine, or hardware issues. However, this metric is not directly exposed to users in logs or Prometheus metrics. Exposing this metric would allow users to: - Detect model instability or misbehaving custom models. - Monitor runtime/engine health in production clusters. - Quickly identify hardware or distributed inference issues affecting outputs ### Motivation & Problem While NaN outputs are rare with well-tested models, they become critical for custom models in early development stages or may also arise within the runtime because of Engine/runtime issues. - Models may have numerical instability. - Hardware issues are more likely to surface The codebase already detects corrupted requests (Request.is_output_corrupted) when the env variable is set `VLLM_COMPUTE_NANS_IN_LOGITS = TRUE`, but this diagnostic information is completely hidden from users, as there are no metrics, no logging, and no monitoring. ### Proposed Idea Two Approaches for Corrupted Request Metrics that i am thinking of are: 1. Approach 1: CLI Config-Based (Current Imp...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: counter metric whenever a request produces invalid outputs (NaNs) due to model, engine, or hardware issues. However, this metric is not directly exposed to users in logs or Prometheus metrics. Exposing this metric would...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: within the runtime because of Engine/runtime issues. - Models may have numerical instability. - Hardware issues are more likely to surface The codebase already detects corrupted requests (Request.is_output_corrupted) wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add num_corrupted_request metric to V1 metrics system. feature request ### Description Currently, vLLM internally tracks a corrupted_requests_counter metric whenever a request produces invalid outputs (NaNs)...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: vllm serve model --include-corrupted-requests Pros: User-friendly, explicit control, follows vLLM patterns Cons: Adds new CLI argument, requires config changes I welcome suggestions and thoughts on the same, and would l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
