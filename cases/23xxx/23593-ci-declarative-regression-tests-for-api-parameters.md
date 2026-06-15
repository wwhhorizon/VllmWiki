# vllm-project/vllm#23593: [CI]: Declarative regression tests for API parameters

| 字段 | 值 |
| --- | --- |
| Issue | [#23593](https://github.com/vllm-project/vllm/issues/23593) |
| 状态 | open |
| 标签 | ci/build;unstale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI]: Declarative regression tests for API parameters

### Issue 正文摘录

For systematic/efficient coverage of request parameters, including different combinations, we can introduce a declarative test where we have entries with different request parameters / prompts and a ground truth of the output (assuming greedy or seeded sampling). The test then runs all of these requests in parallel in a random order and verifies the outputs match. We can run this in FP32 to avoid precision errors. See old example from IBM TGIS: https://github.com/IBM/text-generation-inference/blob/main/integration_tests/test_cases_bloom560m.yaml. This tested a gRPC API but we can do the equivalent with the OpenAI APIs.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI]: Declarative regression tests for API parameters ci/build;unstale For systematic/efficient coverage of request parameters, including different combinations, we can introduce a declarative test where we have entries...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [CI]: Declarative regression tests for API parameters ci/build;unstale For systematic/efficient coverage of request parameters, including different combinations, we can introduce a declarative test where we have entries...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI]: Declarative regression tests for API parameters ci/build;unstale For systematic/efficient coverage of request parameters, including different combinations, we can introduce a declarative test where we have entries...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: m order and verifies the outputs match. We can run this in FP32 to avoid precision errors. See old example from IBM TGIS: https://github.com/IBM/text-generation-inference/blob/main/integration_tests/test_cases_bloom560m...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: m/IBM/text-generation-inference/blob/main/integration_tests/test_cases_bloom560m.yaml. This tested a gRPC API but we can do the equivalent with the OpenAI APIs.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
