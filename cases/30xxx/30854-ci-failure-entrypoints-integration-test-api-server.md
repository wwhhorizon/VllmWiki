# vllm-project/vllm#30854: [CI Failure]: Entrypoints Integration Test (API Server)

| 字段 | 值 |
| --- | --- |
| Issue | [#30854](https://github.com/vllm-project/vllm/issues/30854) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Entrypoints Integration Test (API Server)

### Issue 正文摘录

### Name of failing test `buildkite/ci/pr` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Examples: - https://buildkite.com/vllm/ci/builds/43856/steps/canvas?sid=019b29b8-ae56-4274-b537-809a96b3929f - https://buildkite.com/vllm/ci/builds/43856/steps/canvas?jid=019b29b8-aef0-4bff-bd60-8521aee55430 These CI errors are being triggered in PR that has absolutely nothing to do with these (https://github.com/vllm-project/vllm/pull/30738). Also, every other recent PRs on the repository seems to be suffering from the same failures. Errors from examples above: ``` [2025-12-17T01:57:49Z] entrypoints/openai/test_response_api_with_harmony.py::test_function_calling_required[openai/gpt-oss-20b] (APIServer pid=11797) ERROR 12-16 17:57:49 [serving_responses.py:370] Error in preprocessing prompt inputs -- [2025-12-17T01:57:49Z] (APIServer pid=11797) ERROR 12-16 17:57:49 [serving_responses.py:370] Traceback (most recent call last): [2025-12-17T01:57:49Z] (APIServer pid=11797) ERROR 12-16 17:57:49 [serving_responses.py:370] File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ver) ci-failure ### Name of failing test `buildkite/ci/pr` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Entrypoints Integration Test (API Server) ci-failure ### Name of failing test `buildkite/ci/pr` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g.
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: st `buildkite/ci/pr` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Examples: - https://buildkite.com/v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: :49 [serving_responses.py:370] messages, engine_prompts = self._make_request_with_harmony( [2025-12-17T01:57:49Z] (APIServer pid=11797) ERROR 12-16 17:57:49 [serving_responses.py:370] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [2...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: Entrypoints Integration Test (API Server) ci-failure ### Name of failing test `buildkite/ci/pr` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
