# vllm-project/vllm#28468: [CI Failure]: Blackwell Fusion E2E Tests

| 字段 | 值 |
| --- | --- |
| Issue | [#28468](https://github.com/vllm-project/vllm/issues/28468) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Blackwell Fusion E2E Tests

### Issue 正文摘录

### Name of failing test `tests/compile/test_full_graph.py::test_fp8_kv_scale_compile` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ```bash FAILED tests/compile/test_full_graph.py::test_fp8_kv_scale_compile[deepseek-ai/DeepSeek-V2-Lite-0] - vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause. FAILED tests/compile/test_full_graph.py::test_fp8_kv_scale_compile[deepseek-ai/DeepSeek-V2-Lite-3] - vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause. Illegal memory access ``` ### 📝 History of failing test New failure ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Blackwell Fusion E2E Tests ci-failure ### Name of failing test `tests/compile/test_full_graph.py::test_fp8_kv_scale_compile` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ailure ### Name of failing test `tests/compile/test_full_graph.py::test_fp8_kv_scale_compile` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transform...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: fp8_kv_scale_compile` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ```bash FAILED tests/compile/test_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [CI Failure]: Blackwell Fusion E2E Tests ci-failure ### Name of failing test `tests/compile/test_full_graph.py::test_fp8_kv_scale_compile` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ests/compile/test_full_graph.py::test_fp8_kv_scale_compile` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
