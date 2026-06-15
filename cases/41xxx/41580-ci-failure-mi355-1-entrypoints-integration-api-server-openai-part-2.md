# vllm-project/vllm#41580: [CI Failure]:  mi355_1: Entrypoints Integration (API Server openai - Part 2)

| 字段 | 值 |
| --- | --- |
| Issue | [#41580](https://github.com/vllm-project/vllm/issues/41580) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi355_1: Entrypoints Integration (API Server openai - Part 2)

### Issue 正文摘录

### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi355_1-entrypoints-integration-api-server-openai---part-2 && export VLLM_ALLOW_DEPRECATED_BEAM_SEARCH=1 && cd /vllm-workspace/tests && export VLLM_WORKER_MULTIPROC_METHOD=spawn && pytest -v -s entrypoints/openai/completion --ignore=entrypoints/openai/completion/test_tensorizer_entrypoint.py && pytest -v -s entrypoints/openai/speech_to_text/ && pytest -v -s entrypoints/test_chat_utils.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED entrypoints/openai/completion/test_shutdown.py::test_abort_timeout_exits_quickly[0.0] FAILED entrypoints/openai/completion/test_shutdown.py::test_abort_timeout_exits_quickly[2.0] ``` ### 📝 History of failing test - Current streak start: 2026-04-25 - First failure in 60d window: 2026-04-21 - Last successful nightly: 2026-04-24 - Break frequency (60d, pass↔fail flips): 3 - Latest nightly date: 2026-05-03 - Latest build(s): [amd-ci #8177](https://buildkite.com/vllm/amd-ci/builds/8177) - Latest hardware status: `mi355_1`=fail

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: I Server openai - Part 2) ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi355_1-entrypoints-integration-api-server-openai---part-2 && export VLLM_ALLOW_DEPRECATED_BEAM_SE...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi355_1: Entrypoints Integration (API Server openai - Part 2) ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi355_1-entrypoints-integration-api-server-opena
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: s/test_chat_utils.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED entrypoints/openai/comp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ch_to_text/ && pytest -v -s entrypoints/test_chat_utils.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Integration (API Server openai - Part 2) ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi355_1-entrypoints-integration-api-server-openai---part-2 && export VLLM_ALLOW_DEP...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
