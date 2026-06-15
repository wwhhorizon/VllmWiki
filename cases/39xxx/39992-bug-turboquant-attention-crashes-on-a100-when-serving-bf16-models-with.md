# vllm-project/vllm#39992: [Bug]: Turboquant attention crashes on A100 when serving BF16 models with FP8 KV cache

| 字段 | 值 |
| --- | --- |
| Issue | [#39992](https://github.com/vllm-project/vllm/issues/39992) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;operator;triton |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Turboquant attention crashes on A100 when serving BF16 models with FP8 KV cache

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When serving a BF16 model with the turboquant attention backend on A100 (SM80), the engine crashes during initialization with an `AssertionError` from Triton's `convert_custom_float8`. ### Root cause The Triton kernel `_tq_fused_store_fp8` in `vllm/v1/attention/ops/triton_turboquant_store.py:189` directly casts KV values to FP8: ```python k_vals = tl.load(Key_ptr + base + d_offs, mask=d_mask, other=0.0) k_fp8 = k_vals.to(tl.float8e4b15) if FP8_E4B15 else k_vals.to(tl.float8e4nv) ``` On SM80 (A100), Triton uses a software FP8 conversion path (`convert_custom_float8_sm80`) which only accepts FP16 or FP32 inputs: ```python # triton/language/extra/cuda/utils.py:94 assert arg.type.scalar.is_fp16() or arg.type.scalar.is_fp32() ``` When the model uses BF16, `k_vals` is loaded as BF16, and this assertion fails. This is SM80-specific — on SM89+ (H100), Triton has native FP8 hardware support and may use a different code path. ## How to reproduce ```bash .venv/bin/python -m vllm.entrypoints.openai.api_server \ --model Qwen/Qwen2.5-3B-Instruct \ --kv-cache-dtype turboquant_k8v4 \ --enforce-eager ``` Any BF16 model on A100 with the turboquant...

## 现有链接修复摘要

#39988 [Bugfix] Fix turboquant FP8 cast failure for BF16 models on Ampere GPUs

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: Turboquant attention crashes on A100 when serving BF16 models with FP8 KV cache bug ### Your current environment ### 🐛 Describe the bug When serving a BF16 model with the turboquant attention backend on A100 (SM8...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: Turboquant attention crashes on A100 when serving BF16 models with FP8 KV cache bug ### Your current environment ### 🐛 Describe the bug When serving a BF16 model with the turboquant attention backend on A100 (SM8...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: als.to(tl.float8e4nv) ``` On SM80 (A100), Triton uses a software FP8 conversion path (`convert_custom_float8_sm80`) which only accepts FP16 or FP32 inputs: ```python # triton/language/extra/cuda/utils.py:94 assert arg.t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: Describe the bug When serving a BF16 model with the turboquant attention backend on A100 (SM80), the engine crashes during initialization with an `AssertionError` from Triton's `convert_custom_float8`. ### Root cause Th...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: : Turboquant attention crashes on A100 when serving BF16 models with FP8 KV cache bug ### Your current environment ### 🐛 Describe the bug When serving a BF16 model with the turboquant attention backend on A100 (SM80), t...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39988](https://github.com/vllm-project/vllm/pull/39988) | mentioned | 0.45 | [Bugfix] Fix turboquant FP8 cast failure for BF16 models on Ampere GPUs | ptr + base + d_offs, mask=d_mask, other=0.0).to(tl.float32) ``` pr: #39988 ### before submitting a new issue... - [x] make sure you already searched for relevant issues, and asked… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
