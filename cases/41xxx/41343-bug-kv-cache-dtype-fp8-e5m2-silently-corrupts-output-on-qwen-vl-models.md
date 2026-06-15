# vllm-project/vllm#41343: [Bug]: `kv_cache_dtype="fp8_e5m2"` silently corrupts output on Qwen-VL models (Qwen2-VL, Qwen2.5-VL) with default scaling

| 字段 | 值 |
| --- | --- |
| Issue | [#41343](https://github.com/vllm-project/vllm/issues/41343) |
| 状态 | open |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `kv_cache_dtype="fp8_e5m2"` silently corrupts output on Qwen-VL models (Qwen2-VL, Qwen2.5-VL) with default scaling

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In vLLM 0.19.0, when testing on Qwen2-VL-2B and Qwen2.5-VL-3B, `kv_cache_dtype="fp8_e5m2"` with the default `calculate_kv_scales=False` silently produces degenerate or hallucinated output. Failure rate scales with input pixel variance: uniform-color images fail frequently, natural images mostly survive. `OpenGVLab/InternVL3-1B` under the same code path shows 0% failure, so this is specific to Qwen-family weight distributions, not a generic FP8 KV cache issue. Two workarounds fully fix it: switch to `fp8_e4m3`, or pass `calculate_kv_scales=True`. ## Reproducer ```python from PIL import Image from vllm import LLM, SamplingParams Image.new("RGB", (224, 224), (128, 128, 128)).save("/tmp/uniform_gray.png") def run(kv_dtype, calc_scales=False): llm = LLM( model="Qwen/Qwen2.5-VL-3B-Instruct", enforce_eager=True, dtype="float16", kv_cache_dtype=kv_dtype, calculate_kv_scales=calc_scales, max_model_len=2048, limit_mm_per_prompt={"image": 1}, trust_remote_code=True, ) tok = llm.get_tokenizer() prompt = tok.apply_chat_template( [{"role": "user", "content": [ {"type": "image"}, {"type": "text", "text": "Describe what you see in this image."}]...

## 现有链接修复摘要

#41408 [codex] Guard Qwen-VL fp8_e5m2 default KV scales

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: `kv_cache_dtype="fp8_e5m2"` silently corrupts output on Qwen-VL models (Qwen2-VL, Qwen2.5-VL) with default scaling bug ### Your current environment ### 🐛 Describe the bug In vLLM 0.19.0, when testing on Qwen2-VL-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: `kv_cache_dtype="fp8_e5m2"` silently corrupts output on Qwen-VL models (Qwen2-VL, Qwen2.5-VL) with default scaling bug ### Your current environment ### 🐛 Describe the bug In vLLM 0.19.0, when testing on Qwen2-VL-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: default `calculate_kv_scales=False` silently produces degenerate or hallucinated output. Failure rate scales with input pixel variance: uniform-color images fail frequently, natural images mostly survive. `OpenGVLab/Int...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: seeing that, we ran the same `kv_cache_dtype="fp8_e5m2"` config across a small batch of uniform-color images on `Qwen/Qwen2-VL-2B-Instruct` (prompt: `"What color is this image?"`, same sampling settings). The 3B model d...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: on;sampling_logits;speculative_decoding cache;cuda;fp8;operator;sampling;triton build_error;nan_inf dtype;env_dependency;shape #41408 [codex] Guard Qwen-VL fp8_e5m2 default KV scales Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41408](https://github.com/vllm-project/vllm/pull/41408) | mentioned | 0.6 | [codex] Guard Qwen-VL fp8_e5m2 default KV scales | n-VL fp8_e5m2 default KV scales Mitigates one unsafe path reported in #41343 by adding a fail-fast guard. ## What changed - Adds a post-load attention guard for Qwen2-VL and Qwen2… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
