# vllm-project/vllm#43456: [deepseek_v4] DeepSeekV4MTP loader silently skips top-level head.weight + embed.weight → 0% MTP draft acceptance with no error

| 字段 | 值 |
| --- | --- |
| Issue | [#43456](https://github.com/vllm-project/vllm/issues/43456) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | debug |
| Operator 关键词 | fp8;operator;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [deepseek_v4] DeepSeekV4MTP loader silently skips top-level head.weight + embed.weight → 0% MTP draft acceptance with no error

### Issue 正文摘录

## Summary `vllm.models.deepseek_v4.nvidia.mtp.DeepSeekV4MTP.load_weights` silently skips top-level `head.weight` and `embed.weight` when the saved artifact stores them at the top level (not as `mtp.0.head.weight` / `mtp.0.emb.tok_emb.weight`). The MTP layer's `shared_head.head` (ParallelLMHead) and `embed_tokens` (VocabParallelEmbedding) stay uninitialized → MTP draft head emits garbage logits → **0% MTP acceptance with no load-time error**. Speculative decoding produces draft tokens that are 100% rejected by the verifier. ## Mechanism `DeepSeekV4MTP.load_weights` runs this loop: ```python for name, loaded_weight in weights: name = name.replace("mtp.0.", "") # no-op on top-level keys like "head.weight" spec_layer = get_spec_layer_idx(name) if spec_layer is None: continue # ← top-level head.weight, embed.weight die here ... ``` For a key like `head.weight`: - `name.replace("mtp.0.", "")` returns `head.weight` unchanged - `get_spec_layer_idx("head.weight")` returns `None` - Loop hits `continue` → key never routed to the MTP layer - MTP layer constructed `shared_head.head` as ParallelLMHead but no weight ever assigned → keeps init random values ## Repro 1. Save a DSv4-Flash artifact...

## 现有链接修复摘要

#43459 [deepseek_v4] Route top-level head.weight + embed.weight to MTP shared_head/embed_tokens

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: : drafts produced, accepted = 0. We hit this exact scenario in [`canada-quant/dsv4-flash-w4a16-fp8-mtp`](https://github.com/canada-quant/dsv4-flash-w4a16-fp8-mtp) iteration 9. Smoke artifact had 797 `mtp.0.*` keys at fi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: 4MTP loader silently skips top-level head.weight + embed.weight → 0% MTP draft acceptance with no error ## Summary `vllm.models.deepseek_v4.nvidia.mtp.DeepSeekV4MTP.load_weights` silently skips top-level `head.weight` a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: . ## Suggested fix Option A — `DeepSeekV4MTP.load_weights` should explicitly route top-level `head.weight` to `mtp.{N}.shared_head.head.weight` and top-level `embed.weight` to `mtp.{N}.embed_tokens.weight` (one line add...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: produces draft tokens that are 100% rejected by the verifier. ## Mechanism `DeepSeekV4MTP.load_weights` runs this loop: ```python for name, loaded_weight in weights: name = name.replace("mtp.0.", "") # no-op on top-leve...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: + embed.weight → 0% MTP draft acceptance with no error ## Summary `vllm.models.deepseek_v4.nvidia.mtp.DeepSeekV4MTP.load_weights` silently skips top-level `head.weight` and `embed.weight` when the saved artifact stores...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43459](https://github.com/vllm-project/vllm/pull/43459) | closes_keyword | 0.95 | [deepseek_v4] Route top-level head.weight + embed.weight to MTP shared_head/embed_tokens | Closes #43456. ## The bug `DeepSeekV4MTP.load_weights` (`vllm/models/deepseek_v4/nvidia/mtp.py`) iterates `weights` and does: ```python for name, loaded_weight in weights: m |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
