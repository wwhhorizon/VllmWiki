# vllm-project/vllm#38041: V2 model runner crashes on Qwen3.5 mixed attention (linear + full)

| 字段 | 值 |
| --- | --- |
| Issue | [#38041](https://github.com/vllm-project/vllm/issues/38041) |
| 状态 | open |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;gemm_linear;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | attention;cache;fp8;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> V2 model runner crashes on Qwen3.5 mixed attention (linear + full)

### Issue 正文摘录

## Description When enabling `VLLM_USE_V2_MODEL_RUNNER=1` with Qwen3.5 models (`Qwen3_5ForConditionalGeneration` / `Qwen3_5ForCausalLM`), the engine crashes during KV cache initialization with an `AssertionError` in `_reshape_kv_cache`. ## Environment - vLLM version: `0.17.2.dev0+g95c0f928c.d20260313` (nightly) - GPU: NVIDIA GH200 480GB - Model: Qwen3.5 9B (loaded via VL wrapper with `language_model_only=True`) - Config: FP8 online quantization, 262K context, chunked prefill, eager mode ## Error ``` (EngineCore_DP0 pid=220) ERROR [core.py:1100] File ".../vllm/v1/worker/gpu/attn_utils.py", line 112, in _reshape_kv_cache assert isinstance(kv_cache_spec, AttentionSpec) AssertionError ``` ## Root Cause Qwen3.5 uses a hybrid architecture with both full attention (GQA) and linear attention (GDN/Mamba-like) layers. The `layer_types` config alternates between `"linear_attention"` and `"full_attention"`: ```json "layer_types": ["linear_attention", "linear_attention", "linear_attention", "full_attention", ...] ``` The linear attention layers produce a KV cache spec that is **not** an `AttentionSpec` (it's a recurrent state spec). The V2 model runner's `_reshape_kv_cache` in `attn_utils.py`...

## 现有链接修复摘要

#38081 [Bugfix] Fix V2 model runner crash on hybrid attention models (Qwen3.5)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: with an `AssertionError` in `_reshape_kv_cache`. ## Environment - vLLM version: `0.17.2.dev0+g95c0f928c.d20260313` (nightly) - GPU: NVIDIA GH200 480GB - Model: Qwen3.5 9B (loaded via VL wrapper with `language_model_only...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 3.5 9B (loaded via VL wrapper with `language_model_only=True`) - Config: FP8 online quantization, 262K context, chunked prefill, eager mode ## Error ``` (EngineCore_DP0 pid=220) ERROR [core.py:1100] File ".../vllm/v1/wo...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: V1 model runner. - A related issue: the V1 engine's `unify_kv_cache_spec_page_size` in `kv_cache_utils.py` also fails with `NotImplementedError` when loading text-only `Qwen3_5ForCausalLM`, because linear and full atten...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: V2 model runner crashes on Qwen3.5 mixed attention (linear + full) ## Description When enabling `VLLM_USE_V2_MODEL_RUNNER=1` with Qwen3.5 models (`Qwen3_5ForConditionalGeneration` / `Qwen3_5ForCausalLM`), the engine cra...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: tils.py` assumes all specs are `AttentionSpec` and crashes. ## Steps to Reproduce 1. Load any Qwen3.5 model (e.g., 9B or 27B) 2. Set `VLLM_USE_V2_MODEL_RUNNER=1` 3. Start the engine ```python from vllm import LLM llm =...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38081](https://github.com/vllm-project/vllm/pull/38081) | closes_keyword | 0.95 | [Bugfix] Fix V2 model runner crash on hybrid attention models (Qwen3.5) | Fixes #38041 ## Before Fix (crash log) <details><summary>V2 model runner crashes with AssertionError on Qwen3.5</summary> ``` $ VLLM_USE_V2_MODEL_RUNNER=1 python -m vllm.entrypo |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
