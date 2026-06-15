# vllm-project/vllm#32850: [RFC]: Clarify policy for Open Responses API extensions in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#32850](https://github.com/vllm-project/vllm/issues/32850) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Clarify policy for Open Responses API extensions in vLLM

### Issue 正文摘录

### Motivation. vLLM recently added support for the OpenAI-compatible `/v1/responses` API, which aligns with the public **[Open Responses](https://www.openresponses.org/specification)** specification. The specification [explicitly allows implementations to extend existing schemas with implementation-specific fields](https://www.openresponses.org/specification#extending-open-responses), as long as core semantics remain unchanged. At the same time, such extensions carry a known risk: future versions of the spec may introduce fields with the same names but different semantics, creating potential conflicts. A recent discussion around whether to expose additional vLLM-specific parameters through `/responses` (https://github.com/vllm-project/vllm/pull/32609) highlights an open question: **what is vLLM’s intended policy for extending the Responses API, and how should contributors evaluate such changes?** This question already matters in practice: ### Existing extensions in `/responses` The current vLLM Responses API already exposes fields that are not part of the Open Responses specification (e.g., `top_k`, `request_id`, `priority`, ...). This indicates that vLLM is already extending the...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC]: Clarify policy for Open Responses API extensions in vLLM RFC;stale ### Motivation. vLLM recently added support for the OpenAI-compatible `/v1/responses` API, which aligns with the public **[Open Responses](https:...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: igns with the public **[Open Responses](https://www.openresponses.org/specification)** specification. The specification [explicitly allows implementations to extend existing schemas with implementation-specific fields](...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: nded policy for extending the Responses API, and how should contributors evaluate such changes?** This question already matters in practice: ### Existing extensions in `/responses` The current vLLM Responses API already...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: LLM is already extending the Responses API beyond the vanilla spec. ### Divergence between Chat Completions and Responses The `/chat/completions` API currently exposes a broader set of vLLM-specific or non-standard para...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ch. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
