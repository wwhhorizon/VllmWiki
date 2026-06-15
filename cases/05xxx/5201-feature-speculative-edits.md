# vllm-project/vllm#5201: [Feature]: Speculative edits

| 字段 | 值 |
| --- | --- |
| Issue | [#5201](https://github.com/vllm-project/vllm/issues/5201) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Speculative edits

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Folks at Cursor came up with new speculative method called spec edits is a really cool approach and vLLM should have it! Per @cadedaniel one may implement this in vLLM as an alternative to "SpecDecodeWorker" that specializes in spec edits ("SpecEditWorker"). The reason is that the current framework makes assumptions about the immutability of the prefixes. But a SpecEditWorker would still benefit from surrounding work in vLLM (like the lookahead scheduler, sampling optimizations, and subcomponents of the spec decode framework). ### Alternatives _No response_ ### Additional context > With code edits, we have a strong prior on the draft tokens at any point in time, so we can speculate on future tokens using a deterministic algorithm rather than a draft model https://cursor.sh/blog/instant-apply

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Feature]: Speculative edits feature request;stale ### 🚀 The feature, motivation and pitch Folks at Cursor came up with new speculative method called spec edits is a really cool approach and vLLM should have it! Per @ca...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: okens at any point in time, so we can speculate on future tokens using a deterministic algorithm rather than a draft model https://cursor.sh/blog/instant-apply
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: y implement this in vLLM as an alternative to "SpecDecodeWorker" that specializes in spec edits ("SpecEditWorker"). The reason is that the current framework makes assumptions about the immutability of the prefixes. But...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ate on future tokens using a deterministic algorithm rather than a draft model https://cursor.sh/blog/instant-apply
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: okens at any point in time, so we can speculate on future tokens using a deterministic algorithm rather than a draft model https://cursor.sh/blog/instant-apply

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
