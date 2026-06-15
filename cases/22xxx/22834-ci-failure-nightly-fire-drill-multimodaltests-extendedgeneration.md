# vllm-project/vllm#22834: [CI Failure][NIGHTLY FIRE DRILL]: MultiModalTests - ExtendedGeneration

| 字段 | 值 |
| --- | --- |
| Issue | [#22834](https://github.com/vllm-project/vllm/issues/22834) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure][NIGHTLY FIRE DRILL]: MultiModalTests - ExtendedGeneration

### Issue 正文摘录

### Name of failing test `models/multimodal/generation/test_pixtral.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Potential fix - [[Bugfix] Fix `PixtralHFImagePixelInputs` dynamic shape check by Isotr0py · Pull Request #22827 · vllm-project/vllm](https://github.com/vllm-project/vllm/pull/22827) ### 📝 History of failing test Failing: https://buildkite.com/vllm/ci/builds/26788#0198a196-b390-4f59-978d-0681f3f8b7c7 ### CC List. cc @Isotr0py

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [CI Failure][NIGHTLY FIRE DRILL]: MultiModalTests - ExtendedGeneration ci-failure ### Name of failing test `models/multimodal/generation/test_pixtral.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locall...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure][NIGHTLY FIRE DRILL]: MultiModalTests - ExtendedGeneration ci-failure ### Name of failing test `models/multimodal/generation/test_pixtral.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce local
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: tion/test_pixtral.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Potential fix - [[Bugfix] Fix `Pix...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ] Fix `PixtralHFImagePixelInputs` dynamic shape check by Isotr0py · Pull Request #22827 · vllm-project/vllm](https://github.com/vllm-project/vllm/pull/22827) ### 📝 History of failing test Failing: https://buildkite.com/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure][NIGHTLY FIRE DRILL]: MultiModalTests - ExtendedGeneration ci-failure ### Name of failing test `models/multimodal/generation/test_pixtral.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locall...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
