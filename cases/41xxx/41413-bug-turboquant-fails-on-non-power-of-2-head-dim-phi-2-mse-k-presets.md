# vllm-project/vllm#41413: [Bug]: TurboQuant fails on non-power-of-2 head_dim (Phi-2, MSE-K presets)

| 字段 | 值 |
| --- | --- |
| Issue | [#41413](https://github.com/vllm-project/vllm/issues/41413) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;gemm_linear;hardware_porting;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;fp8;gemm;kernel |
| 症状 | crash;mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TurboQuant fails on non-power-of-2 head_dim (Phi-2, MSE-K presets)

### Issue 正文摘录

## Reproduction ```python from vllm import LLM, SamplingParams llm = LLM(model="microsoft/phi-2", dtype="bfloat16", kv_cache_dtype="turboquant_4bit_nc", max_model_len=2048) llm.generate(["The capital of France is"], SamplingParams(max_tokens=32)) ``` Engine init crashes: ``` File "vllm/v1/attention/backends/turboquant_attn.py", line 380, in do_kv_cache_update y = x_hat @ PiT RuntimeError: mat1 and mat2 shapes cannot be multiplied (16384x80 and 128x128) ``` ## Root cause `_build_hadamard_cached(d)` doubles `H` until `H.shape[0] >= d` then normalizes by `sqrt(d)`. For `d=80` it overshoots to 128×128 and divides by `sqrt(80)` — wrong size, not orthonormal at that size. `_ensure_on_device` stores it as `layer._tq_PiT`, and the MSE-K rotation GEMM hits a shape mismatch on `q @ PiT`. ## Affected presets / models - **Affected:** `turboquant_4bit_nc`, `turboquant_3bit_nc`, `turboquant_k3v4_nc` on any non-power-of-2 `head_dim` - **Not affected:** `turboquant_k8v4` — FP8-K bypasses the WHT (in-kernel FP8 cast), so the broken matrix is built but never multiplied. The model loads, but the PiT buffer is wasted VRAM. - **Models with non-pow-2 `head_dim`:** Phi-2 (`d=80`) is the canonical exampl...

## 现有链接修复摘要

#41414 [Bugfix][Attention][TurboQuant] Pad head_dim to power-of-2 for WHT

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: TurboQuant fails on non-power-of-2 head_dim (Phi-2, MSE-K presets) ## Reproduction ```python from vllm import LLM, SamplingParams llm = LLM(model="microsoft/phi-2", dtype="bfloat16", kv_cache_dtype="turboquant_4b...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: f-2 head_dim (Phi-2, MSE-K presets) ## Reproduction ```python from vllm import LLM, SamplingParams llm = LLM(model="microsoft/phi-2", dtype="bfloat16", kv_cache_dtype="turboquant_4bit_nc", max_model_len=2048) llm.genera...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: stores it as `layer._tq_PiT`, and the MSE-K rotation GEMM hits a shape mismatch on `q @ PiT`. ## Affected presets / models - **Affected:** `turboquant_4bit_nc`, `turboquant_3bit_nc`, `turboquant_k3v4_nc` on any non-powe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: # Reproduction ```python from vllm import LLM, SamplingParams llm = LLM(model="microsoft/phi-2", dtype="bfloat16", kv_cache_dtype="turboquant_4bit_nc", max_model_len=2048) llm.generate(["The capital of France is"], Samp...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ` stores it as `layer._tq_PiT`, and the MSE-K rotation GEMM hits a shape mismatch on `q @ PiT`. ## Affected presets / models - **Affected:** `turboquant_4bit_nc`, `turboquant_3bit_nc`, `turboquant_k3v4_nc` on any non-po...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41414](https://github.com/vllm-project/vllm/pull/41414) | closes_keyword | 0.95 | [Bugfix][Attention][TurboQuant] Pad head_dim to power-of-2 for WHT | Fixes #41413. cc @vibhavagarwal5 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
