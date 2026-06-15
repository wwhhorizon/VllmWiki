# vllm-project/vllm#6915: [Performance] [Speculative decoding]: Compute prepare inputs of the scoring model on GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#6915](https://github.com/vllm-project/vllm/issues/6915) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance] [Speculative decoding]: Compute prepare inputs of the scoring model on GPU

### Issue 正文摘录

### Proposal to improve performance TL;DR: Move speculative decoding `scoring` prepare inputs to GPU, so a CPU synchronization can be skipped. Currently, speculative decoding copies proposal tokens to CPU, where the spec decode framework then creates a ExecuteModelRequest for the target model to use in scoring. This synchronization (copying to CPU) takes ~1ms. When batch expansion is used (currently always used), it is another 0.5-1ms spent in python processing. Lastly, the ExecuteModelRequest is given to the scoring model, which runs prepare inputs (300µs). End-to-end, this optimization should shave off ~1.3ms for MQA and ~2ms for batch expansion. * In MQA, this is the logic which must be lowered to GPU: https://github.com/vllm-project/vllm/pull/6185/files#diff-fbbe61dca888281fce79855e67ce76bbaf6944d957a2963fced77e0f170f03c8R54-R70 * In batch expansion, this is the logic which must be lowered to GPU: https://github.com/vllm-project/vllm/blob/7f8d612d24c66e9b5f8c0aa6cb562e853e9523a0/vllm/spec_decode/batch_expansion.py#L64-L102 * Testing: suggest following the pattern in e2e block manager v2 tests, where we run v1 and v2 versions and compare greedy output: https://github.com/vllm-p...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Performance] [Speculative decoding]: Compute prepare inputs of the scoring model on GPU performance;stale ### Proposal to improve performance TL;DR: Move speculative decoding `scoring` prepare inputs to GPU, so a CPU s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: b5f8c0aa6cb562e853e9523a0/vllm/spec_decode/batch_expansion.py#L64-L102 * Testing: suggest following the pattern in e2e block manager v2 tests, where we run v1 and v2 versions and compare greedy output: https://github.co...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: lowing the pattern in e2e block manager v2 tests, where we run v1 and v2 versions and compare greedy output: https://github.com/vllm-project/vllm/blob/7f8d612d24c66e9b5f8c0aa6cb562e853e9523a0/tests/core/block/e2e/test_c...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ch_expansion.py#L64-L102 * Testing: suggest following the pattern in e2e block manager v2 tests, where we run v1 and v2 versions and compare greedy output: https://github.com/vllm-project/vllm/blob/7f8d612d24c66e9b5f8c0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: rformance] [Speculative decoding]: Compute prepare inputs of the scoring model on GPU performance;stale ### Proposal to improve performance TL;DR: Move speculative decoding `scoring` prepare inputs to GPU, so a CPU sync...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
