# vllm-project/vllm#37121: [Performance]:  KV cache ~7x memory overestimation for hybrid Mamba/attention models (Qwen3.5)

| 字段 | 值 |
| --- | --- |
| Issue | [#37121](https://github.com/vllm-project/vllm/issues/37121) |
| 状态 | open |
| 标签 | performance |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;moe;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cache;moe;quantization |
| 症状 |  |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]:  KV cache ~7x memory overestimation for hybrid Mamba/attention models (Qwen3.5)

### Issue 正文摘录

### Proposal to improve performance Qwen3.5 uses GatedDeltaNet for 24 of 32 layers (O(1) state per request) and full attention for 8 layers (O(n) KV per token). vLLM's KV cache profiler treats all layers uniformly, inflating both the reported token capacity and the actual memory allocation. Two issues in `vllm/v1/core/kv_cache_utils.py`: 1. **Reporting**: `get_max_concurrency _for_kv_cache_config` and `_report_kv_cache_config` use uniform multipliers across all groups, treating Mamba's constant O(1) state as if it scaled like attention's O(n) KV. 2. **Allocation**: `unify_kv_cache_spec_page_size` pads Mamba's small state (~1.1 MiB/block at bf16) up to attention's page size (~32 KiB/block at bf16), then `get_kv_cache_config_from_groups` allocates equal-sized tensors for all groups. Proposed fix (all changes in one file, additive code path): - **Reporting**: Sum per-group costs independently. Count tokens from attention groups only. - **Allocation**: Add new `elif` branch for mixed Mamba+attention with per-layer tensors at natural page sizes. Skip page size unification for these models. ### Report of performance regression Measured on Qwen3.5-4B-AWQ (NVIDIA DGX Spark, vLLM 0.17.1):...

## 现有链接修复摘要

#37124 [Bugfix] Fix KV cache overestimation for hybrid Mamba/attention model…

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: s all groups, treating Mamba's constant O(1) state as if it scaled like attention's O(n) KV. 2. **Allocation**: `unify_kv_cache_spec_page_size` pads Mamba's small state (~1.1 MiB/block at bf16) up to attention's page si...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: ike attention's O(n) KV. 2. **Allocation**: `unify_kv_cache_spec_page_size` pads Mamba's small state (~1.1 MiB/block at bf16) up to attention's page size (~32 KiB/block at bf16), then `get_kv_cache_config_from_groups` a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ormance]: KV cache ~7x memory overestimation for hybrid Mamba/attention models (Qwen3.5) performance ### Proposal to improve performance Qwen3.5 uses GatedDeltaNet for 24 of 32 layers (O(1) state per request) and full a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: full attention for 8 layers (O(n) KV per token). vLLM's KV cache profiler treats all layers uniformly, inflating both the reported token capacity and the actual memory allocation. Two issues in `vllm/v1/core/kv_cache_ut...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 2. **Allocation**: `unify_kv_cache_spec_page_size` pads Mamba's small state (~1.1 MiB/block at bf16) up to attention's page size (~32 KiB/block at bf16), then `get_kv_cache_config_from_groups` allocates equal-sized tens...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37124](https://github.com/vllm-project/vllm/pull/37124) | mentioned | 0.6 | [Bugfix] Fix KV cache overestimation for hybrid Mamba/attention model… | n submitter - References #37121 --- <details> <summary> Essential Elements of an Effective PR Description Checklist </summary> - [ ] The |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
