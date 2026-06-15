# vllm-project/vllm#41564: [Bug]: /wake_up fails with "'list' object has no attribute 'zero_'" on hybrid-SWA / Mamba / DeltaNet models (SM120, NVFP4) — only Gemma-4 interleaved-SWA survives

| 字段 | 值 |
| --- | --- |
| Issue | [#41564](https://github.com/vllm-project/vllm/issues/41564) |
| 状态 | open |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | quantization |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: /wake_up fails with "'list' object has no attribute 'zero_'" on hybrid-SWA / Mamba / DeltaNet models (SM120, NVFP4) — only Gemma-4 interleaved-SWA survives

### Issue 正文摘录

`/wake_up` fails with `AttributeError: 'list' object has no attribute 'zero_'` on four architectures, while Gemma-4 succeeds. **Repro:** 1. Start a failing model (e.g., Qwen3.6-27B-NVFP4) with `--enable-sleep-mode` and `VLLM_SERVER_DEV_MODE=1`. 2. Confirm server readiness via `/health` (HTTP 200). 3. `curl -X POST http:// :8000/sleep?level=1` (HTTP 200, VRAM drops). 4. `curl -X POST http:// :8000/wake_up` → HTTP 500. 5. Engine logs show: `AttributeError: 'list' object has no attribute 'zero_'`. **Env:** - Hardware: 4× NVIDIA RTX PRO 6000 Blackwell (SM 12.0) - OS: Ubuntu 24.04, Driver 580 - Image: `vllm/vllm-openai:cu129-nightly` (digests `8b49cf3a37eb`, `a749a33d8d05`) - Quantization: `compressed-tensors` (NVFP4) - Flags: `--tensor-parallel-size 4`, `--gpu-memory-utilization 0.85` **Expected:** `/wake_up` returns HTTP 200 and inference resumes normally. **Actual:** HTTP 500 with `AttributeError: 'list' object has no attribute 'zero_'`.

## 现有链接修复摘要

#41602 [Bugfix] Fix /wake_up crash on hybrid models (Mamba/DeltaNet)

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: bject has no attribute 'zero_'" on hybrid-SWA / Mamba / DeltaNet models (SM120, NVFP4) — only Gemma-4 interleaved-SWA survives `/wake_up` fails with `AttributeError: 'list' object has no attribute 'zero_'` on four archi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: as no attribute 'zero_'" on hybrid-SWA / Mamba / DeltaNet models (SM120, NVFP4) — only Gemma-4 interleaved-SWA survives `/wake_up` fails with `AttributeError: 'list' object has no attribute 'zero_'` on four architecture...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 'list' object has no attribute 'zero_'" on hybrid-SWA / Mamba / DeltaNet models (SM120, NVFP4) — only Gemma-4 interleaved-SWA survives `/wake_up` fails with `AttributeError: 'list' object has no attribute 'zero_'` on fo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rontend_api;hardware_porting;model_support;quantization quantization env_dependency #41602 [Bugfix] Fix /wake_up crash on hybrid models (Mamba/DeltaNet) `/wake_up` fails with `AttributeError: 'list' object has no attrib...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: e 'zero_'" on hybrid-SWA / Mamba / DeltaNet models (SM120, NVFP4) — only Gemma-4 interleaved-SWA survives `/wake_up` fails with `AttributeError: 'list' object has no attribute 'zero_'` on four architectures, while Gemma...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41602](https://github.com/vllm-project/vllm/pull/41602) | closes_keyword | 0.95 | [Bugfix] Fix /wake_up crash on hybrid models (Mamba/DeltaNet) | Fixes #41564 ## Root Cause `init_fp8_kv_scales()` (called via `post_kv_cache_wake_up()` → `wake_up()`) iterates `self.kv_caches` and calls `.zero_()` on each entry, assuming ever |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
