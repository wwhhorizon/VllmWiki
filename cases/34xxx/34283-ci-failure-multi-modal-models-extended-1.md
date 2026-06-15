# vllm-project/vllm#34283: [CI Failure]: Multi Modal Models (Extended) 1

| 字段 | 值 |
| --- | --- |
| Issue | [#34283](https://github.com/vllm-project/vllm/issues/34283) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Multi Modal Models (Extended) 1

### Issue 正文摘录

### Name of failing test models/multimodal/generation/test_voxtral.py::test_online_serving ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test The models/multimodal/generation/test_voxtral.py::test_online_serving failed on the Feb 10th, 2026 CI run. I can reproduce it locally. ### 📝 History of failing test First started failing Feb 10, 2026 - https://buildkite.com/vllm/ci/builds/50888#019c47d9-4992-429b-bf84-420d9268e792 ### CC List. _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: Multi Modal Models (Extended) 1 ci-failure ### Name of failing test models/multimodal/generation/test_voxtral.py::test_online_serving ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Multi Modal Models (Extended) 1 ci-failure ### Name of failing test models/multimodal/generation/test_voxtral.py::test_online_serving ### Basic information - [ ] Flaky test - [x] Can reproduce locally -
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: :test_online_serving ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test The models/multimodal/generation/te...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Failure]: Multi Modal Models (Extended) 1 ci-failure ### Name of failing test models/multimodal/generation/test_voxtral.py::test_online_serving ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Ca...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
