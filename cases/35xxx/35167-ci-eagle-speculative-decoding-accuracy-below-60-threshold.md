# vllm-project/vllm#35167: [CI] EAGLE speculative decoding accuracy below 60% threshold

| 字段 | 值 |
| --- | --- |
| Issue | [#35167](https://github.com/vllm-project/vllm/issues/35167) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI] EAGLE speculative decoding accuracy below 60% threshold

### Issue 正文摘录

## Name of failing test - `v1/e2e/test_spec_decode.py::test_eagle_correctness[FLASH_ATTN-llama3_eagle3]` ## Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries **Affected jobs:** V1 e2e + engine **Category:** test ## Describe the failing test The test_eagle_correctness test with llama3_eagle3 model fails because the speculative decoding output matches the reference output only 59 out of 100 times (59%), which is barely below the required 60% accuracy threshold. The test compares outputs from a reference LLM and a speculative LLM using EAGLE3 method (meta-llama/Llama-3.1-8B-Instruct with RedHatAI/Llama-3.1-8B-Instruct-speculator.eagle3, num_speculative_tokens=3) on 100 test prompts. The match rate of 59% is just 1% below the threshold, suggesting a flaky test or marginal accuracy regression. ``` AssertionError: assert 59 > 60 (matches below 60% threshold for EAGLE speculative decoding accuracy) ``` ## Relevant builds - [Build #52813](https://buildkite.com/vllm/ci/builds/52813) (22a97e66) - [V1 e2e + engine](https://buildkite.com/vllm/ci/builds/52813#019c8cf4-b618-4b13-98f0-ca89ea513e69) ## History of failing test - **First seen:** Build...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: g test - `v1/e2e/test_spec_decode.py::test_eagle_correctness[FLASH_ATTN-llama3_eagle3]` ## Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries **Affected jobs:** V1 e2e + en...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [CI] EAGLE speculative decoding accuracy below 60% threshold ci-failure ## Name of failing test - `v1/e2e/test_spec_decode.py::test_eagle_correctness[FLASH_ATTN-llama3_eagle3]` ## Basic information - [ ] Flaky test - [...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [CI] EAGLE speculative decoding accuracy below 60% threshold ci-failure ## Name of failing test - `v1/e2e/test_spec_decode.py::test_eagle_correctness[FLASH_ATTN-llama3_eagle3]` ## Basic information - [ ] Flaky test - [...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI] EAGLE speculative decoding accuracy below 60% threshold ci-failure ## Name of failing test - `v1/e2e/test_spec_decode.py::test_eagle_correctness[FLASH_ATTN-llama3_eagle3]` ## Basic information - [ ] Flaky test - [
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [CI] EAGLE speculative decoding accuracy below 60% threshold ci-failure ## Name of failing test - `v1/e2e/test_spec_decode.py::test_eagle_correctness[FLASH_ATTN-llama3_eagle3]` ## Basic information - [ ] Flaky test - [...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
