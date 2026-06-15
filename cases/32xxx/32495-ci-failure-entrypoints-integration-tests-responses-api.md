# vllm-project/vllm#32495: [CI Failure]: Entrypoints Integration Tests (Responses API)

| 字段 | 值 |
| --- | --- |
| Issue | [#32495](https://github.com/vllm-project/vllm/issues/32495) |
| 状态 | closed |
| 标签 | help wanted;ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Entrypoints Integration Tests (Responses API)

### Issue 正文摘录

### Name of failing test `test_function_calling_with_streaming_types[openai/gpt-oss-20b] ` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/ci/builds/47466#019bc92c-fc01-4ecb-83b3-362c5805e161 ### 📝 History of failing test https://buildkite.com/vllm/ci/builds/47466#019bc92c-fc01-4ecb-83b3-362c5805e161 ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Entrypoints Integration Tests (Responses API) help wanted;ci-failure ### Name of failing test `test_function_calling_with_streaming_types[openai/gpt-oss-20b] ` ### Basic information - [x] Flaky test - [ ]
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Name of failing test `test_function_calling_with_streaming_types[openai/gpt-oss-20b] ` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) #...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: openai/gpt-oss-20b] ` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/ci/buil...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: Entrypoints Integration Tests (Responses API) help wanted;ci-failure ### Name of failing test `test_function_calling_with_streaming_types[openai/gpt-oss-20b] ` ### Basic information - [x] Flaky test - [ ]...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
