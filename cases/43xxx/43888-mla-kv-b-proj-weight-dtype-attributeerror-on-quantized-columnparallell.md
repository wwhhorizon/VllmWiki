# vllm-project/vllm#43888: MLA: kv_b_proj.weight.dtype AttributeError on quantized ColumnParallelLinear in chunked prefill

| 字段 | 值 |
| --- | --- |
| Issue | [#43888](https://github.com/vllm-project/vllm/issues/43888) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> MLA: kv_b_proj.weight.dtype AttributeError on quantized ColumnParallelLinear in chunked prefill

### Issue 正文摘录

## Description When using a quantized (AWQ/GPTQ/compressed-tensors) model with MLA attention, vLLM crashes with an `AttributeError` during chunked prefill because `kv_b_proj` is a `ColumnParallelLinear` that lacks a `.weight` attribute after quantization. ## Error ``` AttributeError: 'ColumnParallelLinear' object has no attribute 'weight' ``` at `vllm/model_executor/layers/attention/mla_attention.py:2094` in `_compute_prefill_context`: ```python kv_c_normed = kv_c_normed.to(self.kv_b_proj.weight.dtype) ``` ## Root Cause Lines 2084-2087 already correctly handle quantized layers: ```python _kv_b_proj_w_dtype = ( self.kv_b_proj.weight.dtype if hasattr(self.kv_b_proj, "weight") else self.kv_b_proj.params_dtype ) ``` But line 2094 ignores `_kv_b_proj_w_dtype` and directly accesses `self.kv_b_proj.weight.dtype` without the `hasattr` guard. ## Fix On line 2094, replace: ```python kv_c_normed = kv_c_normed.to(self.kv_b_proj.weight.dtype) ``` with: ```python kv_c_normed = kv_c_normed.to(_kv_b_proj_w_dtype) ``` The variable `_kv_b_proj_w_dtype` is already computed with the correct `hasattr` guard immediately above. ## Impact vLLM EngineCore crashes with a fatal error, forcing a full restart...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: iately above. ## Impact vLLM EngineCore crashes with a fatal error, forcing a full restart (service enters crash loop under load). All inflight requests fail with HTTP 500. ## Environment - vLLM version: v0.21.1rc1.dev3...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: MLA: kv_b_proj.weight.dtype AttributeError on quantized ColumnParallelLinear in chunked prefill ## Description When using a quantized (AWQ/GPTQ/compressed-tensors) model with MLA attention, vLLM crashes with an `Attribu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: GLM-4.7-Flash-AWQ-4bit (quantized with compressed-tensors) - GPU: NVIDIA RTX 3090 (CUDA 12.9) - Quantization: compressed-tensors (AWQ group_size=32, num_bits=4) - CUDA graphs: enabled - MLA: enabled (model uses Multi-he...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: weight.dtype AttributeError on quantized ColumnParallelLinear in chunked prefill ## Description When using a quantized (AWQ/GPTQ/compressed-tensors) model with MLA attention, vLLM crashes with an `AttributeError` during...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: elf.kv_b_proj.weight.dtype if hasattr(self.kv_b_proj, "weight") else self.kv_b_proj.params_dtype ) ``` But line 2094 ignores `_kv_b_proj_w_dtype` and directly accesses `self.kv_b_proj.weight.dtype` without the `hasattr`...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
