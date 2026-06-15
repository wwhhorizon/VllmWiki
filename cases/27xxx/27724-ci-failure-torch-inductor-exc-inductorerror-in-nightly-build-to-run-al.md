# vllm-project/vllm#27724: [CI Failure]: torch._inductor.exc.InductorError in Nightly build to run all tests

| 字段 | 值 |
| --- | --- |
| Issue | [#27724](https://github.com/vllm-project/vllm/issues/27724) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: torch._inductor.exc.InductorError in Nightly build to run all tests

### Issue 正文摘录

### Name of failing test models/language/pooling/test_token_classification.py::test_bert_models[float-boltuix/NeuroBERT-NER] and more ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test torch._inductor.exc.InductorError in Nightly build to run all tests block #25524 #27329 ### 📝 History of failing test Today's test failed https://buildkite.com/vllm/ci/builds/36708/steps/canvas?sid=019a2e20-72db-4f0c-929a-45ef5a6824f0 https://buildkite.com/vllm/ci/builds/36708/steps/canvas?sid=019a2e20-72dc-4b54-b29c-69c4cf8fae73 Flaky in #27338 Yesterday's test can still be passed https://buildkite.com/vllm/ci/builds/36507/steps/canvas?sid=019a28fa-28a3-467d-8db7-163b1bc91ae1 https://buildkite.com/vllm/ci/builds/36507/steps/canvas?sid=019a28fa-28a3-4c24-8b44-d267f09477b5 #27659 can still be passed ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: torch._inductor.exc.InductorError in Nightly build to run all tests ci-failure ### Name of failing test models/language/pooling/test_token_classification.py::test_bert_models[float-boltuix/NeuroBERT-NER] an
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: r in Nightly build to run all tests ci-failure ### Name of failing test models/language/pooling/test_token_classification.py::test_bert_models[float-boltuix/NeuroBERT-NER] and more ### Basic information - [ ] Flaky test...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: uroBERT-NER] and more ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test torch._inductor.exc.InductorError...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: st torch._inductor.exc.InductorError in Nightly build to run all tests block #25524 #27329 ### 📝 History of failing test Today's test failed https://buildkite.com/vllm/ci/builds/36708/steps/canvas?sid=019a2e20-72db-4f0c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Failure]: torch._inductor.exc.InductorError in Nightly build to run all tests ci-failure ### Name of failing test models/language/pooling/test_token_classification.py::test_bert_models[float-boltuix/NeuroBERT-NER] and m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
