# vllm-project/vllm#40622: [CI Failure]: PyTorch Compilation Passes Unit Tests

| 字段 | 值 |
| --- | --- |
| Issue | [#40622](https://github.com/vllm-project/vllm/issues/40622) |
| 状态 | closed |
| 标签 | help wanted;torch.compile;ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: PyTorch Compilation Passes Unit Tests

### Issue 正文摘录

### Name of failing test `tests/compile/passes/test_functionalization.py::test_fix_functionalization[TestFusedAddRMSNorm-True-dtype0]` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test The fix_functionalization test is flaky, as it compares outputs. It's possible this is an actual error as it happens often. It's also possible this is due to different semantics of `RMSNorm` since the partial IR migration (`rms_norm`, not `fused_add_rms_norm`), if the test uses RMSNorm instead of the kernel call directly. ### 📝 History of failing test Last 1-3 weeks ### CC List. @zou3519

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: PyTorch Compilation Passes Unit Tests help wanted;torch.compile;ci-failure ### Name of failing test `tests/compile/passes/test_functionalization.py::test_fix_functionalization[TestFusedAddRMSNorm-True-dtype
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: RMSNorm-True-dtype0]` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test The fix_functionalization test is...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: unctionalization.py::test_fix_functionalization[TestFusedAddRMSNorm-True-dtype0]` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: est_fix_functionalization[TestFusedAddRMSNorm-True-dtype0]` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: PyTorch Compilation Passes Unit Tests help wanted;torch.compile;ci-failure ### Name of failing test `tests/compile/passes/test_functionalization.py::test_fix_functionalization[TestFusedAddRMSNorm-True-dtyp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
