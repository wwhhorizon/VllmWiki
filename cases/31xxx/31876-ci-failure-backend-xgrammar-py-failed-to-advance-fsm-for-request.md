# vllm-project/vllm#31876: [CI Failure]: backend_xgrammar.py: Failed to advance FSM for request

| 字段 | 值 |
| --- | --- |
| Issue | [#31876](https://github.com/vllm-project/vllm/issues/31876) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: backend_xgrammar.py: Failed to advance FSM for request

### Issue 正文摘录

### Name of failing test v1/e2e/test_async_scheduling.py::test_with_spec_decoding ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Test failing with error: [backend_xgrammar.py:180] Failed to advance FSM for request 71-9f92587d for tokens 41551. Please file an issue. Not relevant with the corresponding commit (includes only error message). ### 📝 History of failing test Only observed one build with this failure: https://buildkite.com/vllm/ci/builds/45822/steps/canvas?sid=019b9677-1767-49bb-9444-f848eb8769d9 ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: backend_xgrammar.py: Failed to advance FSM for request ci-failure ### Name of failing test v1/e2e/test_async_scheduling.py::test_with_spec_decoding ### Basic information - [x] Flaky test - [ ] Can reprodu
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [CI Failure]: backend_xgrammar.py: Failed to advance FSM for request ci-failure ### Name of failing test v1/e2e/test_async_scheduling.py::test_with_spec_decoding ### Basic information - [x] Flaky test - [ ] Can reproduc...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: st_with_spec_decoding ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Test failing with error: [backend_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [CI Failure]: backend_xgrammar.py: Failed to advance FSM for request ci-failure ### Name of failing test v1/e2e/test_async_scheduling.py::test_with_spec_decoding ### Basic information - [x] Flaky test - [ ] Can reproduc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: t v1/e2e/test_async_scheduling.py::test_with_spec_decoding ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
