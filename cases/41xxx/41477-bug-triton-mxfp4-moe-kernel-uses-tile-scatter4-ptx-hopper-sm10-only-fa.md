# vllm-project/vllm#41477: [Bug]: Triton MXFP4 MoE kernel uses .tile::scatter4 PTX (Hopper/SM10 only) — fails on SM 12.1 (GB10/DGX Spark); Marlin fallback hits #37030

| 字段 | 值 |
| --- | --- |
| Issue | [#41477](https://github.com/vllm-project/vllm/issues/41477) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;moe;quantization;triton |
| 症状 | crash;mismatch;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Triton MXFP4 MoE kernel uses .tile::scatter4 PTX (Hopper/SM10 only) — fails on SM 12.1 (GB10/DGX Spark); Marlin fallback hits #37030

### Issue 正文摘录

### Your current environment - GPU: NVIDIA **GB10 (DGX Spark)** — SM 12.1 / sm_121a, 128 GB unified memory - Architecture: Grace Blackwell (consumer/edge variant) - Driver 580.142, CUDA 13.0, Ubuntu 24.04 ARM64 - vLLM image: `vllm/vllm-openai:nightly-aarch64` (v0.20.1rc1.dev91+ga749a33d8, 2026-04-30); same behavior on `v0.20.0` ### 🐛 Describe the bug Serving `openai/gpt-oss-120b` with native MXFP4 on **GB10 / DGX Spark (SM 12.1)** has no working `--moe-backend`: | backend | outcome | |---|---| | `marlin` (default) | Runs but emits broken first Harmony token → `content: null`, `reasoning: null` (#37030) | | `triton` (after patching capability gate) | `ptxas error: Feature '.tile::scatter4' not supported on .target 'sm_121a'` | | `flashinfer_cutlass` | Quant scheme mismatch (`u8 / GroupShape(1,32)` not supported) | | `flashinfer_trtllm` | "kernel does not support current device cuda" | | `flashinfer_cutedsl` | Engine init failure | | `deep_gemm` | "kernel does not support current device cuda" | | `emulation` | Works, but ≤5 tok/s | Both `OAITritonExperts` and `UnfusedOAITritonExperts` call `matmul_ogs` from `triton_kernels`, which is JIT-compiled with `.tile::scatter4` PTX. **That i...

## 现有链接修复摘要

#31607 [Bugfix] Add SM 12.1 support + Fix GPT-OSS Harmony garbled reasoning and HarmonyError crashes | #31740 feat: Add SM121/GB10 (DGX Spark) Blackwell-class GPU support | #34822 [Bugfix] Add is_blackwell_class() for SM121/GB10 DGX Spark support | #40923 [Kernel] Marlin MoE: include SM 12.x in default arch list | #41028 [Kernel] OAITritonExperts MXFP4: include SM 12.x in supported device range

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: Triton MXFP4 MoE kernel uses .tile::scatter4 PTX (Hopper/SM10 only) — fails on SM 12.1 (GB10/DGX Spark); Marlin fallback hits #37030 ### Your current environment - GPU: NVIDIA **GB10 (DGX Spark)** — SM 12.1 / sm_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Bug]: Triton MXFP4 MoE kernel uses .tile::scatter4 PTX (Hopper/SM10 only) — fails on SM 12.1 (GB10/DGX Spark); Marlin fallback hits #37030 ### Your current environment - GPU: NVIDIA **GB10 (DGX Spark)** — SM 12.1 / sm_...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: [Bug]: Triton MXFP4 MoE kernel uses .tile::scatter4 PTX (Hopper/SM10 only) — fails on SM 12.1 (GB10/DGX Spark); Marlin fallback hits #37030 ### Your current environment - GPU: NVIDIA **GB10 (DGX Spark)** — SM 12.1 / sm_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: dOAITritonExperts` call `matmul_ogs` from `triton_kernels`, which is JIT-compiled with `.tile::scatter4` PTX. **That instruction is a TMA scatter feature (Hopper SM 9.x / Blackwell datacenter SM 10.x) — it is _not_ part...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 30); same behavior on `v0.20.0` ### 🐛 Describe the bug Serving `openai/gpt-oss-120b` with native MXFP4 on **GB10 / DGX Spark (SM 12.1)** has no working `--moe-backend`: | backend | outcome | |---|---| | `marlin` (defaul...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31607](https://github.com/vllm-project/vllm/pull/31607) | mentioned | 0.45 | [Bugfix] Add SM 12.1 support + Fix GPT-OSS Harmony garbled reasoning and HarmonyError crashes | marlin null content on sm 12.1 — the fallback we currently land on) - #31607 (try/except harmonyerror; turns crash into empty response, doesn't fix kernel output) - #31740 (sm121/… |
| [#31740](https://github.com/vllm-project/vllm/pull/31740) | mentioned | 0.45 | feat: Add SM121/GB10 (DGX Spark) Blackwell-class GPU support | yerror; turns crash into empty response, doesn't fix kernel output) - #31740 (sm121/gb10 platform support, needs-rebase, fp8 focus, no mxfp4 moe kernel) - #41028, #40923, #34822 (… |
| [#34822](https://github.com/vllm-project/vllm/pull/34822) | mentioned | 0.45 | [Bugfix] Add is_blackwell_class() for SM121/GB10 DGX Spark support | port, needs-rebase, fp8 focus, no mxfp4 moe kernel) - #41028, #40923, #34822 (device-range extensions; helpful but don't fix tma / marlin) ### before submitting - [x] searched exi… |
| [#40923](https://github.com/vllm-project/vllm/pull/40923) | mentioned | 0.45 | [Kernel] Marlin MoE: include SM 12.x in default arch list | form support, needs-rebase, fp8 focus, no mxfp4 moe kernel) - #41028, #40923, #34822 (device-range extensions; helpful but don't fix tma / marlin) ### before submitting - [x] sear… |
| [#41028](https://github.com/vllm-project/vllm/pull/41028) | mentioned | 0.45 | [Kernel] OAITritonExperts MXFP4: include SM 12.x in supported device range | b10 platform support, needs-rebase, fp8 focus, no mxfp4 moe kernel) - #41028, #40923, #34822 (device-range extensions; helpful but don't fix tma / marlin) ### before submitting -… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
