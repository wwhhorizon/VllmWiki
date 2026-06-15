# vllm-project/vllm#31507: [CI Failure]:  mi325_1: Model Executor Test

| 字段 | 值 |
| --- | --- |
| Issue | [#31507](https://github.com/vllm-project/vllm/issues/31507) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi325_1: Model Executor Test

### Issue 正文摘录

### Name of failing test `pytest -v -s model_executor && pytest -v -s entrypoints/openai/test_tensorizer_entrypoint.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Short summary: ```log 2025-12-29 12:58:28 CST =========================== short test summary info ============================ 2025-12-29 12:58:28 CST FAILED model_executor/model_loader/test_sharded_state_loader.py::test_sharded_state_loader[1-False] 2025-12-29 12:58:28 CST ======= 1 failed, 69 passed, 8 skipped, 4 warnings in 1088.97s (0:18:08) ======= ``` Full error log: ### 📝 History of failing test https://buildkite.com/vllm/amd-ci/builds/2223

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi325_1: Model Executor Test ci-failure ### Name of failing test `pytest -v -s model_executor && pytest -v -s entrypoints/openai/test_tensorizer_entrypoint.py` ### Basic information - [ ] Flaky test - [x
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [CI Failure]: mi325_1: Model Executor Test ci-failure ### Name of failing test `pytest -v -s model_executor && pytest -v -s entrypoints/openai/test_tensorizer_entrypoint.py` ### Basic information - [ ] Flaky test - [x]...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: orizer_entrypoint.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Short summary: ```log 2025-12-29 1...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: model_loader/test_sharded_state_loader.py::test_sharded_state_loader[1-False] 2025-12-29 12:58:28 CST ======= 1 failed, 69 passed, 8 skipped, 4 warnings in 1088.97s (0:18:08) ======= ``` Full error log: ### 📝 History of...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: mi325_1: Model Executor Test ci-failure ### Name of failing test `pytest -v -s model_executor && pytest -v -s entrypoints/openai/test_tensorizer_entrypoint.py` ### Basic information - [ ] Flaky test - [x]...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
