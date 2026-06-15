# vllm-project/vllm#6906: [Feature]: **Feature Request: Gateway for Model to Support Multiple Models Generation in a Given Context**

| 字段 | 值 |
| --- | --- |
| Issue | [#6906](https://github.com/vllm-project/vllm/issues/6906) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: **Feature Request: Gateway for Model to Support Multiple Models Generation in a Given Context**

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I would like to propose a feature that creates a gateway for a model, allowing for multiple models to generate content within a specific context. This is similar to the concept of speculative decoding, where it is sometimes unnecessary to query the model because the probability distribution is well-known. This feature can dramatically accelerate token generation in scenarios where the next token is deterministic and does not require the usual forward pass. For example, let's assume that I want to generate a JSON completion according to a specific JSON schema. Clearly, the keys of the JSON are mandatory in the response, so at some points, it is obvious what the next token prediction will be. ### Alternatives An alternative approach is to add a logit processor, which would mask the rest of the tokens in cases of deterministic tokens. However, this approach results in redundant processing to calculate the logits. ### Additional context In my specific case, I would like the model to generate answers according to the unified diff format. Therefore, in many states, the next token is well-known, especially when the model needs to generate token quo...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: **Feature Request: Gateway for Model to Support Multiple Models Generation in a Given Context** feature request;stale ### 🚀 The feature, motivation and pitch I would like to propose a feature that creates a g...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: **Feature Request: Gateway for Model to Support Multiple Models Generation in a Given Context** feature request;stale ### 🚀 The feature, motivation and pitch I would like to propose a feature that creates a g...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: tically accelerate token generation in scenarios where the next token is deterministic and does not require the usual forward pass. For example, let's assume that I want to generate a JSON completion according to a spec...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: or a model, allowing for multiple models to generate content within a specific context. This is similar to the concept of speculative decoding, where it is sometimes unnecessary to query the model because the probabilit...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: tically accelerate token generation in scenarios where the next token is deterministic and does not require the usual forward pass. For example, let's assume that I want to generate a JSON completion according to a spec...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
