# vllm-project/vllm#34460: [CI Failure]: Distributed Tests (2 GPUs)(H100) test_dbo.py

| 字段 | 值 |
| --- | --- |
| Issue | [#34460](https://github.com/vllm-project/vllm/issues/34460) |
| 状态 | open |
| 标签 | stale;ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe |
| 子分类 | race_cond |
| Operator 关键词 | cuda;moe |
| 症状 |  |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: Distributed Tests (2 GPUs)(H100) test_dbo.py

### Issue 正文摘录

### Name of failing test `tests/v1/distributed/test_dbo.py::test_dbo_dp_ep_gsm8k[deepep_low_latency]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test The CI test failed with AssertionError: DBO+DP+EP accuracy too low (deepep_low_latency): 0.000 assert accuracy >= MIN_ACCURACY, ( f"DBO+DP+EP accuracy too low ({all2all_backend}): " f"{accuracy:.3f} = 0.62 tests/v1/distributed/test_dbo.py:106: AssertionError ``` ### 📝 History of failing test The CI test first failed on Feb 12, 2026: https://buildkite.com/vllm/ci/builds/51276/steps/canvas?jid=019c50a7-7d89-4a5d-a66b-2e228f4c7939&tab=output ### CC List. _No response_

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [CI Failure]: Distributed Tests (2 GPUs)(H100) test_dbo.py stale;ci-failure ### Name of failing test `tests/v1/distributed/test_dbo.py::test_dbo_dp_ep_gsm8k[deepep_low_latency]` ### Basic information - [ ] Flaky test -...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [CI Failure]: Distributed Tests (2 GPUs)(H100) test_dbo.py stale;ci-failure ### Name of failing test `tests/v1/distributed/test_dbo.py::test_dbo_dp_ep_gsm8k[deepep_low_latency]` ### Basic information - [ ] Flaky test -...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [deepep_low_latency]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test The CI test failed with AssertionE...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Distributed Tests (2 GPUs)(H100) test_dbo.py stale;ci-failure ### Name of failing test `tests/v1/distributed/test_dbo.py::test_dbo_dp_ep_gsm8k[deepep_low_latency]` ### Basic information - [ ] Flaky test -
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: uted/test_dbo.py::test_dbo_dp_ep_gsm8k[deepep_low_latency]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
