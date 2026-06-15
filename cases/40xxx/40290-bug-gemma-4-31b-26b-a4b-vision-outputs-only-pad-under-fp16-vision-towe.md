# vllm-project/vllm#40290: [Bug]: Gemma 4 (31B/26B-A4B) vision outputs only <pad> under fp16 — vision_tower standardize overflows

| 字段 | 值 |
| --- | --- |
| Issue | [#40290](https://github.com/vllm-project/vllm/issues/40290) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cuda;gemm;operator;quantization;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Gemma 4 (31B/26B-A4B) vision outputs only <pad> under fp16 — vision_tower standardize overflows

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Related issues (not duplicates) - [#40095](https://github.com/vllm-project/vllm/issues/40095) — `Gemma4MultimodalEmbedder` norm/linear order swap causes audio ASR hallucination. **Same file**, different layer and different symptom; both can coexist. - [#40106](https://github.com/vllm-project/vllm/issues/40106) / PR [#40185](https://github.com/vllm-project/vllm/pull/40185) — missing prefix-LM mask for `use_bidirectional_attention="vision"`. Confirmed **not** the cause of this pad-token bug (details in Ruled-out hypotheses below). - [#40247](https://github.com/vllm-project/vllm/issues/40247) / [#40286](https://github.com/vllm-project/vllm/issues/40286) — Gemma 4 26B-A4B AWQ **fails to load** on v0.19.1. This bug loads fine (engine starts, vision_tower instantiated) and fails at inference; different surface. ## TL;DR vLLM's Gemma 4 multimodal loader casts `vision_tower` to the engine dtype. With `--dtype float16` (default for AWQ), the SigLIP final standardization step `(h - std_bias) * std_scale` overflows fp16 because `|std_bias|` reaches ~5.4e4 (fp16 max is 6.55e4). `vision_tower.last_hidden_state` becomes `-inf`, which propa...

## 现有链接修复摘要

#40185 gemma4: Enable mm prefix-lm masking for vision bidirectional attention | #40347 [Bugfix][Gemma4] Fix vision fp16 overflow causing <pad> output

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: ;DR vLLM's Gemma 4 multimodal loader casts `vision_tower` to the engine dtype. With `--dtype float16` (default for AWQ), the SigLIP final standardization step `(h - std_bias) * std_scale` overflows fp16 because `|std_bi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Gemma 4 (31B/26B-A4B) vision outputs only <pad> under fp16 — vision_tower standardize overflows ### Your current environment ### 🐛 Describe the bug ### Related issues (not duplicates) - [#40095](https://github.co...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: `Gemma4MultimodalEmbedder` norm/linear order swap causes audio ASR hallucination. **Same file**, different layer and different symptom; both can coexist. - [#40106](https://github.com/vllm-project/vllm/issues/40106) / P...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: modal RMSNorm, and the language model samples ` ` tokens for every image request. The weight is stored in bf16 in the checkpoint and has a range that bf16 can hold but fp16 cannot. Keeping `vision_tower` at bf16 (or fp3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: to the image path. ## Evidence: vision_tower output is -inf I added a small diagnostic patch to `vllm/model_executor/models/gemma4_mm.py` that logs tensor stats at three points in the image pipeline: after `vision_tower...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40185](https://github.com/vllm-project/vllm/pull/40185) | mentioned | 0.45 | gemma4: Enable mm prefix-lm masking for vision bidirectional attention | ginal report about missing prefix-lm (related but not this bug) - pr [#40185](https://github.com/vllm-project/vllm/pull/40185) — prefix-lm fix, requested-closed; not required - hf… |
| [#40347](https://github.com/vllm-project/vllm/pull/40347) | closes_keyword | 0.95 | [Bugfix][Gemma4] Fix vision fp16 overflow causing <pad> output | Fixes #40290. Gemma4 SigLIP's final `(h - std_bias) * std_scale` overflows fp16: `\|std_bias\|` reaches ~5.4e4 in the 31B / 26B-A4B checkpoints, fp16 max is ±6.55e4. The intermediat |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
