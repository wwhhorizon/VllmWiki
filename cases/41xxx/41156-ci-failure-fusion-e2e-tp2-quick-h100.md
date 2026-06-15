# vllm-project/vllm#41156: [CI Failure]: Fusion E2E TP2 Quick (H100)

| 字段 | 值 |
| --- | --- |
| Issue | [#41156](https://github.com/vllm-project/vllm/issues/41156) |
| 状态 | closed |
| 标签 | help wanted;torch.compile;ci-failure;needs reproduction |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Fusion E2E TP2 Quick (H100)

### Issue 正文摘录

### Name of failing test `tests/compile/fusions_e2e/test_tp2_ar_rms.py::test_tp2_ar_rms_fp8_fusions` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Consistent OOM, haven't tried to repro locally. DSV4 PR touched many files, something probably caused a new unaccounted allocation somewhere. Our memory tracking is known to be unsafe. ### 📝 History of failing test Started failing with the Deepseek V4 PR (#40860): - Full build right before: https://buildkite.com/vllm/ci/builds/63026/canvas - DSV4 commit build: https://buildkite.com/vllm/ci/builds/63030/canvas Been failing consistently on main since: - http://buildkite.com/vllm/ci/builds/63061/canvas - https://buildkite.com/vllm/ci/builds/63175/canvas - https://buildkite.com/vllm/ci/builds/63246/canvas ### CC List. cc @zou3519 @youkaichao @pavanimajety @mgoin cc @ywang96 @WoosukKwon just fyi

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: Fusion E2E TP2 Quick (H100) help wanted;torch.compile;ci-failure;needs reproduction ### Name of failing test `tests/compile/fusions_e2e/test_tp2_ar_rms.py::test_tp2_ar_rms_fp8_fusions` ### Basic informatio
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: 2_ar_rms_fp8_fusions` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Consistent OOM, haven't tried to r...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ing test `tests/compile/fusions_e2e/test_tp2_ar_rms.py::test_tp2_ar_rms_fp8_fusions` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ###...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [CI Failure]: Fusion E2E TP2 Quick (H100) help wanted;torch.compile;ci-failure;needs reproduction ### Name of failing test `tests/compile/fusions_e2e/test_tp2_ar_rms.py::test_tp2_ar_rms_fp8_fusions` ### Basic informatio...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: e.g. bug in `transformers`) ### 🧪 Describe the failing test Consistent OOM, haven't tried to repro locally. DSV4 PR touched many files, something probably caused a new unaccounted allocation somewhere. Our memory tracki...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
