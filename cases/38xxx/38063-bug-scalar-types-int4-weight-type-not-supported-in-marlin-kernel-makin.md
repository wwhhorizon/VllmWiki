# vllm-project/vllm#38063: [Bug] scalar_types.int4 weight type not supported in Marlin kernel, making W4A8-INT models undeployable

| 字段 | 值 |
| --- | --- |
| Issue | [#38063](https://github.com/vllm-project/vllm/issues/38063) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | hardware_porting;model_support;quantization |
| 子分类 | install |
| Operator 关键词 | kernel;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] scalar_types.int4 weight type not supported in Marlin kernel, making W4A8-INT models undeployable

### Issue 正文摘录

## Summary When loading a compressed_tensors W4A8-INT model with `int4` weight type (e.g., quantized with LLM Compressor), vLLM fails to deploy because `scalar_types.int4` is not included in the Marlin kernel's supported quantization types. ## Root Cause `query_marlin_supported_quant_types` in `marlin_utils.py` only returns `[scalar_types.uint4b8, scalar_types.uint8b128]` for the non-zero-point path. `scalar_types.int4` is missing, so `MarlinLinearKernel.can_implement()` returns `False` and no kernel is selected. ```python # Current (broken) res = [scalar_types.uint4b8, scalar_types.uint8b128] # Fix res = [scalar_types.uint4b8, scalar_types.uint8b128, scalar_types.int4] ``` Additionally, `process_weights_after_loading` has an assert that only allows `uint4b8` in the W4A8 path: ```python # Current (broken) assert c.weight_type == scalar_types.uint4b8 # Fix assert c.weight_type in (scalar_types.uint4b8, scalar_types.int4) ``` ## Impact Any W4A8-INT model saved with `int4` weight type (signed) cannot be loaded. This includes models quantized via LLM Compressor's `compressed_tensors` format. ## Fix See: https://github.com/yeshihai/vllm/tree/feat/marlin-w4a8-int Tested on L40 (SM89, Ad...

## 现有链接修复摘要

#38066 feat(quantization): fix W4A8-INT activation quantization and int4 support in Marlin kernel

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug] scalar_types.int4 weight type not supported in Marlin kernel, making W4A8-INT models undeployable ## Summary When loading a compressed_tensors W4A8-INT model with `int4` weight type (e.g., quantized with LLM Compr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: r_types.int4 weight type not supported in Marlin kernel, making W4A8-INT models undeployable ## Summary When loading a compressed_tensors W4A8-INT model with `int4` weight type (e.g., quantized with LLM Compressor), vLL...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ardware_porting;model_support;quantization kernel;quantization dtype;env_dependency #38066 feat(quantization): fix W4A8-INT activation quantization and int4 support in Marlin kernel Summary
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: tps://github.com/yeshihai/vllm/tree/feat/marlin-w4a8-int Tested on L40 (SM89, Ada Lovelace) with Qwen2.5-7B. development hardware_porting;model_support;quantization kernel;quantization dtype;env_dependency #38066 feat(q...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: pes.int4` is missing, so `MarlinLinearKernel.can_implement()` returns `False` and no kernel is selected. ```python # Current (broken) res = [scalar_types.uint4b8, scalar_types.uint8b128] # Fix res = [scalar_types.uint4b...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38066](https://github.com/vllm-project/vllm/pull/38066) | closes_keyword | 0.95 | feat(quantization): fix W4A8-INT activation quantization and int4 support in Marlin kernel | Fixes #38063, Fixes #38064 ## Root Causes & Changes ### 1. `compressed_tensors_w4a8_int.py` - `act_type=params_dtype` (bf16) → `act_type=torch.int8` - Add `weight_type=self.quant |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
