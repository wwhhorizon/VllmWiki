# vllm-project/vllm#42906: [Bug]: vllm-openai:v0.19.1-cu130 / v0.16.0-cu130 docker images bundle pre-fix flashinfer (≤ 0.6.6), causing CUDA IMA on MoE FP8 decode

| 字段 | 值 |
| --- | --- |
| Issue | [#42906](https://github.com/vllm-project/vllm/issues/42906) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;fp8;kernel;moe;quantization;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm-openai:v0.19.1-cu130 / v0.16.0-cu130 docker images bundle pre-fix flashinfer (≤ 0.6.6), causing CUDA IMA on MoE FP8 decode

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## TL;DR `vllm/vllm-openai:v0.19.1-cu130` and `vllm/vllm-openai:v0.16.0-cu130` both ship a flashinfer wheel that **predates** the bounds-check fix [flashinfer-ai/flashinfer#2762](https://github.com/flashinfer-ai/flashinfer/pull/2762) (merged 2026-04-24, first released in **flashinfer 0.6.10**, 2026-05-04). As a result, the `FLASHINFER_CUTLASS` FP8 MoE backend — which vLLM picks by default for FP8 MoE models — hits a CUDA **`illegal memory access`** mid-decode. This is the exact crash reported in [#35706](https://github.com/vllm-project/vllm/issues/35706) (closed). The downstream code fix is in flashinfer main, but the images still bundle the pre-fix wheel. **Two requests**: 1. Could the next image rebuild bump the bundled `flashinfer-python` / `flashinfer-cubin` / `flashinfer-jit-cache` to `>= 0.6.10`? 2. Until then, would it be possible to mention this in the image `README` or `release notes` (or have vLLM emit a startup warning if it detects bundled `flashinfer The crash is caused by a bounds-check removal in flashinfer's bundled TRT-LLM `finalizeMoeRoutingKernel`, introduced in flashinfer **v0.5.3** (commit `20435b40`). When v...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: vllm-openai:v0.19.1-cu130 / v0.16.0-cu130 docker images bundle pre-fix flashinfer (≤ 0.6.6), causing CUDA IMA on MoE FP8 decode bug ### Your current environment ### 🐛 Describe the bug ## TL;DR `vllm/vllm-openai:v...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: : vllm-openai:v0.19.1-cu130 / v0.16.0-cu130 docker images bundle pre-fix flashinfer (≤ 0.6.6), causing CUDA IMA on MoE FP8 decode bug ### Your current environment ### 🐛 Describe the bug ## TL;DR `vllm/vllm-openai:v0.19....
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: 0 docker images bundle pre-fix flashinfer (≤ 0.6.6), causing CUDA IMA on MoE FP8 decode bug ### Your current environment ### 🐛 Describe the bug ## TL;DR `vllm/vllm-openai:v0.19.1-cu130` and `vllm/vllm-openai:v0.16.0-cu1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: v0.16.0-cu130 docker images bundle pre-fix flashinfer (≤ 0.6.6), causing CUDA IMA on MoE FP8 decode bug ### Your current environment ### 🐛 Describe the bug ## TL;DR `vllm/vllm-openai:v0.19.1-cu130` and `vllm/vllm-openai...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: After in-container pip upgrade to `flashinfer-python==0.6.11.post3` (latest stable), the same grep returns `1` — and the crash disappears. ## Workarounds we verified ### 1. `VLLM_USE_FLASHINFER_MOE_FP8=0` (recommended i...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
