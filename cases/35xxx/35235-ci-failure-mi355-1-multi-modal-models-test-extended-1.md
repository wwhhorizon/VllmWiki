# vllm-project/vllm#35235: [CI Failure]:  mi355_1: Multi-Modal Models Test (Extended) 1

| 字段 | 值 |
| --- | --- |
| Issue | [#35235](https://github.com/vllm-project/vllm/issues/35235) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi355_1: Multi-Modal Models Test (Extended) 1

### Issue 正文摘录

### Name of failing test `pytest -s -v models/multimodal/generation/test_voxtral_realtime.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This test group fails here: ```log FAILED models/multimodal/generation/test_voxtral_realtime.py::test_voxtral_realtime_forward ERROR models/multimodal/generation/test_voxtral_realtime.py::test_voxtral_realtime_generator ``` ### 📝 History of failing test https://buildkite.com/vllm/amd-ci/builds/5300/steps/canvas?sid=019c8e72-d8e2-4234-8ce4-ebea2d096164&tab=output

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: mi355_1: Multi-Modal Models Test (Extended) 1 ci-failure ### Name of failing test `pytest -s -v models/multimodal/generation/test_voxtral_realtime.py` ### Basic information - [ ] Flaky test - [x] Can repro...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi355_1: Multi-Modal Models Test (Extended) 1 ci-failure ### Name of failing test `pytest -s -v models/multimodal/generation/test_voxtral_realtime.py` ### Basic information - [ ] Flaky test - [x] Can re
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: _voxtral_realtime.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This test group fails here: ```log...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: mi355_1: Multi-Modal Models Test (Extended) 1 ci-failure ### Name of failing test `pytest -s -v models/multimodal/generation/test_voxtral_realtime.py` ### Basic information - [ ] Flaky test - [x] Can repro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
