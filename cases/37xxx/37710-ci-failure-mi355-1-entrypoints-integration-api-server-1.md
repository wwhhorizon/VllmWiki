# vllm-project/vllm#37710: [CI Failure]:  mi355_1: Entrypoints Integration (API Server 1)

| 字段 | 值 |
| --- | --- |
| Issue | [#37710](https://github.com/vllm-project/vllm/issues/37710) |
| 状态 | closed |
| 标签 | rocm;ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi355_1: Entrypoints Integration (API Server 1)

### Issue 正文摘录

### Name of failing test `pytest -s -v tests/entrypoints/openai/speech_to_text/test_translation_validation.py::test_streaming_response[openai/whisper-small]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Whisper looks like it has some sort of accuracy issue on gfx950. ### 📝 History of failing test https://buildkite.com/vllm/amd-ci/builds/6721/steps/canvas?sid=019d09d4-711d-4fbe-9f40-6ec17a28f286&tab=output

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: penai/whisper-small]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Whisper looks like it has some sor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi355_1: Entrypoints Integration (API Server 1) rocm;ci-failure ### Name of failing test `pytest -s -v tests/entrypoints/openai/speech_to_text/test_translation_validation.py::test_streaming_response[openai
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [CI Failure]: mi355_1: Entrypoints Integration (API Server 1) rocm;ci-failure ### Name of failing test `pytest -s -v tests/entrypoints/openai/speech_to_text/test_translation_validation.py::test_streaming_response[openai...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: trypoints Integration (API Server 1) rocm;ci-failure ### Name of failing test `pytest -s -v tests/entrypoints/openai/speech_to_text/test_translation_validation.py::test_streaming_response[openai/whisper-small]` ### Basi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: lidation.py::test_streaming_response[openai/whisper-small]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
