# vllm-project/vllm#37704: [CI Failure]:  mi250_1: Kernels Core Operation Test

| 字段 | 值 |
| --- | --- |
| Issue | [#37704](https://github.com/vllm-project/vllm/issues/37704) |
| 状态 | closed |
| 标签 | rocm;ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;ci_build;hardware_porting |
| 子分类 | debug |
| Operator 关键词 | activation;cuda;kernel |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]:  mi250_1: Kernels Core Operation Test

### Issue 正文摘录

### Name of failing test `pytest -s -v kernels/core/test_layernorm.py::test_fused_rms_norm_quant` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test RMS norm seems to be buggy on MI250. We might need to fall back to MI325 for this. Investigation pending. Error logs: ```log FAILED kernels/core/test_layernorm.py::test_fused_rms_norm_quant[False-cuda:0-0-0.01-dtype0-False-768-4096] FAILED kernels/core/test_layernorm.py::test_fused_rms_norm_quant[False-cuda:0-0-0.01-dtype0-False-5120-4096] FAILED kernels/core/test_layernorm.py::test_fused_rms_norm_quant[False-cuda:0-0-0.01-dtype0-False-8192-4096] FAILED kernels/core/test_layernorm.py::test_fused_rms_norm_quant[False-cuda:0-0-1.0-dtype0-False-5120-4096] FAILED kernels/core/test_layernorm.py::test_fused_rms_norm_quant[False-cuda:0-0-1.0-dtype0-False-8192-4096] FAILED kernels/core/test_layernorm.py::test_fused_rms_norm_quant[False-cuda:0-0-10.0-dtype0-False-768-4096] FAILED kernels/core/test_layernorm.py::test_fused_rms_norm_quant[False-cuda:0-0-10.0-dtype0-False-5120-4096] FAILED kernels/core/test_layernorm.py::test_fused_rms_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi250_1: Kernels Core Operation Test rocm;ci-failure ### Name of failing test `pytest -s -v kernels/core/test_layernorm.py::test_fused_rms_norm_quant` ### Basic information - [ ] Flaky test - [ ] Can rep
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: test `pytest -s -v kernels/core/test_layernorm.py::test_fused_rms_norm_quant` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Desc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [CI Failure]: mi250_1: Kernels Core Operation Test rocm;ci-failure ### Name of failing test `pytest -s -v kernels/core/test_layernorm.py::test_fused_rms_norm_quant` ### Basic information - [ ] Flaky test - [ ] Can repro...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: fused_rms_norm_quant` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test RMS norm seems to be buggy on MI25...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ``log FAILED kernels/core/test_layernorm.py::test_fused_rms_norm_quant[False-cuda:0-0-0.01-dtype0-False-768-4096] FAILED kernels/core/test_layernorm.py::test_fused_rms_norm_quant[False-cuda:0-0-0.01-dtype0-False-5120-40...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
