# vllm-project/vllm#35407: [CI] DBO with DP+EP accuracy regression on GSM8K evaluation

| 字段 | 值 |
| --- | --- |
| Issue | [#35407](https://github.com/vllm-project/vllm/issues/35407) |
| 状态 | open |
| 标签 | stale;ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe |
| 子分类 | race_cond |
| Operator 关键词 | cuda;moe |
| 症状 | build_error |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI] DBO with DP+EP accuracy regression on GSM8K evaluation

### Issue 正文摘录

## Name of failing test - `v1/distributed/test_dbo.py::test_dbo_dp_ep_gsm8k[deepep_high_throughput]` ## Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries **Affected jobs:** Distributed Tests (2 GPUs)(H100) **Category:** test ## Describe the failing test The DBO (Dynamic Batch Orchestration) feature combined with Data Parallel (DP) and Expert Parallel (EP) is producing lower than expected accuracy on GSM8K evaluation. The test runs a GSM8K evaluation with a vLLM server configured with DBO enabled, data parallel size 2, and expert parallel enabled. The accuracy achieved falls below the minimum acceptable threshold of 0.62, indicating a quality regression in the DBO implementation when using the deepep_high_throughput all2all backend. This test is marked as xfail for Blackwell GPUs due to known instability, but failures can occur on other GPU types as well. ``` AssertionError: DBO+DP+EP accuracy too low (deepep_high_throughput): 0.590 < 0.620 ``` ## Relevant builds - [Build #53327](https://buildkite.com/vllm/ci/builds/53327) (d3a51da9) - [Distributed Tests (2 GPUs)(H100)](https://buildkite.com/vllm/ci/builds/53327#019c98c0-9dff-4564-a9c...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [CI] DBO with DP+EP accuracy regression on GSM8K evaluation stale;ci-failure ## Name of failing test - `v1/distributed/test_dbo.py::test_dbo_dp_ep_gsm8k[deepep_high_throughput]` ## Basic information - [ ] Flaky test - [...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [CI] DBO with DP+EP accuracy regression on GSM8K evaluation stale;ci-failure ## Name of failing test - `v1/distributed/test_dbo.py::test_dbo_dp_ep_gsm8k[deepep_high_throughput]` ## Basic information - [ ] Flaky test - [...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: d/test_dbo.py::test_dbo_dp_ep_gsm8k[deepep_high_throughput]` ## Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries **Affected jobs:** Distributed Tests (2 GPUs)(H100) **Cat...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [CI] DBO with DP+EP accuracy regression on GSM8K evaluation stale;ci-failure ## Name of failing test - `v1/distributed/test_dbo.py::test_dbo_dp_ep_gsm8k[deepep_high_throughput]` ## Basic information - [ ] Flaky test - [...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI] DBO with DP+EP accuracy regression on GSM8K evaluation stale;ci-failure ## Name of failing test - `v1/distributed/test_dbo.py::test_dbo_dp_ep_gsm8k[deepep_high_throughput]` ## Basic information - [ ] Flaky test -

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
