# vllm-project/vllm#34365: [CI Failure]:  mi325_1: Async Engine, Inputs, Utils, Worker, Config Test (CPU)

| 字段 | 值 |
| --- | --- |
| Issue | [#34365](https://github.com/vllm-project/vllm/issues/34365) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi325_1: Async Engine, Inputs, Utils, Worker, Config Test (CPU)

### Issue 正文摘录

### Name of failing test `pytest -s -v tests/config/test_config_generation.py::test_unrecognized_env` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There was a recent regression: ```log hard_fail = True def validate_environ(hard_fail: bool) -> None: for env in os.environ: if env.startswith("VLLM_") and env not in environment_variables: if hard_fail: > raise ValueError(f"Unknown vLLM environment variable detected: {env}") E ValueError: Unknown vLLM environment variable detected: VLLM_TEST_GROUP_NAME /usr/local/lib/python3.12/dist-packages/vllm/envs.py:1623: ValueError ``` There is probably a deprecated env var somewhere used in there. Should be an easy fix. ### 📝 History of failing test https://buildkite.com/vllm/amd-ci/builds/4576/steps/canvas?sid=019c4b80-1c79-43ab-a5c4-0ae5590ba305&tab=output

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi325_1: Async Engine, Inputs, Utils, Worker, Config Test (CPU) ci-failure ### Name of failing test `pytest -s -v tests/config/test_config_generation.py::test_unrecognized_env` ### Basic information - [
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [CI Failure]: mi325_1: Async Engine, Inputs, Utils, Worker, Config Test (CPU) ci-failure ### Name of failing test `pytest -s -v tests/config/test_config_generation.py::test_unrecognized_env` ### Basic information - [ ]...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: mi325_1: Async Engine, Inputs, Utils, Worker, Config Test (CPU) ci-failure ### Name of failing test `pytest -s -v tests/config/test_config_generation.py::test_unrecognized_env` ### Basic information - [ ]...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: est_unrecognized_env` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There was a recent regression: ```...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
