# vllm-project/vllm#43969: [Bug]: gpt-oss-120b MXFP4 MoE init OOM-killed on unified-memory ARM (DGX Spark / Jetson Thor)

| 字段 | 值 |
| --- | --- |
| Issue | [#43969](https://github.com/vllm-project/vllm/issues/43969) |
| 状态 | open |
| 标签 | cpu |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;kernel;moe;quantization |
| 症状 | crash;oom |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gpt-oss-120b MXFP4 MoE init OOM-killed on unified-memory ARM (DGX Spark / Jetson Thor)

### Issue 正文摘录

### Your current environment Environment collected from `python -m vllm.collect_env` inside the upstream-vllm validation containers (one Thor, one Spark). Both runs use the same `public.ecr.aws/q9t5s3a7/vllm-release-repo` aarch64 nightly. **Both hosts (validation container)** - OS: Ubuntu 22.04.5 LTS (aarch64) - Python: 3.12.13 - CUDA runtime (in container): 13.0.88 - PyTorch: 2.11.0+cu130 - vLLM: 0.21.1rc1.dev201+g1fe330398 (aarch64 nightly from `public.ecr.aws/q9t5s3a7/vllm-release-repo`) **Host A — Jetson AGX Thor** - GPU: NVIDIA Thor (SM 11.0), reported as iGPU on `tegra` kernel - Driver: 595.73 - CPU: 14 ARM cores - Kernel: Linux 6.8.12-1021-tegra - Unified memory architecture (no discrete VRAM) **Host B — DGX Spark GB10** - GPU: NVIDIA GB10 (SM 12.1) - Driver: 580.78 - CPU: 20 ARM cores - Kernel: Linux 6.11.0-1013-nvidia - Unified memory architecture (no discrete VRAM) ### Describe the bug Loading `openai/gpt-oss-120b` in MXFP4 with `vllm serve` on either of the two unified-memory ARM systems above is host-OOM-killed during MoE quantization-method initialization. The kernel sends SIGKILL (exit 137) to the `vllm serve` process before model weights finish materializing — this...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: — this is a Linux OOM-kill, not a CUDA OOM. The failure is 100% reproducible on both hosts with the upstream aarch64 nightly. The same workload at upstream commit `132765e3560659ff63ebd236203672e991b70e08` (the `v0.20.1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: rk). Both runs use the same `public.ecr.aws/q9t5s3a7/vllm-release-repo` aarch64 nightly. **Both hosts (validation container)** - OS: Ubuntu 22.04.5 LTS (aarch64) - Python: 3.12.13 - CUDA runtime (in container): 13.0.88...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: gpt-oss-120b MXFP4 MoE init OOM-killed on unified-memory ARM (DGX Spark / Jetson Thor) cpu ### Your current environment Environment collected from `python -m vllm.collect_env` inside the upstream-vllm validation...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: gpt-oss-120b MXFP4 MoE init OOM-killed on unified-memory ARM (DGX Spark / Jetson Thor) cpu ### Your current environment Environment collected from `python -m vllm.collect_env` inside the upstream-vllm validation...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: 1270 → 1498 → 1515 → 1683 across releases) are explained by *new sibling backends inserted before the MARLIN branch* — HUMMING, AITER_MXFP4_MXFP4, AITER_MXFP4_FP8, CPU — not by changes to MARLIN itself. In other words,...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
