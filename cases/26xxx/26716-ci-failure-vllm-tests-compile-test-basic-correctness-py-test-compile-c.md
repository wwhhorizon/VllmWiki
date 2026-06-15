# vllm-project/vllm#26716: [CI Failure]: vllm/tests/compile/test_basic_correctness.py::test_compile_correctness[test_setting5]

| 字段 | 值 |
| --- | --- |
| Issue | [#26716](https://github.com/vllm-project/vllm/issues/26716) |
| 状态 | closed |
| 标签 | stale;ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: vllm/tests/compile/test_basic_correctness.py::test_compile_correctness[test_setting5]

### Issue 正文摘录

### Name of failing test vllm/tests/compile/test_basic_correctness.py::test_compile_correctness[test_setting5] ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Test is failing on H100, H200 and B200. Currently passing in CI. Test is commented out for now. ``` results are not the same: ref_result={'test': 'pure_text', 'logprobs': [TopLogprob(token='athol', bytes=[97, 116, 104, 111, 108], logprob=-10.38), TopLogprob(token='reconst', bytes=[114, 101, 99, 111, 110, 115, 116], logprob=-10.38), TopLogprob(token='User', bytes=[85, 115, 101, 114], logprob=-10.38), TopLogprob(token='lagen', bytes=[108, 97, 103, 101, 110], logprob=-10.38), TopLogprob(token='ів', bytes=[209, 150, 208, 178], logprob=-10.38)]} E compare_result={'test': 'pure_text', 'logprobs': [TopLogprob(token='athol', bytes=[97, 116, 104, 111, 108], logprob=-10.38), TopLogprob(token='reconst', bytes=[114, 101, 99, 111, 110, 115, 116], logprob=-10.38), TopLogprob(token='User', bytes=[85, 115, 101, 114], logprob=-10.38), TopLogprob(token='Design', bytes=[68, 101, 115, 105, 103, 110], logprob=-10.38), TopLogprob(tok...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: vllm/tests/compile/test_basic_correctness.py::test_compile_correctness[test_setting5] stale;ci-failure ### Name of failing test vllm/tests/compile/test_basic_correctness.py::test_compile_correctness[test_se
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: in `transformers`) ### 🧪 Describe the failing test Test is failing on H100, H200 and B200. Currently passing in CI. Test is commented out for now. ``` results are not the same: ref_result={'test': 'pure_text', 'logprobs...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ctness[test_setting5] ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Test is failing on H100, H200 and...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: sic_correctness.py::test_compile_correctness[test_setting5] ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: mpile/test_basic_correctness.py::test_compile_correctness[test_setting5] stale;ci-failure ### Name of failing test vllm/tests/compile/test_basic_correctness.py::test_compile_correctness[test_setting5] ### Basic informat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
