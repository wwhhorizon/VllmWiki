# vllm-project/vllm#30931: [Bug]: Prefix Cache Corruption with LoRA  with the same name but different id

| 字段 | 值 |
| --- | --- |
| Issue | [#30931](https://github.com/vllm-project/vllm/issues/30931) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf;nondeterministic |
| 根因提示 | env_dependency;memory_layout;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Prefix Cache Corruption with LoRA  with the same name but different id

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After 8 hours of debugging for my project, I'm glad to report this bug 🐶. ## Summary When using vLLM with LoRA adapters and prefix caching enabled, different LoRA configurations with the same `lora_name` but different `lora_int_id` values incorrectly share KV cache blocks. This causes the model to generate outputs using cached activations from the wrong LoRA weights, leading to incorrect/inconsistent behavior. ## Environment - **vLLM version**: v0.11.1 - **Python version**: 3.12 - **GPU**: NVIDIA (Tensor Parallelism = 4) - **Model**: meta-llama/Llama-3.3-70B-Instruct - **LoRA enabled**: Yes (`enable_lora=True`) - **Prefix caching enabled**: Yes (`enable_prefix_caching=True`) ## Expected Behavior Two `LoRARequest` instances with: - Same `lora_name` - Different `lora_int_id` - Different actual LoRA weight files Should be treated as completely separate adapters with independent KV caches. The documentation states: *"lora_int_id must be globally unique for a given adapter"*, implying this should be the primary cache key. ## Actual Behavior The two requests share the same KV cache blocks, causing vLLM to serve cached activations compu...

## 现有链接修复摘要

#31069 Fix LoRA prefix cache corruption by using lora_int_id

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 5: - Inconsistent model outputs - Wrong LoRA behavior being applied - Stale cache hits when editing LoRA configurations ## Root Cause ### Issue 1: `LoRARequest` equality based on `lora_name` only **File**: `vllm/lora/reque...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: s, leading to incorrect/inconsistent behavior. ## Environment - **vLLM version**: v0.11.1 - **Python version**: 3.12 - **GPU**: NVIDIA (Tensor Parallelism = 4) - **Model**: meta-llama/Llama-3.3-70B-Instruct - **LoRA ena...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ix Cache Corruption with LoRA with the same name but different id bug;unstale ### Your current environment ### 🐛 Describe the bug After 8 hours of debugging for my project, I'm glad to report this bug 🐶. ## Summary When...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: *: v0.11.1 - **Python version**: 3.12 - **GPU**: NVIDIA (Tensor Parallelism = 4) - **Model**: meta-llama/Llama-3.3-70B-Instruct - **LoRA enabled**: Yes (`enable_lora=True`) - **Prefix caching enabled**: Yes (`enable_pre...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: Prefix Cache Corruption with LoRA with the same name but different id bug;unstale ### Your current environment ### 🐛 Describe the bug After 8 hours of debugging for my project, I'm glad to report this bug 🐶. #

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31069](https://github.com/vllm-project/vllm/pull/31069) | closes_keyword | 0.95 | Fix LoRA prefix cache corruption by using lora_int_id | Fixes #30931 - LoRA prefix cache corruption The KV cache hash was incorrectly using `lora_name` instead of `lora_int_id` for LoRA requests. This caused different LoRA configuratio |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
