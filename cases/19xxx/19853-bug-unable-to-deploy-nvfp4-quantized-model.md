# vllm-project/vllm#19853: [Bug]: Unable to deploy NVFP4 quantized model

| 字段 | 值 |
| --- | --- |
| Issue | [#19853](https://github.com/vllm-project/vllm/issues/19853) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unable to deploy NVFP4 quantized model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am trying to deploy an NVFP4 quantized model as newly supported in 0.9.1. I copied the minimal setup from #18312: ```python import torch from vllm import LLM, SamplingParams prompts = [ "The Swiss Alps are", "Brad Marchand is", "The Toronto Maple Leafs are" ] # Create a sampling params object for greedy sampling sampling_params = SamplingParams(temperature=0.80, top_p=0.95, max_tokens=40, min_tokens=10) llm = LLM("nm-testing/TinyLlama-1.1B-Chat-v1.0-NVFP4A4") ``` This fails with the following output: It looks like the quantization config is slightly different from what vllm expects. In `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors:CompressedTensorsConfig._get_scheme_from_parts`, the quant type check `_is_fp4a4_nvfp4` fails due to the quantization strategy spec: ```python weight_quant = QuantizationArgs( num_bits=4, type='float', symmetric=True, group_size=16, strategy='group', # <--- should be 'tensor_group' block_structure=None, dynamic=False, actorder=None, observer='minmax', observer_kwargs={}, ) input_quant = QuantizationArgs( num_bits=4, type='float', symmetric=True, group_size=16, strategy...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ly supported in 0.9.1. I copied the minimal setup from #18312: ```python import torch from vllm import LLM, SamplingParams prompts = [ "The Swiss Alps are", "Brad Marchand is", "The Toronto Maple Leafs are" ] # Create a...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: Unable to deploy NVFP4 quantized model bug ### Your current environment ### 🐛 Describe the bug I am trying to deploy an NVFP4 quantized model as newly supported in 0.9.1. I copied the minimal setup from #18312: `...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Unable to deploy NVFP4 quantized model bug ### Your current environment ### 🐛 Describe the bug I am trying to deploy an NVFP4 quantized model as newly supported in 0.9.1. I copied the minimal setup from #18312: `...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: t LLM, SamplingParams prompts = [ "The Swiss Alps are", "Brad Marchand is", "The Toronto Maple Leafs are" ] # Create a sampling params object for greedy sampling sampling_params = SamplingParams(temperature=0.80, top_p=...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: group_size=16, strategy='group', # <--- should be 'tensor_group' block_structure=None, dynamic=False, actorder=None, observer='minmax', observer_kwargs={}, ) input_quant = QuantizationArgs( num_bits=4, type='float', sym...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
