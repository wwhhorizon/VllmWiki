# vllm-project/vllm#22398: [CI Failure]: test_reward.py::test_prm_models - AttributeError: 'DynamicCache' object has no attribute 'get_usable_length'. Did you mean: 'get_seq_length'?

| 字段 | 值 |
| --- | --- |
| Issue | [#22398](https://github.com/vllm-project/vllm/issues/22398) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: test_reward.py::test_prm_models - AttributeError: 'DynamicCache' object has no attribute 'get_usable_length'. Did you mean: 'get_seq_length'?

### Issue 正文摘录

### Name of failing test models/language/pooling/test_reward.py::test_prm_models[True-half-Qwen/Qwen2.5-Math-PRM-7B] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test [2025-08-06T21:39:31Z] FAILED models/language/pooling/test_reward.py::test_prm_models[True-half-Qwen/Qwen2.5-Math-PRM-7B] - AttributeError: 'DynamicCache' object has no attribute 'get_usable_length'. Did you mean: 'get_seq_length'? [2025-08-06T21:39:31Z] FAILED models/language/pooling/test_reward.py::test_prm_models[False-half-Qwen/Qwen2.5-Math-PRM-7B] - AttributeError: 'DynamicCache' object has no attribute 'get_usable_length'. Did you mean: 'get_seq_length'? ### 📝 History of failing test https://buildkite.com/organizations/vllm/analytics/suites/ci-1/tests/600d233a-e9e7-8f9f-b750-17eede6e1172?branch=main&period=1day broken by #22327 ### CC List. _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: test_reward.py::test_prm_models - AttributeError: 'DynamicCache' object has no attribute 'get_usable_length'. Did you mean: 'get_seq_length'? ci-failure ### Name of failing test models/language/pooling/tes...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: test_reward.py::test_prm_models - AttributeError: 'DynamicCache' object has no attribute 'get_usable_length'. Did you mean: 'get_seq_length'? ci-failure ### Name of failing test models/language/pooling/test
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: /Qwen2.5-Math-PRM-7B] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test [2025-08-06T21:39:31Z] FAILED mode...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 39:31Z] FAILED models/language/pooling/test_reward.py::test_prm_models[False-half-Qwen/Qwen2.5-Math-PRM-7B] - AttributeError: 'DynamicCache' object has no attribute 'get_usable_length'. Did you mean: 'get_seq_length'? #...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: test_reward.py::test_prm_models - AttributeError: 'DynamicCache' object has no attribute 'get_usable_length'. Did you mean: 'get_seq_length'? ci-failure ### Name of failing test models/language/pooling/tes...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
