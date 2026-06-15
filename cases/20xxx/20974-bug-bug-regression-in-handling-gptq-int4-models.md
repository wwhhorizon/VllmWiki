# vllm-project/vllm#20974: [Bug]: Bug/Regression in handling GPTQ-Int4 models

| 字段 | 值 |
| --- | --- |
| Issue | [#20974](https://github.com/vllm-project/vllm/issues/20974) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Bug/Regression in handling GPTQ-Int4 models

### Issue 正文摘录

### Your current environment - ### 🐛 Describe the bug Models such as Qwen/Qwen3-30B-A3B-GPTQ-Int4 ran fine with the vllm version as of Jun 27, 2025 (commit ID cd766a445a6c18945609a5bdafff98d0ce3dcd00) However, on the 0.9.2 release (as well as main), I get the following error with ALL GPTQ-Int4 models (tested with Qwen3-30B-A3B, Qwen3-235B-A22B, tencent/Hunyuan-A13B-Instruct-GPTQ-Int4: Local build using: ``` VLLM_USE_PRECOMPILED=1 pip install --editable . ``` Cmdline: ``` vllm serve "Qwen/Qwen3-30B-A3B-GPTQ-Int4" --host 0.0.0.0 --port 8000 --download-dir /workspace --max-model-len 20000 ``` ``` Error: File "/usr/local/lib/python3.11/dist-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl return self._call_impl(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.11/dist-packages/torch/nn/modules/module.py", line 1762, in _call_impl return forward_call(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/workspace/vllm_source2/vllm/model_executor/models/qwen3_moe.py", line 527, in forward hidden_states = self.model(input_ids, positions, intermediate_tensors, ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/workspace/vllm_so...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: bug Models such as Qwen/Qwen3-30B-A3B-GPTQ-Int4 ran fine with the vllm version as of Jun 27, 2025 (commit ID cd766a445a6c18945609a5bdafff98d0ce3dcd00) However, on the 0.9.2 release (as well as main), I get the following...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Bug/Regression in handling GPTQ-Int4 models bug ### Your current environment - ### 🐛 Describe the bug Models such as Qwen/Qwen3-30B-A3B-GPTQ-Int4 ran fine with the vllm version as of Jun 27, 2025 (commit ID cd766...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Bug/Regression in handling GPTQ-Int4 models bug ### Your current environment - ### 🐛 Describe the bug Models such as Qwen/Qwen3-30B-A3B-GPTQ-Int4 ran fine with the vllm version as of Jun 27, 2025 (commit ID cd766...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: Bug/Regression in handling GPTQ-Int4 models bug ### Your current environment - ### 🐛 Describe the bug Models such as Qwen/Qwen3-30B-A3B-GPTQ-Int4 ran fine with the vllm version as of Jun 27, 2025 (commit ID cd766...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: space/vllm_source2/vllm/model_executor/layers/quantization/kernels/mixed_precision/machete.py", line 129, in apply_weights output = ops.machete_mm(a=x_2d, File "/workspace/vllm_source2/vllm/_custom_ops.py", line 1099, i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
