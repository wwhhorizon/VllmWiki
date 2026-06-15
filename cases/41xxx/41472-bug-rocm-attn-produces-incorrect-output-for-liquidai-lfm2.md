# vllm-project/vllm#41472: [Bug]: ROCM_ATTN produces incorrect output for LiquidAI LFM2

| 字段 | 值 |
| --- | --- |
| Issue | [#41472](https://github.com/vllm-project/vllm/issues/41472) |
| 状态 | open |
| 标签 | rocm |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cuda |
| 症状 | mismatch |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ROCM_ATTN produces incorrect output for LiquidAI LFM2

### Issue 正文摘录

## Summary `ROCM_ATTN` appears to produce incorrect / gibberish continuations for `LiquidAI/LFM2-8B-A1B` on ROCm. The same prompts produce sane outputs with Hugging Face Transformers in the same environment, while vLLM with the ROCm attention path produces corrupted tails after initially-correct tokens. This issue is intended to track the root cause discussed in https://github.com/vllm-project/vllm/pull/41054. That PR works around the problem by avoiding the default ROCm attention backend for this model family, but the underlying `ROCM_ATTN` correctness issue should be tracked separately. ## Environment - Hardware: AMD Instinct MI325X (`gfx942`) - ROCm/HIP: `7.2.53211` - vLLM wheel: `0.20.0+rocm721` - Torch: `2.10.0+git8514f05` - Transformers: `5.6.2` - Model: `LiquidAI/LFM2-8B-A1B` - dtype: `bfloat16` - `max_model_len=2048` - `enforce_eager=True` I reproduced this with the ROCm wheels. I have not yet verified the release Docker image. ## Reproduction Minimal shape of the vLLM run: ```python from transformers import AutoTokenizer from vllm import LLM, SamplingParams model = "LiquidAI/LFM2-8B-A1B" messages = [ [{"role": "user", "content": "Answer with a single number only. What is...

## 现有链接修复摘要

#42420 rocm_attn: fix paged attention for custom KV cache layouts

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Hardware: AMD Instinct MI325X (`gfx942`) - ROCm/HIP: `7.2.53211` - vLLM wheel: `0.20.0+rocm721` - Torch: `2.10.0+git8514f05` - Transformers: `5.6.2` - Model: `LiquidAI/LFM2-8B-A1B` - dtype: `bfloat16` - `max_model_len=2...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: ROCM_ATTN produces incorrect output for LiquidAI LFM2 rocm ## Summary `ROCM_ATTN` appears to produce incorrect / gibberish continuations for `LiquidAI/LFM2-8B-A1B` on ROCm. The same prompts produce sane outputs w...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: That PR works around the problem by avoiding the default ROCm attention backend for this model family, but the underlying `ROCM_ATTN` correctness issue should be tracked separately. ## Environment - Hardware: AMD Instin...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: .0+git8514f05` - Transformers: `5.6.2` - Model: `LiquidAI/LFM2-8B-A1B` - dtype: `bfloat16` - `max_model_len=2048` - `enforce_eager=True` I reproduced this with the ROCm wheels. I have not yet verified the release Docker...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: 1B` - dtype: `bfloat16` - `max_model_len=2048` - `enforce_eager=True` I reproduced this with the ROCm wheels. I have not yet verified the release Docker image. ## Reproduction Minimal shape of the vLLM run: ```python fr...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42420](https://github.com/vllm-project/vllm/pull/42420) | closes_keyword | 0.95 | rocm_attn: fix paged attention for custom KV cache layouts | Fixes #41472 — the ROCm custom paged-attention kernel (`paged_attention_ll4mi_QKV_mfma{4,16}`) produces wrong outputs for models whose KV cache layout does not match the standard c |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
