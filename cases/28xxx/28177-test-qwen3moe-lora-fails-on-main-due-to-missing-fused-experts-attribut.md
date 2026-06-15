# vllm-project/vllm#28177: test_qwen3moe_lora fails on main due to missing fused_experts attribute in unquantized MoE models

| 字段 | 值 |
| --- | --- |
| Issue | [#28177](https://github.com/vllm-project/vllm/issues/28177) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> test_qwen3moe_lora fails on main due to missing fused_experts attribute in unquantized MoE models

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Title:** `test_qwen3moe_lora` fails on main due to missing `fused_experts` attribute in unquantized MoE models **Description:** Running ```bash pytest tests/lora/test_qwen3moe_tp.py -k test_qwen3moe_lora ``` on the current `main` branch fails with the following error: ``` AttributeError: 'UnquantizedFusedMoEMethod' object has no attribute 'fused_experts' ``` This occurs because **non-quantized MoE models** don't have a `quant_method` or `fused_experts` attribute. The test (and possibly parts of the LoRA integration code) still assumes these attributes exist. I believe this regression was introduced by [PR #21229](https://github.com/vllm-project/vllm/pull/21229). **Steps to reproduce:** ```bash pytest tests/lora/test_qwen3moe_tp.py -k test_qwen3moe_lora ``` **Expected behavior:** The test should pass for both quantized and unquantized MoE models. **Actual behavior:** Fails with `AttributeError` due to missing `fused_experts` attribute. **Suggested fix:** Add conditional handling in the LoRA test or MoE method logic to gracefully handle unquantized models that do not define `fused_experts` or `quant_method`. ### Before submitting...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: test_qwen3moe_lora fails on main due to missing fused_experts attribute in unquantized MoE models bug ### Your current environment ### 🐛 Describe the bug **Title:** `test_qwen3moe_lora` fails on main due to missing `fuse
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: test_qwen3moe_lora fails on main due to missing fused_experts attribute in unquantized MoE models bug ### Your current environment ### 🐛 Describe the bug **Title:** `test_qwen3moe_lora` fails on main due to missing `fus...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: test_qwen3moe_lora fails on main due to missing fused_experts attribute in unquantized MoE models bug ### Your current environment ### 🐛 Describe the bug **Title:** `test_qwen3moe_lora` fails on main due to missing
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [PR #21229](https://github.com/vllm-project/vllm/pull/21229). **Steps to reproduce:** ```bash pytest tests/lora/test_qwen3moe_tp.py -k test_qwen3moe_lora ``` **Expected behavior:** The test should pass for both quantize...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: _qwen3moe_lora fails on main due to missing fused_experts attribute in unquantized MoE models bug ### Your current environment ### 🐛 Describe the bug **Title:** `test_qwen3moe_lora` fails on main due to missing `fused_e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
