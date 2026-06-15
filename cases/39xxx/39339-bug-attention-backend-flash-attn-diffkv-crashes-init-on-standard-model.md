# vllm-project/vllm#39339: [Bug]: `attention_backend='FLASH_ATTN_DIFFKV'` crashes init on standard models with "too many values to unpack"

| 字段 | 值 |
| --- | --- |
| Issue | [#39339](https://github.com/vllm-project/vllm/issues/39339) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `attention_backend='FLASH_ATTN_DIFFKV'` crashes init on standard models with "too many values to unpack"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The DIFFKV backend assumes the KV cache is a 2-tensor stack (`key_cache, value_cache = kv_cache.unbind(0)`), but on models with uniform K/V heads it has a different shape. There is no upfront compatibility check. ### Reproduce ```python import vllm vllm.LLM( model="Qwen/Qwen3-0.6B", max_model_len=512, attention_backend="FLASH_ATTN_DIFFKV", ) ``` EngineCore stderr: ``` File ".../vllm/v1/attention/backends/flash_attn.py", line 808, in do_kv_cache_update key_cache, value_cache = kv_cache.unbind(0) ^^^^^^^^^^^^^^^^^^^^^^ ValueError: too many values to unpack (expected 2) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#39417 [Attention] Validate DIFFKV via backend selection

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: hape. There is no upfront compatibility check. ### Reproduce ```python import vllm vllm.LLM( model="Qwen/Qwen3-0.6B", max_model_len=512, attention_backend="FLASH_ATTN_DIFFKV", ) ``` EngineCore stderr: ``` File ".../vllm...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: `attention_backend='FLASH_ATTN_DIFFKV'` crashes init on standard models with "too many values to unpack" bug ### Your current environment ### 🐛 Describe the bug The DIFFKV backend assumes the KV cache is a 2-tens...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: `attention_backend='FLASH_ATTN_DIFFKV'` crashes init on standard models with "too many values to unpack" bug ### Your current environment ### 🐛 Describe the bug The DIFFKV backend assumes the KV cache is a 2-tens...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: it has a different shape. There is no upfront compatibility check. ### Reproduce ```python import vllm vllm.LLM( model="Qwen/Qwen3-0.6B", max_model_len=512, attention_backend="FLASH_ATTN_DIFFKV", ) ``` EngineCore stderr...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39417](https://github.com/vllm-project/vllm/pull/39417) | closes_keyword | 0.95 | [Attention] Validate DIFFKV via backend selection | Fixes #39339. ## Purpose Reject `attention_backend="FLASH_ATTN_DIFFKV"` through normal backend validation instead of letting initialization continue until it crashes. ## Test |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
