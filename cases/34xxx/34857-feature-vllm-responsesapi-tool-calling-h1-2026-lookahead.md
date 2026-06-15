# vllm-project/vllm#34857: [Feature]: vLLM ResponsesAPI & Tool Calling H1 2026 lookahead

| 字段 | 值 |
| --- | --- |
| Issue | [#34857](https://github.com/vllm-project/vllm/issues/34857) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: vLLM ResponsesAPI & Tool Calling H1 2026 lookahead

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### looking back on the past few months vLLM has made a lot of progress on responsesAPI & tool calling in the past few months. To summarize, we've implemented the following: - MCP support for GPTOSS: after GPT-OSS was release in August 2025, we added a series of PRs to support running GPTOSS with MCP: https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/openai/responses/context.py#L663 - MCP support for all models: https://github.com/vllm-project/vllm/issues/30115. We added the ability to run MCP for _all_ models through a ParsableContext. - Function tool calling: https://github.com/vllm-project/vllm/pull/26874 - We've also added a series of improvements to vLLM responsesAPI, such as fixing tool parsing issues: https://github.com/vllm-project/vllm/pull/30304, supporting partial message generation https://github.com/vllm-project/vllm/pull/32100, adding debugging support with input / output tokens https://github.com/vllm-project/vllm/pull/33378 to name a few. - added renderer as a central interface to tokenize chat messages: https://github.com/vllm-project/vllm/pull/30200 - added the initial implementation of the Parser() class, whi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: arize, we've implemented the following: - MCP support for GPTOSS: after GPT-OSS was release in August 2025, we added a series of PRs to support running GPTOSS with MCP: https://github.com/vllm-project/vllm/blob/main/vll...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: vLLM ResponsesAPI & Tool Calling H1 2026 lookahead feature request;stale ### 🚀 The feature, motivation and pitch ### looking back on the past few months vLLM has made a lot of progress on responsesAPI & tool...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ds for perf optimizations, guided decode, and structured outputs. - 100% accuracy on verifying OSS model evals. https://github.com/MoonshotAI/K2-Vendor-Verifier. - Essentially, we would like to be able to reproduce eval...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ds for perf optimizations, guided decode, and structured outputs. - 100% accuracy on verifying OSS model evals. https://github.com/MoonshotAI/K2-Vendor-Verifier. - Essentially, we would like to be able to reproduce eval...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ) class, which allows for offloading responsesAPI parsing to be model specific: https://github.com/vllm-project/vllm/issues/32713 ### What's next and how can you help? For the next few months, at vLLM we would like to f...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
