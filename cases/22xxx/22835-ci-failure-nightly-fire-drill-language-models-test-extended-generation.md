# vllm-project/vllm#22835: [CI Failure][NIGHTLY FIRE DRILL]: Language Models Test (Extended Generation)

| 字段 | 值 |
| --- | --- |
| Issue | [#22835](https://github.com/vllm-project/vllm/issues/22835) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure][NIGHTLY FIRE DRILL]: Language Models Test (Extended Generation)

### Issue 正文摘录

### Name of failing test models/language/generation/test_common.py::test_models[False-5-32-bigcode/tiny_starcoder_py] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test logprob mismatch for starcoder ### 📝 History of failing test https://buildkite.com/vllm/ci/builds/26788#0198a196-b390-4f59-978d-0681f3f8b7c7 ### CC List. _No response_

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: de/tiny_starcoder_py] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test logprob mismatch for starcoder ###...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure][NIGHTLY FIRE DRILL]: Language Models Test (Extended Generation) ci-failure ### Name of failing test models/language/generation/test_common.py::test_models[False-5-32-bigcode/tiny_starcoder_py] ### Basic inf
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [CI Failure][NIGHTLY FIRE DRILL]: Language Models Test (Extended Generation) ci-failure ### Name of failing test models/language/generation/test_common.py::test_models[False-5-32-bigcode/tiny_starcoder_py] ### Basic inf...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: (e.g. bug in `transformers`) ### 🧪 Describe the failing test logprob mismatch for starcoder ### 📝 History of failing test https://buildkite.com/vllm/ci/builds/26788#0198a196-b390-4f59-978d-0681f3f8b7c7 ### CC List. _No...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: f failing test models/language/generation/test_common.py::test_models[False-5-32-bigcode/tiny_starcoder_py] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
