# vllm-project/vllm#31165: [CI Failure]: Entrypoints

| 字段 | 值 |
| --- | --- |
| Issue | [#31165](https://github.com/vllm-project/vllm/issues/31165) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Entrypoints

### Issue 正文摘录

### Name of failing test `entrypoints/openai/test_audio.py::test_chat_streaming_input_audio` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test [2025-12-22T16:15:39Z] FAILED entrypoints/openai/test_audio.py::test_chat_streaming_input_audio[https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/mary_had_lamb.ogg-fixie-ai/ultravox-v0_5-llama-3_2-1b] - AssertionError: assert 'This audio a... snippet from' == 'This audio a...short excerpt' -- ### 📝 History of failing test seems new ### CC List. _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ints/openai/test_audio.py::test_chat_streaming_input_audio` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: treaming_input_audio` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test [2025-12-22T16:15:39Z] FAILED entr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [CI Failure]: Entrypoints ci-failure ### Name of failing test `entrypoints/openai/test_audio.py::test_chat_streaming_input_audio` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by exter
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: Entrypoints ci-failure ### Name of failing test `entrypoints/openai/test_audio.py::test_chat_streaming_input_audio` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by extern...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
