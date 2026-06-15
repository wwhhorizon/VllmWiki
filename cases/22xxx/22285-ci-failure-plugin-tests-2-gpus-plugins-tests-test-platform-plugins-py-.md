# vllm-project/vllm#22285: [CI Failure]: Plugin Tests (2 GPUs) - plugins_tests/test_platform_plugins.py::test_oot_attention_backend

| 字段 | 值 |
| --- | --- |
| Issue | [#22285](https://github.com/vllm-project/vllm/issues/22285) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Plugin Tests (2 GPUs) - plugins_tests/test_platform_plugins.py::test_oot_attention_backend

### Issue 正文摘录

### Name of failing test `plugins_tests/test_platform_plugins.py::test_oot_attention_backend` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Test: https://buildkite.com/vllm/ci/builds/26049/steps/canvas?sid=01987b1c-3586-457d-acd1-ff0fe56f532b ### 📝 History of failing test This test has been failing since this PR landed https://github.com/vllm-project/vllm/pull/22217 ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Plugin Tests (2 GPUs) - plugins_tests/test_platform_plugins.py::test_oot_attention_backend ci-failure ### Name of failing test `plugins_tests/test_platform_plugins.py::test_oot_attention_backend` ### Basic
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ts (2 GPUs) - plugins_tests/test_platform_plugins.py::test_oot_attention_backend ci-failure ### Name of failing test `plugins_tests/test_platform_plugins.py::test_oot_attention_backend` ### Basic information - [ ] Flaky...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ot_attention_backend` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Test: https://buildkite.com/vllm/c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tests/test_platform_plugins.py::test_oot_attention_backend` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: Plugin Tests (2 GPUs) - plugins_tests/test_platform_plugins.py::test_oot_attention_backend ci-failure ### Name of failing test `plugins_tests/test_platform_plugins.py::test_oot_attention_backend` ### Basic...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
