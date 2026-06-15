# vllm-project/vllm#20366: [CI Failure]: entrypoints-test: test_streaming_response

| 字段 | 值 |
| --- | --- |
| Issue | [#20366](https://github.com/vllm-project/vllm/issues/20366) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: entrypoints-test: test_streaming_response

### Issue 正文摘录

### Name of failing test entrypoints/openai/test_transcription_validation.py::test_streaming_response ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Two sporadic failing tests: entrypoints/openai/test_transcription_validation.py::test_streaming_response entrypoints/openai/test_translation_validation.py::test_streaming_response Failing with: openai.APITimeoutError: Request timed out. Example commits from main which fail: https://github.com/vllm-project/vllm/commit/c05596f1a350f3d993c467959ed02492141c2527 https://github.com/vllm-project/vllm/commit/7da296be04933cfc29031f5bd1ba7cd28f376faa There are more... ### 📝 History of failing test The first commit in main with this error is: https://github.com/vllm-project/vllm/commit/c05596f1a350f3d993c467959ed02492141c2527 However, looking at the code it seems unrelated. So maybe some other commit beforehand. My guess is around Jun 30th-July1st. ### CC List. _No response_

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: st_streaming_response ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Two sporadic failing tests: entryp...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [CI Failure]: entrypoints-test: test_streaming_response ci-failure ### Name of failing test entrypoints/openai/test_transcription_validation.py::test_streaming_response ### Basic information - [x] Flaky test - [ ] Can
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: i/test_transcription_validation.py::test_streaming_response ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ation.py::test_streaming_response Failing with: openai.APITimeoutError: Request timed out. Example commits from main which fail: https://github.com/vllm-project/vllm/commit/c05596f1a350f3d993c467959ed02492141c2527 https...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: entrypoints-test: test_streaming_response ci-failure ### Name of failing test entrypoints/openai/test_transcription_validation.py::test_streaming_response ### Basic information - [x] Flaky test - [ ] Can r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
