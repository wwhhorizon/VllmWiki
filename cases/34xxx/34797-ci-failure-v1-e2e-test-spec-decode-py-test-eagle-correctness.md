# vllm-project/vllm#34797: [CI Failure]: v1/e2e/test_spec_decode.py::test_eagle_correctness

| 字段 | 值 |
| --- | --- |
| Issue | [#34797](https://github.com/vllm-project/vllm/issues/34797) |
| 状态 | open |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: v1/e2e/test_spec_decode.py::test_eagle_correctness

### Issue 正文摘录

### Name of failing test v1/e2e/test_spec_decode.py::test_eagle_correctness ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED v1/e2e/test_spec_decode.py::test_eagle_correctness[FLASH_ATTN-llama3_eagle3] - assert 57 > 60 FAILED v1/e2e/test_spec_decode.py::test_eagle_correctness[FLASH_ATTN-deepseek_eagle] - RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} ``` ### 📝 History of failing test https://buildkite.com/vllm/ci/builds/52052/steps/canvas?sid=019c6f8d-c40a-4054-a55d-963d026333f0 ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: v1/e2e/test_spec_decode.py::test_eagle_correctness ci-failure ### Name of failing test v1/e2e/test_spec_decode.py::test_eagle_correctness ### Basic information - [x] Flaky test - [ ] Can reproduce locally
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ng test v1/e2e/test_spec_decode.py::test_eagle_correctness ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: est_eagle_correctness ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED v1/e2e/test_spec_decode...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [CI Failure]: v1/e2e/test_spec_decode.py::test_eagle_correctness ci-failure ### Name of failing test v1/e2e/test_spec_decode.py::test_eagle_correctness ### Basic information - [x] Flaky test - [ ] Can reproduce locally...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: v1/e2e/test_spec_decode.py::test_eagle_correctness ci-failure ### Name of failing test v1/e2e/test_spec_decode.py::test_eagle_correctness ### Basic information - [x] Flaky test - [ ] Can reproduce locally...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
