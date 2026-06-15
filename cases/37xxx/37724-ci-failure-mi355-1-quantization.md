# vllm-project/vllm#37724: [CI Failure]:  mi355_1: Quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#37724](https://github.com/vllm-project/vllm/issues/37724) |
| 状态 | closed |
| 标签 | rocm;ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;quantization |
| 子分类 | debug |
| Operator 关键词 | fp8;quantization |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]:  mi355_1: Quantization

### Issue 正文摘录

### Name of failing test `pytest -v -s tests/quantization/ --ignore tests/quantization/test_blackwell_moe.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There are some failures in this TG: ```log FAILED quantization/test_fp8.py::test_online_quant_peak_mem FAILED quantization/test_mixed_precision.py::test_mixed_precision_model_accuracies[amd/Qwen3-8B-WMXFP4FP8-AMXFP4FP8-AMP-KVFP8-accuracy_numbers0] FAILED quantization/test_mixed_precision.py::test_mixed_precision_model_accuracies[amd/Llama-2-70b-chat-hf-FP8-MLPerf-fp8_attn_quark_format-accuracy_numbers1] FAILED quantization/test_ptpc_fp8.py::test_ptpc_fp8_rocm[auto-bfloat16] FAILED quantization/test_ptpc_fp8.py::test_ptpc_fp8_rocm[fp8-bfloat16] FAILED quantization/test_quark.py::test_ocp_mx_wikitext_correctness[1-config0] FAILED quantization/test_quark.py::test_ocp_mx_wikitext_correctness[1-config2] FAILED quantization/test_torchao.py::test_online_quant_config_dict_json FAILED quantization/test_torchao.py::test_online_quant_config_file ``` Of these failures, some are unique to MI355. These failures need to be tria...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [CI Failure]: mi355_1: Quantization rocm;ci-failure ### Name of failing test `pytest -v -s tests/quantization/ --ignore tests/quantization/test_blackwell_moe.py` ### Basic information - [ ] Flaky test - [x] Can reproduc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: ization/ --ignore tests/quantization/test_blackwell_moe.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: est_blackwell_moe.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There are some failures in this TG...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi355_1: Quantization rocm;ci-failure ### Name of failing test `pytest -v -s tests/quantization/ --ignore tests/quantization/test_blackwell_moe.py` ### Basic information - [ ] Flaky test - [x] Can reprod
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [CI Failure]: mi355_1: Quantization rocm;ci-failure ### Name of failing test `pytest -v -s tests/quantization/ --ignore tests/quantization/test_blackwell_moe.py` ### Basic information - [ ] Flaky test - [x] Can reproduc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
