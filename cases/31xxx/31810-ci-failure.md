# vllm-project/vllm#31810: [CI Failure]:

| 字段 | 值 |
| --- | --- |
| Issue | [#31810](https://github.com/vllm-project/vllm/issues/31810) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:

### Issue 正文摘录

### Name of failing test `pytest -v -s entrypoints/openai/test_default_mm_loras.py::test_default_mm_lora_chat_completions -k Phi-4` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Unrelated job failed https://buildkite.com/vllm/ci/builds/45604#019b9196-dca3-4e4d-b478-4877723546b1 ### 📝 History of failing test Sees fine based on history: https://buildkite.com/organizations/vllm/analytics/suites/ci-1/tests/f51cc3aa-4045-86db-a9c9-6d5024151beb?branch=main&columns%5B%5D=reliability&columns%5B%5D=duration_avg&columns%5B%5D=passed_on_retry_count&columns%5B%5D=latest_passed_on_retry&order=DESC&query=tests%2Fentrypoints%2Fopenai%2Ftest_default_mm_loras.py&sort_by=passed_on_retry_count&view=flaky ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: ci-failure ### Name of failing test `pytest -v -s entrypoints/openai/test_default_mm_loras.py::test_default_mm_lora_chat_completions -k Phi-4` ### Basic information - [x] Flaky test - [ ] Can reproduce lo
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: completions -k Phi-4` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Unrelated job failed https://build...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: m_loras.py::test_default_mm_lora_chat_completions -k Phi-4` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: ci-failure ### Name of failing test `pytest -v -s entrypoints/openai/test_default_mm_loras.py::test_default_mm_lora_chat_completions -k Phi-4` ### Basic information - [x] Flaky test - [ ] Can reproduce loc...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
