# vllm-project/vllm#35134: [CI Failure]: Fusion E2E Quick (H100) `test_tp1_fp8_fusions`

| 字段 | 值 |
| --- | --- |
| Issue | [#35134](https://github.com/vllm-project/vllm/issues/35134) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;ci_build;quantization |
| 子分类 |  |
| Operator 关键词 | fp8 |
| 症状 | build_error |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: Fusion E2E Quick (H100) `test_tp1_fp8_fusions`

### Issue 正文摘录

### Name of failing test `tests/compile/fusions_e2e/test_tp1_quant.py::test_tp1_fp8_fusions[inductor_partition-+quant_fp8,-rms_norm-6-TRITON_ATTN-Qwen/Qwen3-30B-A3B-FP8- -model_kwargs3- -True]` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/ci/builds/52746/steps/canvas?jid=019c8b3b-0484-4e0c-8817-d06478d2e786&tab=output#019c8b3b-0484-4e0c-8817-d06478d2e786/L565 ``` FAILED tests/compile/fusions_e2e/test_tp1_quant.py::test_tp1_fp8_fusions[inductor_partition-+quant_fp8,-rms_norm-6-TRITON_ATTN-Qwen/Qwen3-30B-A3B-FP8- -model_kwargs3- -True] - AssertionError: rms_quant_fusion expected: [6], found: [0] assert [0] == [6] At index 0 diff: 0 != 6 Full diff: [ - 6, ? ^ + 0, ? ^ ] ``` ### 📝 History of failing test Seems to have started today ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: Fusion E2E Quick (H100) `test_tp1_fp8_fusions` ci-failure ### Name of failing test `tests/compile/fusions_e2e/test_tp1_quant.py::test_tp1_fp8_fusions[inductor_partition-+quant_fp8,-rms_norm-6-TRITON_ATTN-Qw
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [CI Failure]: Fusion E2E Quick (H100) `test_tp1_fp8_fusions` ci-failure ### Name of failing test `tests/compile/fusions_e2e/test_tp1_quant.py::test_tp1_fp8_fusions[inductor_partition-+quant_fp8,-rms_norm-6-TRITON_ATTN-Q...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: st_tp1_fp8_fusions[inductor_partition-+quant_fp8,-rms_norm-6-TRITON_ATTN-Qwen/Qwen3-30B-A3B-FP8- -model_kwargs3- -True]` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external librar...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: quant.py::test_tp1_fp8_fusions[inductor_partition-+quant_fp8,-rms_norm-6-TRITON_ATTN-Qwen/Qwen3-30B-A3B-FP8- -model_kwargs3- -True]` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by ext...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: odel_kwargs3- -True]` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/ci/buil...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
