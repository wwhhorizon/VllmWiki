# vllm-project/vllm#35769: [CI Failure]:  mi325_1: Quantized Models Test

| 字段 | 值 |
| --- | --- |
| Issue | [#35769](https://github.com/vllm-project/vllm/issues/35769) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;quantization |
| 子分类 |  |
| Operator 关键词 | quantization |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]:  mi325_1: Quantized Models Test

### Issue 正文摘录

### Name of failing test `pytest -s -v models/quantization/test_gpt_oss.py::test_gpt_oss_attention_quantization` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There was a regression in this TG. ### 📝 History of failing test https://buildkite.com/vllm/amd-ci/builds/5661/steps/canvas?sid=019cad58-e61d-4bf9-8028-1a6a6a7ac897&tab=output ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi325_1: Quantized Models Test ci-failure ### Name of failing test `pytest -s -v models/quantization/test_gpt_oss.py::test_gpt_oss_attention_quantization` ### Basic information - [ ] Flaky test - [x] Can
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [CI Failure]: mi325_1: Quantized Models Test ci-failure ### Name of failing test `pytest -s -v models/quantization/test_gpt_oss.py::test_gpt_oss_attention_quantization` ### Basic information - [ ] Flaky test - [x] Can r...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: mi325_1: Quantized Models Test ci-failure ### Name of failing test `pytest -s -v models/quantization/test_gpt_oss.py::test_gpt_oss_attention_quantization` ### Basic information - [ ] Flaky test - [x] Can r...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: tention_quantization` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There was a regression in this TG....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [CI Failure]: mi325_1: Quantized Models Test ci-failure ### Name of failing test `pytest -s -v models/quantization/test_gpt_oss.py::test_gpt_oss_attention_quantization` ### Basic information - [ ] Flaky test - [x] Can r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
