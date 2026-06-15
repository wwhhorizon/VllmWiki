# vllm-project/vllm#42960: [Feature]: Batch-invariant support for GDN_ATTN (Qwen3-Next / Qwen3.6 hybrid Mamba+GDN MoE models)

| 字段 | 值 |
| --- | --- |
| Issue | [#42960](https://github.com/vllm-project/vllm/issues/42960) |
| 状态 | open |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | runtime_err |
| Operator 关键词 | attention;cuda;kernel;moe;quantization |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Batch-invariant support for GDN_ATTN (Qwen3-Next / Qwen3.6 hybrid Mamba+GDN MoE models)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug / 🛠 Feature request Setting `VLLM_BATCH_INVARIANT=1` on a model that contains GDN (Gated-Delta-Net) linear-attention layers causes engine startup to abort with: ``` RuntimeError: VLLM batch_invariant mode is not supported for GDN_ATTN. ``` Source: `vllm/v1/attention/selector.py:154` in `_cached_get_mamba_attn_backend`. This is a hard incompatibility — no fallback, no partial mode. It blocks reproducibility work for all Qwen3-Next / Qwen3.6-style models (and any other hybrid Mamba/GDN architecture). ### Reproduction ```bash docker run --rm --gpus all --ipc host \ -e HUGGING_FACE_HUB_TOKEN=... \ -e VLLM_BATCH_INVARIANT=1 \ vllm/vllm-openai:v0.21.0 \ --model cyankiwi/Qwen3.6-35B-A3B-AWQ-4bit \ --trust-remote-code \ --max-model-len 20480 ``` Both `v0.21.0` and `nightly` (May 2026) fail with the same error. The check is triggered as soon as the engine selects the Mamba/GDN attention backend during init, before any AWQ-kernel logic runs — so it is independent of `--quantization`, `--attention-backend`, `VLLM_ATTENTION_BACKEND` (unrecognized in 0.21.0), and other workaround knobs. ### Related - #42456 — added SM80 batch-invariant suppor...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: or all Qwen3-Next / Qwen3.6-style models (and any other hybrid Mamba/GDN architecture). ### Reproduction ```bash docker run --rm --gpus all --ipc host \ -e HUGGING_FACE_HUB_TOKEN=... \ -e VLLM_BATCH_INVARIANT=1 \ vllm/v...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: a hard incompatibility — no fallback, no partial mode. It blocks reproducibility work for all Qwen3-Next / Qwen3.6-style models (and any other hybrid Mamba/GDN architecture). ### Reproduction ```bash docker run --rm --g...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: Source: `vllm/v1/attention/selector.py:154` in `_cached_get_mamba_attn_backend`. This is a hard incompatibility — no fallback, no partial mode. It blocks reproducibility work for all Qwen3-Next / Qwen3.6-style models (a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Batch-invariant support for GDN_ATTN (Qwen3-Next / Qwen3.6 hybrid Mamba+GDN MoE models) ### Your current environment ### 🐛 Describe the bug / 🛠 Feature request Setting `VLLM_BATCH_INVARIANT=1` on a model that...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ch-invariant support for GDN_ATTN (Qwen3-Next / Qwen3.6 hybrid Mamba+GDN MoE models) ### Your current environment ### 🐛 Describe the bug / 🛠 Feature request Setting `VLLM_BATCH_INVARIANT=1` on a model that contains GDN...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
