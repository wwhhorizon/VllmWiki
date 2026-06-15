# vllm-project/vllm#29116: [AMD][CI Failure]: Tracking V1 Test others failing tests

| 字段 | 值 |
| --- | --- |
| Issue | [#29116](https://github.com/vllm-project/vllm/issues/29116) |
| 状态 | closed |
| 标签 | rocm;ci-failure |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [AMD][CI Failure]: Tracking V1 Test others failing tests

### Issue 正文摘录

Remaining tests ([build](https://buildkite.com/vllm/amd-ci/builds/1080#019a981e-6cc9-4e5c-a751-4d9ff1d961e3)): - v1/sample/test_logprobs.py::test_spec_decode_logprobs[model_setup0-raw_logits] - v1/sample/test_sampling_params_e2e.py::test_bad_words - AssertionError... (tracking in https://github.com/vllm-project/vllm/issues/27945) https://buildkite.com/vllm/amd-ci/builds/1080#019a981e-6cc9-4e5c-a751-4d9ff1d961e3

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [AMD][CI Failure]: Tracking V1 Test others failing tests rocm;ci-failure Remaining tests ([build](https://buildkite.com/vllm/amd-ci/builds/1080#019a981e-6cc9-4e5c-a751-4d9ff1d961e3)): - v1/sample/test_logprobs.py::test_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [AMD][CI Failure]: Tracking V1 Test others failing tests rocm;ci-failure Remaining tests ([build](https://buildkite.com/vllm/amd-ci/builds/1080#019a981e-6cc9-4e5c-a751-4d9ff1d961e3)): - v1/sample/test_logprobs.py::test_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 4d9ff1d961e3)): - v1/sample/test_logprobs.py::test_spec_decode_logprobs[model_setup0-raw_logits] - v1/sample/test_sampling_params_e2e.py::test_bad_words - AssertionError... (tracking in https://github.com/vllm-project/v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: -6cc9-4e5c-a751-4d9ff1d961e3)): - v1/sample/test_logprobs.py::test_spec_decode_logprobs[model_setup0-raw_logits] - v1/sample/test_sampling_params_e2e.py::test_bad_words - AssertionError... (tracking in https://github.co...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [AMD][CI Failure]: Tracking V1 Test others failing tests rocm;ci-failure Remaining tests ([build](https://buildkite.com/vllm/amd-ci/builds/1080#019a981e-6cc9-4e5c-a751-4d9ff1d961e3)): - v1/sample/test_logprobs.py::test_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
