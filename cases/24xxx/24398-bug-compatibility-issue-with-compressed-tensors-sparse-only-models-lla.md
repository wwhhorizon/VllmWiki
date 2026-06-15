# vllm-project/vllm#24398: [Bug]: Compatibility Issue with Compressed-Tensors Sparse-Only Models (Llama4 MoE)

| 字段 | 值 |
| --- | --- |
| Issue | [#24398](https://github.com/vllm-project/vllm/issues/24398) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Compatibility Issue with Compressed-Tensors Sparse-Only Models (Llama4 MoE)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The issue occurs because vLLM's compressed-tensors quantization handler assumes that all compressed-tensors models have quantization configuration. For sparse-only models: 1. `quant_config.target_scheme_map` is `None` (no quantization schemes) 2. `CompressedTensorsMoEMethod.get_moe_method()` tries to access `target_scheme_map["Linear"]` without null checking 3. The FusedMoE layer expects a quantization method but receives `None` ## Steps to Reproduce 1. Generate a sparse-only model using compressed-tensors with 2:4 sparsity: ```python from llmcompressor.modifiers import SparseGPTModifier recipe = [ SparseGPTModifier( sparsity=0.5, mask_structure="2:4", targets=["Linear"], ignore=["lm_head"], ) ] ``` 2. Try to load the model with vLLM: ```python from vllm import LLM model = LLM("path/to/sparse-only-model") ``` 3. Observe the error in `compressed_tensors_moe.py` ## Error Traceback ``` File "vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py", line 73 weight_quant = quant_config.target_scheme_map["Linear"].get("weights") TypeError: 'NoneType' object is not subscriptable ``` ## Proposed Solution The...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ressed-tensors with 2:4 sparsity: ```python from llmcompressor.modifiers import SparseGPTModifier recipe = [ SparseGPTModifier( sparsity=0.5, mask_structure="2:4", targets=["Linear"], ignore=["lm_head"], ) ] ``` 2. Try...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Compatibility Issue with Compressed-Tensors Sparse-Only Models (Llama4 MoE) bug;stale ### Your current environment ### 🐛 Describe the bug The issue occurs because vLLM's compressed-tensors quantization handler as...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: rget_scheme_map` is `None` (no quantization schemes) 2. `CompressedTensorsMoEMethod.get_moe_method()` tries to access `target_scheme_map["Linear"]` without null checking 3. The FusedMoE layer expects a quantization meth...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: : Compatibility Issue with Compressed-Tensors Sparse-Only Models (Llama4 MoE) bug;stale ### Your current environment ### 🐛 Describe the bug The issue occurs because vLLM's compressed-tensors quantization handler assumes...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: bility Issue with Compressed-Tensors Sparse-Only Models (Llama4 MoE) bug;stale ### Your current environment ### 🐛 Describe the bug The issue occurs because vLLM's compressed-tensors quantization handler assumes that all...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
