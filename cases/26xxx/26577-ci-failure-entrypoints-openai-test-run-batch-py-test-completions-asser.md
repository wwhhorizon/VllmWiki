# vllm-project/vllm#26577: [CI Failure]: entrypoints/openai/test_run_batch.py::test_completions - AssertionError

| 字段 | 值 |
| --- | --- |
| Issue | [#26577](https://github.com/vllm-project/vllm/issues/26577) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: entrypoints/openai/test_run_batch.py::test_completions - AssertionError

### Issue 正文摘录

### Name of failing test entrypoints/openai/test_run_batch.py::test_completions ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` [2025-10-09T23:13:36Z] (EngineCore_DP0 pid=11264) File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/model_loader/default_loader.py", line 258, in get_all_weights [2025-10-09T23:13:36Z] (EngineCore_DP0 pid=11264) yield from self._get_weights_iterator(primary_weights) [2025-10-09T23:13:36Z] (EngineCore_DP0 pid=11264) File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/model_loader/default_loader.py", line 244, in [2025-10-09T23:13:36Z] (EngineCore_DP0 pid=11264) return ((source.prefix + name, tensor) for (name, tensor) in weights_iterator) [2025-10-09T23:13:36Z] (EngineCore_DP0 pid=11264) ^^^^^^^^^^^^^^^^ [2025-10-09T23:13:36Z] (EngineCore_DP0 pid=11264) File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/model_loader/weight_utils.py", line 625, in safetensors_weights_iterator [2025-10-09T23:13:36Z] (EngineCore_DP0 pid=11264) with safe_open(st_file, framework="pt") as f: [2025-10-09T23:13:36Z] (En...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: entrypoints/openai/test_run_batch.py::test_completions - AssertionError ci-failure ### Name of failing test entrypoints/openai/test_run_batch.py::test_completions ### Basic information - [ ] Flaky test -
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: est entrypoints/openai/test_run_batch.py::test_completions ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: .py::test_completions ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` [2025-10-09T23:13:36Z] (Engine...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: entrypoints/openai/test_run_batch.py::test_completions - AssertionError ci-failure ### Name of failing test entrypoints/openai/test_run_batch.py::test_completions ### Basic information - [ ] Flaky test - [...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
