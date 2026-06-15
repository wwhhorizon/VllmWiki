# vllm-project/vllm#29114: [AMD][CI Failure]: Tracking V1 Test e2e + engine failing tests

| 字段 | 值 |
| --- | --- |
| Issue | [#29114](https://github.com/vllm-project/vllm/issues/29114) |
| 状态 | closed |
| 标签 | rocm;ci-failure |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [AMD][CI Failure]: Tracking V1 Test e2e + engine failing tests

### Issue 正文摘录

Remaining tests ([build](https://buildkite.com/vllm/amd-ci/builds/1080#019a981e-6cc9-4e5c-a751-4d9ff1d961e3)): - v1/e2e/test_async_scheduling.py - v1/e2e/test_correctness_sliding_window.py - v1/e2e/test_kv_sharing_fast_prefill.py - v1/e2e/test_spec_decode.py::test_ngram_and_suffix_correctness[speculative_config1] https://buildkite.com/vllm/amd-ci/builds/1080#019a981e-6cc9-4e5c-a751-4d9ff1d961e3

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: v1/e2e/test_correctness_sliding_window.py - v1/e2e/test_kv_sharing_fast_prefill.py - v1/e2e/test_spec_decode.py::test_ngram_and_suffix_correctness[speculative_config1] https://buildkite.com/vllm/amd-ci/builds/1080#019a9...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [AMD][CI Failure]: Tracking V1 Test e2e + engine failing tests rocm;ci-failure Remaining tests ([build](https://buildkite.com/vllm/amd-ci/builds/1080#019a981e-6cc9-4e5c-a751-4d9ff1d961e3)): - v1/e2e/test_async_schedulin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [AMD][CI Failure]: Tracking V1 Test e2e + engine failing tests rocm;ci-failure Remaining tests ([build](https://buildkite.com/vllm/amd-ci/builds/1080#019a981e-6cc9-4e5c-a751-4d9ff1d961e3)): - v1/e2e/test_async_schedulin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 1/e2e/test_spec_decode.py::test_ngram_and_suffix_correctness[speculative_config1] https://buildkite.com/vllm/amd-ci/builds/1080#019a981e-6cc9-4e5c-a751-4d9ff1d961e3
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [AMD][CI Failure]: Tracking V1 Test e2e + engine failing tests rocm;ci-failure Remaining tests ([build](https://buildkite.com/vllm/amd-ci/builds/1080#019a981e-6cc9-4e5c-a751-4d9ff1d961e3)): - v1/e2e/test_async_schedulin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
