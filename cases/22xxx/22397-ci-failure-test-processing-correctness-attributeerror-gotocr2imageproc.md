# vllm-project/vllm#22397: [CI Failure]: test_processing_correctness - AttributeError: 'GotOcr2ImageProcessorFast' object has no attribute 'get_number_of_image_tokens'. 

| 字段 | 值 |
| --- | --- |
| Issue | [#22397](https://github.com/vllm-project/vllm/issues/22397) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: test_processing_correctness - AttributeError: 'GotOcr2ImageProcessorFast' object has no attribute 'get_number_of_image_tokens'. 

### Issue 正文摘录

### Name of failing test models/multimodal/processing/test_common.py::test_processing_correctness[1.0-32-0.3-internlm/Intern-S1] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Test failure introduced by a GPT-OSS PR [2025-08-06T21:09:08Z] FAILED models/multimodal/processing/test_common.py::test_processing_correctness[1.0-32-0.3-internlm/Intern-S1] - AttributeError: 'GotOcr2ImageProcessorFast' object has no attribute 'get_number_of_image_tokens'. Did you mean: 'get_number_of_image_patches'? ### 📝 History of failing test https://buildkite.com/organizations/vllm/analytics/suites/ci-1/tests/396bc3d2-b2a6-8b15-b051-5a341f82961c?branch=main&period=14days appears to have been introduced by #223278 [test run history](https://buildkite.com/organizations/vllm/analytics/suites/ci-1/runs/e7f09665-d87e-8618-a7a1-fb8055c9fd40) ### CC List. _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: bute 'get_number_of_image_tokens'. ci-failure ### Name of failing test models/multimodal/processing/test_common.py::test_processing_correctness[1.0-32-0.3-internlm/Intern-S1] ### Basic information - [ ] Flaky test - [ ]...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: test_processing_correctness - AttributeError: 'GotOcr2ImageProcessorFast' object has no attribute 'get_number_of_image_tokens'. ci-failure ### Name of failing test models/multimodal/processing/test_common.
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: 3-internlm/Intern-S1] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Test failure introduced by a GPT-O...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: test_processing_correctness - AttributeError: 'GotOcr2ImageProcessorFast' object has no attribute 'get_number_of_image_tokens'. ci-failure ### Name of failing test models/multimodal/processing/test_common....

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
