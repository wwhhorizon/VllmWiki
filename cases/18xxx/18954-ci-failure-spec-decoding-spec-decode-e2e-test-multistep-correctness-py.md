# vllm-project/vllm#18954: [CI Failure]: Spec Decoding - spec_decode/e2e/test_multistep_correctness.py

| 字段 | 值 |
| --- | --- |
| Issue | [#18954](https://github.com/vllm-project/vllm/issues/18954) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Spec Decoding - spec_decode/e2e/test_multistep_correctness.py

### Issue 正文摘录

### Name of failing test `test_spec_decode_e2e_greedy_correctness_tiny_model_large_bs_diff_output_len` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/ci/builds/21085/steps?jid=01971f59-be20-45f4-9e11-dcd3b1e67173 ### 📝 History of failing test Started failing since yesterday since today's nightly caught the failure https://buildkite.com/organizations/vllm/analytics/suites/ci-1/tests/a8e2f4a9-a7cf-81ec-ba3e-3a1e8b022a79?period=1day&tags=scm.branch%3Amain ### CC List. @mgoin @njhill

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Spec Decoding - spec_decode/e2e/test_multistep_correctness.py ci-failure ### Name of failing test `test_spec_decode_e2e_greedy_correctness_tiny_model_large_bs_diff_output_len` ### Basic information - [ ]
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ### Name of failing test `test_spec_decode_e2e_greedy_correctness_tiny_model_large_bs_diff_output_len` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: e_bs_diff_output_len` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/ci/buil...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [CI Failure]: Spec Decoding - spec_decode/e2e/test_multistep_correctness.py ci-failure ### Name of failing test `test_spec_decode_e2e_greedy_correctness_tiny_model_large_bs_diff_output_len` ### Basic information - [ ] F...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: Spec Decoding - spec_decode/e2e/test_multistep_correctness.py ci-failure ### Name of failing test `test_spec_decode_e2e_greedy_correctness_tiny_model_large_bs_diff_output_len` ### Basic information - [ ] F...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
