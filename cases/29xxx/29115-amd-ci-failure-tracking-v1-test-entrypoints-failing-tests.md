# vllm-project/vllm#29115: [AMD][CI Failure]: Tracking V1 Test entrypoints failing tests

| 字段 | 值 |
| --- | --- |
| Issue | [#29115](https://github.com/vllm-project/vllm/issues/29115) |
| 状态 | closed |
| 标签 | rocm;ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [AMD][CI Failure]: Tracking V1 Test entrypoints failing tests

### Issue 正文摘录

Remaining tests ([build](https://buildkite.com/vllm/amd-ci/builds/1080#019a981e-6cca-4b68-acd4-af786efa561b)): - v1/entrypoints/llm/test_struct_output_generate.py::test_structured_output[Qwen/Qwen2.5-1.5B-Instruct-lm-format-enforcer-auto-None] https://buildkite.com/vllm/amd-ci/builds/1080#019a981e-6cca-4b68-acd4-af786efa561b

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [AMD][CI Failure]: Tracking V1 Test entrypoints failing tests rocm;ci-failure Remaining tests ([build](https://buildkite.com/vllm/amd-ci/builds/1080#019a981e-6cca-4b68-acd4-af786efa561b)): - v1/entrypoints/llm/test_stru...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 1/entrypoints/llm/test_struct_output_generate.py::test_structured_output[Qwen/Qwen2.5-1.5B-Instruct-lm-format-enforcer-auto-None] https://buildkite.com/vllm/amd-ci/builds/1080#019a981e-6cca-4b68-acd4-af786efa561b
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [AMD][CI Failure]: Tracking V1 Test entrypoints failing tests rocm;ci-failure Remaining tests ([build](https://buildkite.com/vllm/amd-ci/builds/1080#019a981e-6cca-4b68-acd4-af786efa561b)): - v1/entrypoints/llm/test_stru...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [AMD][CI Failure]: Tracking V1 Test entrypoints failing tests rocm;ci-failure Remaining tests ([build](https://buildkite.com/vllm/amd-ci/builds/1080#019a981e-6cca-4b68-acd4-af786efa561b)): - v1/entrypoints/llm/test_stru...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
