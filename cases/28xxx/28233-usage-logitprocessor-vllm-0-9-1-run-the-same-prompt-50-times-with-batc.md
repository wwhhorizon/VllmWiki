# vllm-project/vllm#28233: [Usage]: LogitProcessor vLLM 0.9.1 run the same prompt 50 times with batching, apply logitprocessor independently on each

| 字段 | 值 |
| --- | --- |
| Issue | [#28233](https://github.com/vllm-project/vllm/issues/28233) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: LogitProcessor vLLM 0.9.1 run the same prompt 50 times with batching, apply logitprocessor independently on each

### Issue 正文摘录

### Your current environment Goal Run the same prompt 50 times through vLLM 0.9.1, generating independent outputs with a custom LogitsProcessor that forces a comma token after some pattern "xyz" appears in each generation. What You Want Batched execution: Process all 50 generations efficiently in parallel Independent state: Each of the 50 generations should have its own state in the logits processor Pattern detection: When text ends with "xyz", mask all tokens except comma }, One-time application: Each generation should only apply the comma mask once Current Hurdles 1. Processor Signature Confusion vLLM V0 (0.9.1) uses signature: __call__(prompt_token_ids, generated_token_ids, logits) prompt_token_ids: The input prompt tokens (same for all 50) generated_token_ids: Tokens generated so far (different per generation) Problem: No built-in request ID to distinguish between the 50 generations 2. State Management When using the same prompt 50 times: All generations share identical prompt_token_ids Can't use prompt as unique identifier Using generated_token_ids as key works initially, but becomes complex as sequences diverge State dictionary grows indefinitely without cleanup 3. Batching...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 50 times with batching, apply logitprocessor independently on each usage;stale ### Your current environment Goal Run the same prompt 50 times through vLLM 0.9.1, generating independent outputs with a custom LogitsProces...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ration. What You Want Batched execution: Process all 50 generations efficiently in parallel Independent state: Each of the 50 generations should have its own state in the logits processor Pattern detection: When text en...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: llm ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
