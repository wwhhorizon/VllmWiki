# vllm-project/vllm#43350: [CI Failure]: Multiple tests failing with assert output_size is not None

| 字段 | 值 |
| --- | --- |
| Issue | [#43350](https://github.com/vllm-project/vllm/issues/43350) |
| 状态 | open |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Multiple tests failing with assert output_size is not None

### Issue 正文摘录

### Name of failing test tests/compile/fullgraph/test_full_graph.py::test_fp8_kv_scale_compile (e.g.) ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Multiple tests fail with `assert output_size is not None`, also after retry. Failing tests include: - `tests/compile/fullgraph/test_full_graph.py::test_fp8_kv_scale_compile` (multiple models) - `v1/spec_decode/test_speculators_correctness.py::test_speculators_model` - `quantization/test_fp8.py::test_online_quantization` - Run in Distributed Torchrun + Examples (4 GPUs) ### 📝 History of failing test This is a new failure ### CC List. _No response_

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: # Name of failing test tests/compile/fullgraph/test_full_graph.py::test_fp8_kv_scale_compile (e.g.) ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `tra...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Multiple tests failing with assert output_size is not None ci-failure ### Name of failing test tests/compile/fullgraph/test_full_graph.py::test_fp8_kv_scale_compile (e.g.) ### Basic information - [ ] Flak
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: lgraph/test_full_graph.py::test_fp8_kv_scale_compile (e.g.) ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: _scale_compile (e.g.) ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Multiple tests fail with `assert o...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: t_full_graph.py::test_fp8_kv_scale_compile` (multiple models) - `v1/spec_decode/test_speculators_correctness.py::test_speculators_model` - `quantization/test_fp8.py::test_online_quantization` - Run in Distributed Torchr...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
