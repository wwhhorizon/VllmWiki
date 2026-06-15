# vllm-project/vllm#42821: [Bug]: `model.load_weights` silently corrupts MoE forward on second call

| 字段 | 值 |
| --- | --- |
| Issue | [#42821](https://github.com/vllm-project/vllm/issues/42821) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf;nondeterministic |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: `model.load_weights` silently corrupts MoE forward on second call

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug A loaded model's `load_weights` method (e.g. `Qwen3MoeForCausalLM.load_weights`) is not idempotent on a live `AsyncLLMEngine` for unquantized MoE models that land on the FlashInfer-CUTLASS or FlashInfer-TRTLLM backend. Calling `load_weights` a second time, even with the same HF safetensors source the engine was originally loaded from, silently corrupts every subsequent forward into a stable multi-language subword soup: ```none ...Sot remis二十四节气ttsueEil Извест彻底s [data)Gilr)fam)Aam shcuiteg... ``` ### Mechanism I ran an extensive bisect on this between v0.19.1 and v0.20.2, and arrived at https://github.com/vllm-project/vllm/pull/36286 (from `vllm==0.20.0`) causing this regression for the MoE. backends `FLASHINFER_CUTLASS` and `FLASHINFER_TRTLLM`. 1. https://github.com/vllm-project/vllm/pull/36286 moves every per-backend kernel-layout transform (e.g. `FLASHINFER_CUTLASS`, `FLASHINFER_TRTLLM`) out of `UnquantizedFusedMoEMethod.process_weights_after_loading`'s body and routes it through [`_setup_kernel`](https://github.com/vllm-project/vllm/blob/v0.20.2/vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py#L150-L177) →...

## 现有链接修复摘要

#36286 [MoE Refactor] Migrate Unquantized to Full Oracle Flow | #42823 [Bugfix][Model Loader] Make `model.load_weights` safe to invoke on already-initialized model

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: [Bug]: `model.load_weights` silently corrupts MoE forward on second call bug ### Your current environment ### 🐛 Describe the bug A loaded model's `load_weights` method (e.g. `Qwen3MoeForCausalLM.load_weights`) is not id...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: yers/fused_moe/oracle/unquantized.py#L296-L321) applies a MoE-backend-specific layout mutation once at engine init: - `FLASHINFER_CUTLASS` (gated MoE): `swap_w13_to_w31(w13)` (swaps the `[w1; w3]` halves to `[w3; w1]`)....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: t on a live `AsyncLLMEngine` for unquantized MoE models that land on the FlashInfer-CUTLASS or FlashInfer-TRTLLM backend. Calling `load_weights` a second time, even with the same HF safetensors source the engine was ori...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: ersa); the resulting forward output is a multilingual subword soup. ### Reproducer ```python import asyncio import glob import os import sys import time from pathlib import Path import vllm from huggingface_hub import s...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: usalLM.load_weights`) is not idempotent on a live `AsyncLLMEngine` for unquantized MoE models that land on the FlashInfer-CUTLASS or FlashInfer-TRTLLM backend. Calling `load_weights` a second time, even with the same HF...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36286](https://github.com/vllm-project/vllm/pull/36286) | mentioned | 0.45 | [MoE Refactor] Migrate Unquantized to Full Oracle Flow | convert_moe_weights_to_flashinfer_trtllm_block_layout(...)`. - #36286 now routes the install through `replace_parameter`, which preserves `weight_loader`, making the corruption ha |
| [#42823](https://github.com/vllm-project/vllm/pull/42823) | closes_keyword | 0.95 | [Bugfix][Model Loader] Make `model.load_weights` safe to invoke on already-initialized model | Closes #42821. `UnquantizedFusedMoEMethod.process_weights_after_loading` rewrites `layer.w13_weight` in place once at engine init — `swap_w13_to_w31` on the FlashInfer CUTLASS p |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
