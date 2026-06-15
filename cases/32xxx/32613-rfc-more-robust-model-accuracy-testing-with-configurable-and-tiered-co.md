# vllm-project/vllm#32613: [RFC]: More robust model accuracy testing with configurable and tiered coverage

| 字段 | 值 |
| --- | --- |
| Issue | [#32613](https://github.com/vllm-project/vllm/issues/32613) |
| 状态 | open |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: More robust model accuracy testing with configurable and tiered coverage

### Issue 正文摘录

### Motivation. This RFC proposes to increase the scope and resource investment of vLLM's model accuracy testing infra to catch accuracy regressions early on. Accuracy issues have been noticeably more frequent given the added optimizations, kernel backends, and models. Once the degradations are merged into main, they are difficult to detect, hard to debug, and much more likely to affect production deployment compared to functional breakages or perf regressions which are easier to detect.. A quick search in our github issues reflect the current state of accuracy issues: https://github.com/vllm-project/vllm/issues?q=is%3Aissue%20accuracy Some known gaps in our current tests (AFAIK): 1. Need more per-commit testing (especially [blackwell](https://github.com/vllm-project/vllm/blob/07d614511f8b233650596a86b701faf0ad3a41a1/.buildkite/test-pipeline.yaml\#L961-L969 ) ) and tiered testing (per-commit, nightly, weekly) to gate against degradations. 2. Lack the ability to customize a models accuracy criteria based on its capability. GSM8k can be too easy for SOTA models even with noticeable accuracy degradations. We also need more tool-calling evals. 3. Deployment recipes in lm-eval tests ca...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: l breakages or perf regressions which are easier to detect.. A quick search in our github issues reflect the current state of accuracy issues: https://github.com/vllm-project/vllm/issues?q=is%3Aissue%20accuracy Some kno...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [RFC]: More robust model accuracy testing with configurable and tiered coverage RFC;stale ### Motivation. This RFC proposes to increase the scope and resource investment of vLLM's model accuracy testing infra to catch a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [RFC]: More robust model accuracy testing with configurable and tiered coverage RFC;stale ### Motivation. This RFC proposes to increase the scope and resource investment of vLLM's model accuracy testing infra to catch a...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: have been noticeably more frequent given the added optimizations, kernel backends, and models. Once the degradations are merged into main, they are difficult to detect, hard to debug, and much more likely to affect prod...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: gaps in our current tests (AFAIK): 1. Need more per-commit testing (especially [blackwell](https://github.com/vllm-project/vllm/blob/07d614511f8b233650596a86b701faf0ad3a41a1/.buildkite/test-pipeline.yaml\#L961-L969 ) )...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
