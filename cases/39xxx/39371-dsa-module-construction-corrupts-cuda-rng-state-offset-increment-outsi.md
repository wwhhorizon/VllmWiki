# vllm-project/vllm#39371: DSA module construction corrupts CUDA RNG state (Offset increment outside graph capture)

| 字段 | 值 |
| --- | --- |
| Issue | [#39371](https://github.com/vllm-project/vllm/issues/39371) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;hardware_porting;model_support |
| 子分类 | race_cond |
| Operator 关键词 | attention;cuda;kernel |
| 症状 | crash;nondeterministic |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> DSA module construction corrupts CUDA RNG state (Offset increment outside graph capture)

### Issue 正文摘录

## Bug: DeepseekV2MLAAttention construction leaves CUDA graph RNG offset tracking active ### Description Constructing a `DeepseekV2MLAAttention` module for DSA (DeepSeek-V3.2 sparse MLA) leaves the CUDA graph RNG offset tracking in an active state. Any subsequent RNG operation (`normal_()`, `uniform_()`, `torch.randn()`, `torch.randint()`, etc.) on the same device fails with: ``` RuntimeError: Offset increment outside graph capture encountered unexpectedly. ``` This happens outside vLLM's model runner — we construct standalone modules for kernel benchmarking. Regular (non-DSA) MLA modules do not trigger this. ### Reproduction ```python import torch from vllm.config import VllmConfig, set_current_vllm_config from vllm.model_executor.models.deepseek_v2 import DeepseekV2MLAAttention vllm_config = ... # VllmConfig with DeepSeek-V3.2 model with set_current_vllm_config(vllm_config): attn_module = DeepseekV2MLAAttention( vllm_config=vllm_config, config=hf_config, # ... DSA-specific config prefix="model.layers.0.self_attn", ) attn_module = attn_module.to("cuda:0") # This crashes: torch.randn(1, device="cuda:0") # RuntimeError: Offset increment outside graph capture encountered unexpectedl...

## 现有链接修复摘要

#33451 [Attention] Add FlashInfer Sparse MLA backend | #34457 [Bugfix][MTP][Sparse MLA] Allow sparse MLA with MTP to run with FULL cudagraphs | #34552 [BugFix] Add support for MTP num_speculative_tokens > 1 with sparse MLA

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: DSA module construction corrupts CUDA RNG state (Offset increment outside graph capture) ## Bug: DeepseekV2MLAAttention construction leaves CUDA graph RNG offset tracking active ### Description Constructing a `DeepseekV...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: (non-DSA) MLA modules do not trigger this. ### Reproduction ```python import torch from vllm.config import VllmConfig, set_current_vllm_config from vllm.model_executor.models.deepseek_v2 import DeepseekV2MLAAttention vl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: graph capture encountered unexpectedly. ``` This happens outside vLLM's model runner — we construct standalone modules for kernel benchmarking. Regular (non-DSA) MLA modules do not trigger this. ### Reproduction ```pyth...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: vironment - vLLM v0.17.0 - NVIDIA B200 (Blackwell, SM100) - CUDA 13.0 - FlashInfer sparse MLA backend ### Likely cause The FlashInfer sparse MLA backend (#33451) or DSA CUDA graph support (#34457) appears to activate CU...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: Workaround Avoid all RNG operations after DSA module construction. Use deterministic initialization (`fill_()`, `torch.full()`, `torch.zeros()`) instead. correctness attention_kv_cache;hardware_porting;model_support att...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#33451](https://github.com/vllm-project/vllm/pull/33451) | mentioned | 0.45 | [Attention] Add FlashInfer Sparse MLA backend | rse mla backend ### likely cause the flashinfer sparse mla backend (#33451) or dsa cuda graph support (#34457) appears to activate cuda graph rng offset tracking during module con… |
| [#34457](https://github.com/vllm-project/vllm/pull/34457) | mentioned | 0.45 | [Bugfix][MTP][Sparse MLA] Allow sparse MLA with MTP to run with FULL cudagraphs | the flashinfer sparse mla backend (#33451) or dsa cuda graph support (#34457) appears to activate cuda graph rng offset tracking during module construction that persists after `__… |
| [#34552](https://github.com/vllm-project/vllm/pull/34552) | mentioned | 0.45 | [BugFix] Add support for MTP num_speculative_tokens > 1 with sparse MLA | ng during module construction that persists after `__init__` returns. #34552 also notes dsa "has issues with cudagraphs" on blackwell. ### workaround avoid all rng operations afte… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
