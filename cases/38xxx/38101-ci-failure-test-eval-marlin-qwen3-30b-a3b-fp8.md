# vllm-project/vllm#38101: [CI Failure]: Test Eval Marlin Qwen3-30B-A3B-Fp8

| 字段 | 值 |
| --- | --- |
| Issue | [#38101](https://github.com/vllm-project/vllm/issues/38101) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;gemm_linear;moe;quantization |
| 子分类 |  |
| Operator 关键词 | fp8;kernel;moe;quantization |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: Test Eval Marlin Qwen3-30B-A3B-Fp8

### Issue 正文摘录

### Name of failing test `tests/evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-30B-A3B-Fp8-CT-Channel-marlin]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test `pytest tests/evals/gsm8k/test_gsm8k_correctness.py --config-list-file=configs/moe-refactor/config-h100.txt -k "Qwen3-30B-A3B-Fp8-CT-Channel-marlin" -v -s` Fails with `'QKVParallelLinear' object has no attribute 'workspace'` in `vllm/vllm/model_executor/kernels/linear/scaled_mm/marlin.py", line 101, in apply_weights` called from `schemes/compressed_tensors_w8a8_fp8.py` because `CompressedTensorsW8A8Fp8` doesn't call `fp8_linear.process_weights_after_loading(layer)` Introduced in https://github.com/vllm-project/vllm/pull/32929 ### 📝 History of failing test https://buildkite.com/vllm/ci/builds/57706/steps/canvas?sid=019d1e6f-1784-460b-b631-fcea0f90d7ff&tab=output ### CC List. @jikunshang @robertgshaw2-redhat @mgoin @tjtanaa

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [CI Failure]: Test Eval Marlin Qwen3-30B-A3B-Fp8 ci-failure ### Name of failing test `tests/evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-30B-A3B-Fp8-CT-Channel-marlin]` ### Basic information - [ ]...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [CI Failure]: Test Eval Marlin Qwen3-30B-A3B-Fp8 ci-failure ### Name of failing test `tests/evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-30B-A3B-Fp8-CT-Channel-marlin]` ### Basic information - [ ]...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Test Eval Marlin Qwen3-30B-A3B-Fp8 ci-failure ### Name of failing test `tests/evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-30B-A3B-Fp8-CT-Channel-marlin]` ### Basic information - [
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: lin Qwen3-30B-A3B-Fp8 ci-failure ### Name of failing test `tests/evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-30B-A3B-Fp8-CT-Channel-marlin]` ### Basic information - [ ] Flaky test - [x] Can repro...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: t tests/evals/gsm8k/test_gsm8k_correctness.py --config-list-file=configs/moe-refactor/config-h100.txt -k "Qwen3-30B-A3B-Fp8-CT-Channel-marlin" -v -s` Fails with `'QKVParallelLinear' object has no attribute 'workspace'`...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
