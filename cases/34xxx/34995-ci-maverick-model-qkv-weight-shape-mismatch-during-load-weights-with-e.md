# vllm-project/vllm#34995: [CI] Maverick model QKV weight shape mismatch during load_weights with expert parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#34995](https://github.com/vllm-project/vllm/issues/34995) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI] Maverick model QKV weight shape mismatch during load_weights with expert parallelism

### Issue 正文摘录

## Name of failing test - `models/multimodal/generation/test_maverick.py::test_dummy_maverick[2-True-False-meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8-4-4-2]` - `models/multimodal/generation/test_maverick.py::test_dummy_maverick[2-True-True-meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8-4-4-2]` ## Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries **Affected jobs:** Distributed Model Tests (2 GPUs) **Category:** test ## Describe the failing test When loading Maverick (mllama4) models with tensor parallelism and expert parallelism enabled, the QKV weight loader fails with a shape assertion error in parameter.py:200. The loaded weight shape does not match the expected param_data shape during load_qkv_weight. ``` AssertionError: assert param_data.shape == loaded_weight.shape in parameter.py load_qkv_weight during Maverick model weight loading with expert parallelism AssertionError: param_data.shape == loaded_weight.shape (QKV weight shape mismatch during load_qkv_weight in parameter.py:200) AssertionError: assert param_data.shape == loaded_weight.shape AssertionError: param_data.shape == loaded_weight.shape failed during load_qk...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [CI] Maverick model QKV weight shape mismatch during load_weights with expert parallelism ci-failure ## Name of failing test - `models/multimodal/generation/test_maverick.py::test_dummy_maverick[2-True-False-meta-llama/...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [CI] Maverick model QKV weight shape mismatch during load_weights with expert parallelism ci-failure ## Name of failing test - `models/multimodal/generation/test_maverick.py::test_dummy_maverick[2-True-False-meta-llama/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI] Maverick model QKV weight shape mismatch during load_weights with expert parallelism ci-failure ## Name of failing test - `models/multimodal/generation/test_maverick.py::test_dummy_maverick[2-True-False-meta-llama/L
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ummy_maverick[2-True-False-meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8-4-4-2]` - `models/multimodal/generation/test_maverick.py::test_dummy_maverick[2-True-True-meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8-4-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [CI] Maverick model QKV weight shape mismatch during load_weights with expert parallelism ci-failure ## Name of failing test - `models/multimodal/generation/test_maverick.py::test_dummy_maverick[2-True-False-meta-llama/...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
