# vllm-project/vllm#26454: [CI Failure]: Distributed tests fail comparing -O1 and -O0 in `compile/test_basic_correctness.py::test_compile_correctness[test_setting5]`

| 字段 | 值 |
| --- | --- |
| Issue | [#26454](https://github.com/vllm-project/vllm/issues/26454) |
| 状态 | closed |
| 标签 | torch.compile;ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Distributed tests fail comparing -O1 and -O0 in `compile/test_basic_correctness.py::test_compile_correctness[test_setting5]`

### Issue 正文摘录

### Name of failing test tests/compile/test_basic_correctness.py::test_compile_correctness[test_setting5] ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test It seems like the logprobs no longer match between compilation levels/modes 0 and 1: ``` [2025-10-08T05:24:19Z] FAILED compile/test_basic_correctness.py::test_compile_correctness[test_setting5] - AssertionError: Results for model='microsoft/Phi-3.5-vision-instruct' are not the same. [2025-10-08T05:24:19Z] ref_args=['--enforce-eager', '--trust-remote-code', '--max-model-len', '2048', '-pp', '2', '-tp', '1', '-O0'] ref_envs={} [2025-10-08T05:24:19Z] compare_args=['--enforce-eager', '--trust-remote-code', '--max-model-len', '2048', '-pp', '2', '-tp', '1', '-O1'] compare_envs={} [2025-10-08T05:24:19Z] ref_result={'test': 'text_image', 'logprobs': [TopLogprob(token='reichen', bytes=[114, 101, 105, 99, 104, 101, 110], logprob=-10.37547492980957), TopLogprob(token='Serv', bytes=[83, 101, 114, 118], logprob=-10.375476837158203), TopLogprob(token='жи', bytes=[208, 182, 208, 184], logprob=-10.375476837158203), TopLogprob(token...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Distributed tests fail comparing -O1 and -O0 in `compile/test_basic_correctness.py::test_compile_correctness[test_setting5]` torch.compile;ci-failure ### Name of failing test tests/compile/test_basic_correc
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: sic_correctness.py::test_compile_correctness[test_setting5] ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ctness[test_setting5] ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test It seems like the logprobs no long...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: Distributed tests fail comparing -O1 and -O0 in `compile/test_basic_correctness.py::test_compile_correctness[test_setting5]` torch.compile;ci-failure ### Name of failing test tests/compile/test_basic_corre...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
