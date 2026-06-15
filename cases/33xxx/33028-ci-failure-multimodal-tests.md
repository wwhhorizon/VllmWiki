# vllm-project/vllm#33028: [CI Failure]: MultiModal Tests

| 字段 | 值 |
| --- | --- |
| Issue | [#33028](https://github.com/vllm-project/vllm/issues/33028) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: MultiModal Tests

### Issue 正文摘录

### Name of failing test `test_intern_vit` | `test_radio` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test [2026-01-25T07:58:36Z] FAILED models/multimodal/pooling/test_intern_vit.py::test_models[half-OpenGVLab/InternViT-300M-448px] - AttributeError: 'NoneType' object has no attribute 'multimodal_config' -- [2026-01-25T07:58:36Z] FAILED models/multimodal/pooling/test_intern_vit.py::test_models[half-OpenGVLab/InternViT-6B-448px-V1-5] - AttributeError: 'NoneType' object has no attribute 'multimodal_config' [2026-01-25T07:58:36Z] FAILED models/multimodal/pooling/test_radio.py::test_radio[half-nvidia/C-RADIOv2-H] - AttributeError: 'NoneType' object has no attribute 'multimodal_config' [2026-01-25T07:58:36Z] FAILED models/multimodal/pooling/test_radio.py::test_radio[bfloat16-nvidia/C-RADIOv2-H] - AttributeError: 'NoneType' object has no attribute 'multimodal_config' ### 📝 History of failing test https://buildkite.com/vllm/ci/builds/48359#019bf3f4-da6d-400e-97da-4e2234f391fe ### CC List. cc @DarkLight1337

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [CI Failure]: MultiModal Tests ci-failure ### Name of failing test `test_intern_vit` | `test_radio` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `tra...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: MultiModal Tests ci-failure ### Name of failing test `test_intern_vit` | `test_radio` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `tr
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 25T07:58:36Z] FAILED models/multimodal/pooling/test_radio.py::test_radio[bfloat16-nvidia/C-RADIOv2-H] - AttributeError: 'NoneType' object has no attribute 'multimodal_config' ### 📝 History of failing test https://buildk...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: n_vit` | `test_radio` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test [2026-01-25T07:58:36Z] FAILED mode...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: MultiModal Tests ci-failure ### Name of failing test `test_intern_vit` | `test_radio` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `tra...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
