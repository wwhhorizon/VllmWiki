# vllm-project/vllm#35168: [CI] Ngram speculative decoding accuracy below 66% threshold

| 字段 | 值 |
| --- | --- |
| Issue | [#35168](https://github.com/vllm-project/vllm/issues/35168) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI] Ngram speculative decoding accuracy below 66% threshold

### Issue 正文摘录

## Name of failing test - `v1/e2e/test_spec_decode.py::test_ngram_and_suffix_correctness[speculative_config0]` ## Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries **Affected jobs:** V1 e2e + engine **Category:** test ## Describe the failing test The test_ngram_and_suffix_correctness test with ngram method fails because the speculative decoding output matches the reference output only 54 out of 100 times (54%), which is below the required 66% accuracy threshold. The test compares outputs from a reference LLM and a speculative LLM using ngram decoding (prompt_lookup_max=5, prompt_lookup_min=3, num_speculative_tokens=3) on 100 test prompts. The low match rate indicates that ngram speculative decoding is producing different outputs than the baseline model more frequently than expected. ``` AssertionError: assert 54 >= 66 (matches below 66% threshold for ngram speculative decoding accuracy) ``` ## Relevant builds - [Build #52813](https://buildkite.com/vllm/ci/builds/52813) (22a97e66) - [V1 e2e + engine](https://buildkite.com/vllm/ci/builds/52813#019c8cf4-b618-4b13-98f0-ca89ea513e69) ## History of failing test - **First seen:** Build #528...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: [CI] Ngram speculative decoding accuracy below 66% threshold ci-failure ## Name of failing test - `v1/e2e/test_spec_decode.py::test_ngram_and_suffix_correctness[speculative_config0]` ## Basic information - [ ] Flaky tes...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI] Ngram speculative decoding accuracy below 66% threshold ci-failure ## Name of failing test - `v1/e2e/test_spec_decode.py::test_ngram_and_suffix_correctness[speculative_config0]` ## Basic information - [ ] Flaky te
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 1/e2e/test_spec_decode.py::test_ngram_and_suffix_correctness[speculative_config0]` ## Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries **Affected jobs:** V1 e2e + engine...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [CI] Ngram speculative decoding accuracy below 66% threshold ci-failure ## Name of failing test - `v1/e2e/test_spec_decode.py::test_ngram_and_suffix_correctness[speculative_config0]` ## Basic information - [ ] Flaky tes...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI] Ngram speculative decoding accuracy below 66% threshold ci-failure ## Name of failing test - `v1/e2e/test_spec_decode.py::test_ngram_and_suffix_correctness[speculative_config0]` ## Basic information - [ ] Flaky tes...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
