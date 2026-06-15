# vllm-project/vllm#4532: [RFC]: Refactor FP8 kv-cache

| 字段 | 值 |
| --- | --- |
| Issue | [#4532](https://github.com/vllm-project/vllm/issues/4532) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;fp8;kernel;quantization |
| 症状 | build_error |
| 根因提示 | dtype |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Refactor FP8 kv-cache

### Issue 正文摘录

### Motivation. **Support float8_e4m3 for NVIDIA GPUs:** The current FP8 kv-cache supports e5m2 on NVIDIA GPUs, and e4m3 on AMD GPUs. While e5m2 seems to be an ideal format for kv-cache storage due to better performance (i.e., e5m2 has the same number of exponent bits as fp16 so its scaling overhead could be smaller than e4m3), model checkpoints with FP8 weights mostly adopt e4m3 format. As a result, in order to support FP8 models in vLLM, we need float8_e4m3 kv-cache for both vendors. **Refactor FP8 kv-cache:** In the current implementation, we use macros to dispatch FP8 tensor quantization logic in vLLM custom kernels. For example, in the current `cache_kernel.cu`, we use the following code to quantize tensors for CUDA or ROCm: ``` #if defined(ENABLE_FP8_E5M2) // Only for CUDA key_cache[tgt_key_idx] = fp8_e5m2_unscaled::vec_conversion (tgt_key); value_cache[tgt_value_idx] = fp8_e5m2_unscaled::vec_conversion (tgt_value); #elif defined(ENABLE_FP8_E4M3) // Only for ROCm key_cache[tgt_key_idx] = fp8_e4m3::scaled_vec_conversion (tgt_key, kv_scale); value_cache[tgt_value_idx] = fp8_e4m3::scaled_vec_conversion (tgt_value, kv_scale); #else assert(false); #endif ``` This creates the foll...

## 现有链接修复摘要

#4535 [Kernel] Refactor FP8 kv-cache with NVIDIA float8_e4m3 support | #4893 [Misc] Load FP8 kv-cache scaling factors from checkpoints

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [RFC]: Refactor FP8 kv-cache RFC ### Motivation. **Support float8_e4m3 for NVIDIA GPUs:** The current FP8 kv-cache supports e5m2 on NVIDIA GPUs, and e4m3 on AMD GPUs. While e5m2 seems to be an ideal format for kv-cache...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: / Only for CUDA key_cache[tgt_key_idx] = fp8_e5m2_unscaled::vec_conversion (tgt_key); value_cache[tgt_value_idx] = fp8_e5m2_unscaled::vec_conversion (tgt_value); #elif defined(ENABLE_FP8_E4M3) // Only for ROCm key_cache...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: he same number of exponent bits as fp16 so its scaling overhead could be smaller than e4m3), model checkpoints with FP8 weights mostly adopt e4m3 format. As a result, in order to support FP8 models in vLLM, we need floa...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: Refactor FP8 kv-cache:** In the current implementation, we use macros to dispatch FP8 tensor quantization logic in vLLM custom kernels. For example, in the current `cache_kernel.cu`, we use the following code to quantiz...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: gt_value_idx] = fp8_e4m3::scaled_vec_conversion (tgt_value, kv_scale); #else assert(false); #endif ``` This creates the following issues: 1. We cannot enable e4m3 and e5m2 in the same build. 2. The function arguments ar...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4535](https://github.com/vllm-project/vllm/pull/4535) | mentioned | 0.6 | [Kernel] Refactor FP8 kv-cache with NVIDIA float8_e4m3 support | efactor FP8 kv-cache with NVIDIA float8_e4m3 support The first PR for #4532. Task list: - [x] Add NVIDIA e4m3. - [x] Refactor cache_kernel.cu. - [x] Unit tests for reshape and cac |
| [#4893](https://github.com/vllm-project/vllm/pull/4893) | mentioned | 0.6 | [Misc] Load FP8 kv-cache scaling factors from checkpoints | sc] Load FP8 kv-cache scaling factors from checkpoints The 2nd PR for #4532. This PR supports loading FP8 kv-cache scaling factors from a FP8 checkpoint (with `.kv_scale` paramete… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
