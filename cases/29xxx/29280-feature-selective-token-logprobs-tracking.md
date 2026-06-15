# vllm-project/vllm#29280: [Feature]: Selective Token Logprobs Tracking

| 字段 | 值 |
| --- | --- |
| Issue | [#29280](https://github.com/vllm-project/vllm/issues/29280) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Selective Token Logprobs Tracking

### Issue 正文摘录

## Summary Add `track_token_ids` parameter to `SamplingParams` to enable efficient tracking of logprobs for specific tokens without requiring full vocabulary logprobs. ## Motivation ### Current Limitation Users who need logprobs for specific tokens (e.g., class labels, binary choices, special tokens) must choose between: 1. **Option A**: Use `logprobs=k` (top-k) and hope their tokens are in top-k - ❌ Unreliable: Target tokens may not be in top-k - ❌ Workaround: Assign `-9999.0` to missing tokens (see [Issue #8111](https://github.com/vllm-project/vllm/issues/8111)) 2. **Option B**: Use `max_logprobs=-1` and `logprobs=-1` to get full vocabulary - ❌ Memory overhead: ~150k logprobs per token (~1.2 MB per token) - ❌ Performance: Large GPU→CPU transfer - ❌ Wasteful: Discard 99.99% of retrieved logprobs ### Real-World Use Cases **1. Classification Tasks** ([Issue #8111](https://github.com/vllm-project/vllm/issues/8111)) ```python # User wants probabilities for: ["Technology", "Politics", "Sports", "Art"] # Currently must use logprobs=-1 or get unreliable -9999.0 values ``` **2. Binary Decision Making** ```python # Medical diagnosis: ["Positive", "Negative"] # Content moderation: ["Safe",...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: python # Track specific vocabulary items across long sequences # Analyze model confidence for hypothesis testing # Study attention to particular tokens ``` ## Proposed API ### SamplingParams Extension ```python from vll...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Selective Token Logprobs Tracking feature request;stale ## Summary Add `track_token_ids` parameter to `SamplingParams` to enable efficient tracking of logprobs for specific tokens without requiring full vocab...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ummary Add `track_token_ids` parameter to `SamplingParams` to enable efficient tracking of logprobs for specific tokens without requiring full vocabulary logprobs. ## Motivation ### Current Limitation Users who need log...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: "] # Content moderation: ["Safe", "Unsafe"] # Fact checking: ["True", "False"] ``` **3. AI-Generated Image Detection** (Our Use Case) ```python # Track probabilities for: ["real", "ai-generated", "synthetic", "authentic...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: special tokens) must choose between: 1. **Option A**: Use `logprobs=k` (top-k) and hope their tokens are in top-k - ❌ Unreliable: Target tokens may not be in top-k - ❌ Workaround: Assign `-9999.0` to missing tokens (see...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
