# vllm-project/vllm#42068: Gemma 4 + DFlash incompatible: MTP-specific backend propagation forces TRITON_ATTN on independent (DFlash) drafters

| 字段 | 值 |
| --- | --- |
| Issue | [#42068](https://github.com/vllm-project/vllm/issues/42068) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;sampling |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> Gemma 4 + DFlash incompatible: MTP-specific backend propagation forces TRITON_ATTN on independent (DFlash) drafters

### Issue 正文摘录

# DRAFT — vLLM GitHub Issue (source-verified) **Status:** ready for review. Once approved, post via: ``` gh issue create --repo vllm-project/vllm \ --title "Gemma 4 + DFlash incompatible: MTP-specific backend propagation forces TRITON_ATTN on independent (DFlash) drafters" \ --body-file notebooks/DFLASH_VLLM_ISSUE_DRAFT.md ``` --- ## Title `Gemma 4 + DFlash incompatible: MTP-specific backend propagation forces TRITON_ATTN on independent (DFlash) drafters` ## Body ### Summary For Gemma 4, the spec-decode draft-config builder unconditionally propagates the target's force-locked `TRITON_ATTN` backend to the drafter. This is correct for **MTP** drafters (KV-shared with target — they need the same backend) but breaks **DFlash** drafters (independent KV, non-causal attention) which require `FLASHINFER` or `FLASH_ATTN`. The result: Gemma 4 + DFlash speculative decoding is structurally impossible today, even though `SpeculativeConfig.attention_backend` exists in the documented API. ### Reproducer vLLM nightly `0.20.2rc1.dev95+g8a4888be2`, Modal H100, fresh image with `flashinfer-python>=0.2.0` installed. ```python from vllm import LLM llm = LLM( model="google/gemma-4-31B-it", max_model_le...

## 现有链接修复摘要

#41745 [Spec Decode] Add Gemma4 MTP speculative decoding support | #42069 [Spec Decode] Allow DFlash drafter to autoselect non-causal-capable backend on Gemma 4

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Gemma 4 + DFlash incompatible: MTP-specific backend propagation forces TRITON_ATTN on independent (DFlash) drafters # DRAFT — vLLM GitHub Issue (source-verified) **Status:** ready for review. Once approved, post via: ``...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 5: `SpeculativeConfig.attention_backend` exists in the documented API. ### Reproducer vLLM nightly `0.20.2rc1.dev95+g8a4888be2`, Modal H100, fresh image with `flashinfer-python>=0.2.0` installed. ```python from vllm import...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: d API. ### Reproducer vLLM nightly `0.20.2rc1.dev95+g8a4888be2`, Modal H100, fresh image with `flashinfer-python>=0.2.0` installed. ```python from vllm import LLM llm = LLM( model="google/gemma-4-31B-it", max_model_len=...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: lm = LLM( model="google/gemma-4-31B-it", max_model_len=4096, dtype="bfloat16", speculative_config={ "method": "dflash", "model": "z-lab/gemma-4-31B-it-DFlash", "num_speculative_tokens": 16, }, ) ``` Failing log: ``` INF...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: -specific backend propagation forces TRITON_ATTN on independent (DFlash) drafters # DRAFT — vLLM GitHub Issue (source-verified) **Status:** ready for review. Once approved, post via: ``` gh issue create --repo vllm-proj...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41745](https://github.com/vllm-project/vllm/pull/41745) | mentioned | 0.45 | [Spec Decode] Add Gemma4 MTP speculative decoding support | decoding support (cc @lucianommartins — natural reviewer; thanks for #41745, this issue is the inverse case for independent drafters) - vllm stable docs already document `speculat… |
| [#42069](https://github.com/vllm-project/vllm/pull/42069) | closes_keyword | 0.95 | [Spec Decode] Allow DFlash drafter to autoselect non-causal-capable backend on Gemma 4 | Fixes #42068. When the target is Gemma 4 (heterogeneous head dimensions: `head_dim=256`, `global_head_dim=512`), `Gemma4Config.verify_and_update_config` force-locks `attention_con |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
