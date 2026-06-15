# vllm-project/vllm#27576: [CI Failure]: Entrypoints Integration Test (API Server) flake in entrypoints/openai/test_transcription_validation.py::test_basic_audio_gemma

| 字段 | 值 |
| --- | --- |
| Issue | [#27576](https://github.com/vllm-project/vllm/issues/27576) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Entrypoints Integration Test (API Server) flake in entrypoints/openai/test_transcription_validation.py::test_basic_audio_gemma

### Issue 正文摘录

### Name of failing test entrypoints/openai/test_transcription_validation.py::test_basic_audio_gemma ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test On an unrelated PR, I caught a flake of this test with: `FAILED entrypoints/openai/test_transcription_validation.py::test_basic_audio_gemma - RuntimeError: Server failed to start in time.` It looks like the server timed out with the default 240s timeout while attempting to load this model. The logs indicate forward progress was being made, albeit slower than expected. Perhaps this test just needs a longer `max_wait_seconds` to be passed in as an additional arg to the `RemoteOpenAIServer` initializer? ### 📝 History of failing test I cannot see the Buildkit Test Suites feature - perhaps it is not public? But, here's a link to one place this flaked on a PR I had open - https://buildkite.com/vllm/ci/builds/36258/steps/canvas?jid=019a1a38-3f40-423e-9f36-7248c8d7b84e#019a1a38-3f40-423e-9f36-7248c8d7b84e/7-13138 This test was added in #23735 ### CC List. cc @NickLucche as the original author of the test in question

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: Entrypoints Integration Test (API Server) flake in entrypoints/openai/test_transcription_validation.py::test_basic_audio_gemma ci-failure ### Name of failing test entrypoints/openai/test_transcription_valid
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: in entrypoints/openai/test_transcription_validation.py::test_basic_audio_gemma ci-failure ### Name of failing test entrypoints/openai/test_transcription_validation.py::test_basic_audio_gemma ### Basic information - [x]...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: est_basic_audio_gemma ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test On an unrelated PR, I caught a fla...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: in entrypoints/openai/test_transcription_validation.py::test_basic_audio_gemma ci-failure ### Name of failing test entrypoints/openai/test_transcription_validation.py::test_basic_audio_gemma ### Basic information - [x]...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: Entrypoints Integration Test (API Server) flake in entrypoints/openai/test_transcription_validation.py::test_basic_audio_gemma ci-failure ### Name of failing test entrypoints/openai/test_transcription_vali...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
