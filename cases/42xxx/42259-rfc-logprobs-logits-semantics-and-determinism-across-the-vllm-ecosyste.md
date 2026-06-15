# vllm-project/vllm#42259: [RFC]: Logprobs/Logits Semantics and Determinism Across the vLLM Ecosystem

| 字段 | 值 |
| --- | --- |
| Issue | [#42259](https://github.com/vllm-project/vllm/issues/42259) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Logprobs/Logits Semantics and Determinism Across the vLLM Ecosystem

### Issue 正文摘录

## Motivation Several open bugs and in-flight fixes across vLLM, vLLM-Ascend, and VERL point to the same underlying problem: the semantics and determinism of returned logits/logprobs are not specified tightly enough. This shows up as: - prompt-side values ignoring `logprobs_mode` - request-order-dependent `prompt_logprobs` under prefix caching - duplicated sampled tokens in `top_logprobs` - backend-specific mode propagation gaps - rollout/trainer logprob mismatch in VERL ## Problem Statement The same logical request can produce different answers depending on: - whether prompt-side or decode-side probabilities are returned - raw vs processed `logprobs_mode` - prefix caching being enabled - streaming delta behavior - sampled token overlap with top-k/top-p output - backend implementation details in core vLLM, vLLM-Ascend, or VERL integration paths That creates user-visible wrong values, non-deterministic scoring, and training signal mismatch. ## Proposed Change Define a shared contract for: - `logits` - `logprobs` - `prompt_logprobs` - `top_logprobs` The contract should cover: - raw vs processed semantics - deterministic behavior with prefix caching - streaming delta behavior - de-du...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: robs` - backend-specific mode propagation gaps - rollout/trainer logprob mismatch in VERL ## Problem Statement The same logical request can produce different answers depending on: - whether prompt-side or decode-side pr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: , or VERL integration paths That creates user-visible wrong values, non-deterministic scoring, and training signal mismatch. ## Proposed Change Define a shared contract for: - `logits` - `logprobs` - `prompt_logprobs` -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ough. This shows up as: - prompt-side values ignoring `logprobs_mode` - request-order-dependent `prompt_logprobs` under prefix caching - duplicated sampled tokens in `top_logprobs` - backend-specific mode propagation ga...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: bs` under prefix caching - duplicated sampled tokens in `top_logprobs` - backend-specific mode propagation gaps - rollout/trainer logprob mismatch in VERL ## Problem Statement The same logical request can produce differ...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: em: the semantics and determinism of returned logits/logprobs are not specified tightly enough. This shows up as: - prompt-side values ignoring `logprobs_mode` - request-order-dependent `prompt_logprobs` under prefix ca...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
