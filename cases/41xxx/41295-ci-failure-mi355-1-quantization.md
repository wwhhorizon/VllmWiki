# vllm-project/vllm#41295: [CI Failure]:  mi355_1: Quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#41295](https://github.com/vllm-project/vllm/issues/41295) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;quantization |
| 子分类 | runtime_err |
| Operator 关键词 | quantization |
| 症状 | build_error |
| 根因提示 | dtype |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]:  mi355_1: Quantization

### Issue 正文摘录

### Name of failing test `VLLM_TEST_FORCE_LOAD_FORMAT=auto pytest -v -s quantization/ --ignore quantization/test_blackwell_moe.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ```log FAILED quantization/test_cutlass_w4a16.py::test_machete_kernel_selected[fp16-gptq-g128] FAILED quantization/test_cutlass_w4a16.py::test_machete_kernel_selected[bf16-gptq-g128] FAILED quantization/test_cutlass_w4a16.py::test_machete_kernel_selected[fp16-awq-g128] FAILED quantization/test_cutlass_w4a16.py::test_machete_kernel_selected[fp16-channelwise] FAILED quantization/test_cutlass_w4a16.py::test_machete_rejects_invalid_config[partitioned-g_idx] FAILED quantization/test_cutlass_w4a16.py::test_machete_rejects_invalid_config[unsupported-quant-type] FAILED quantization/test_cutlass_w4a16.py::test_machete_rejects_invalid_config[unsupported-group-size] FAILED quantization/test_cutlass_w4a16.py::test_w4a16_machete_e2e[nm-testing/tinyllama-oneshot-w4a16-channel-v2] FAILED quantization/test_cutlass_w4a16.py::test_w4a16_machete_e2e[nm-testing/TinyLlama-1.1B-Chat-v1.0-W4A16-G128-Asym-Updated-Ac...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: [CI Failure]: mi355_1: Quantization ci-failure ### Name of failing test `VLLM_TEST_FORCE_LOAD_FORMAT=auto pytest -v -s quantization/ --ignore quantization/test_blackwell_moe.py` ### Basic information - [ ] Flaky test -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: Quantization ci-failure ### Name of failing test `VLLM_TEST_FORCE_LOAD_FORMAT=auto pytest -v -s quantization/ --ignore quantization/test_blackwell_moe.py` ### Basic information - [ ] Flaky test - [x] Can reproduce local...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: est_blackwell_moe.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ```log FAILED quantization/test_cu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [CI Failure]: mi355_1: Quantization ci-failure ### Name of failing test `VLLM_TEST_FORCE_LOAD_FORMAT=auto pytest -v -s quantization/ --ignore quantization/test_blackwell_moe.py` ### Basic information - [ ] Flaky test -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi355_1: Quantization ci-failure ### Name of failing test `VLLM_TEST_FORCE_LOAD_FORMAT=auto pytest -v -s quantization/ --ignore quantization/test_blackwell_moe.py` ### Basic information - [ ] Flaky test

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
