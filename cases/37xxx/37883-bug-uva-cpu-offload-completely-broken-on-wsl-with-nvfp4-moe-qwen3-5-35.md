# vllm-project/vllm#37883: [Bug] UVA CPU offload completely broken on WSL with NVFP4 MoE (Qwen3.5-35B-A3B): three distinct crashes across all parameter combinations

| 字段 | 值 |
| --- | --- |
| Issue | [#37883](https://github.com/vllm-project/vllm/issues/37883) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;gemm;kernel;moe;operator;quantization |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] UVA CPU offload completely broken on WSL with NVFP4 MoE (Qwen3.5-35B-A3B): three distinct crashes across all parameter combinations

### Issue 正文摘录

### Current environment - vLLM version: 0.18.0-cu130 (also reproduced on 0.17.1-cu130) - GPU: NVIDIA GeForce RTX 5090D 32GB (SM120, consumer Blackwell) - Host OS: Windows 11 + Docker Desktop (WSL2 backend) - Container runtime: Docker with NVIDIA GPU passthrough - Model: [Sehyo/Qwen3.5-35B-A3B-NVFP4](https://huggingface.co/Sehyo/Qwen3.5-35B-A3B-NVFP4) (compressed-tensors / NVFP4 quantization) - NVFP4 GEMM backend: MARLIN (on 0.17.1), FLASHINFER_CUTLASS (on 0.18.0) - Note from vLLM startup log: "Using 'pin_memory=False' as WSL is detected." ### 🐛 Describe the bug Attempting to use --cpu-offload-gb with --cpu-offload-params=experts on a NVFP4-quantized MoE model under WSL results in three distinct fatal crashes depending on the parameter combination. No combination of workarounds has produced a working configuration. All three crashes occur during profile_run() at startup, before the engine is ready to serve requests. ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Crash 1 — Dynamo cannot trace setattr (v0.18.0, compile mode) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Config: --cpu-offload-gb=4 --cpu-offload-params=experts (no --enforce-eager) Error: torch._dynamo.exc.Unsupported: Failed to t...

## 现有链接修复摘要

#41496 [Bug Fix] Allow pinned memory for WSL2 | #43453 [Offloader] Skip per-tensor scale parameters from CPU offload

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: es across all parameter combinations bug ### Current environment - vLLM version: 0.18.0-cu130 (also reproduced on 0.17.1-cu130) - GPU: NVIDIA GeForce RTX 5090D 32GB (SM120, consumer Blackwell) - Host OS: Windows 11 + Do...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: on: 0.18.0-cu130 (also reproduced on 0.17.1-cu130) - GPU: NVIDIA GeForce RTX 5090D 32GB (SM120, consumer Blackwell) - Host OS: Windows 11 + Docker Desktop (WSL2 backend) - Container runtime: Docker with NVIDIA GPU passt...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: (SM120, consumer Blackwell) - Host OS: Windows 11 + Docker Desktop (WSL2 backend) - Container runtime: Docker with NVIDIA GPU passthrough - Model: [Sehyo/Qwen3.5-35B-A3B-NVFP4](https://huggingface.co/Sehyo/Qwen3.5-35B-A...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug] UVA CPU offload completely broken on WSL with NVFP4 MoE (Qwen3.5-35B-A3B): three distinct crashes across all parameter combinations bug ### Current environment - vLLM version: 0.18.0-cu130 (also reproduced on 0.17...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug] UVA CPU offload completely broken on WSL with NVFP4 MoE (Qwen3.5-35B-A3B): three distinct crashes across all parameter combinations bug ### Current environment - vLLM version: 0.18.0-cu130 (also reproduced on 0.17...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41496](https://github.com/vllm-project/vllm/pull/41496) | mentioned | 0.6 | [Bug Fix] Allow pinned memory for WSL2 | SL2. This PR improves WSL2 support and potentially addresses issue #37883 ## Test Plan <details> <summary>Use the new test to verify no perf regression is introduced as a result |
| [#43453](https://github.com/vllm-project/vllm/pull/43453) | mentioned | 0.6 | [Offloader] Skip per-tensor scale parameters from CPU offload | a young adventurer named Alex..." ``` ## Related (not duplicate) - #37883 — bug report; this PR closes **Crash 2**. Crash 3 is addressed by #41496. - #41496 — enables pinned memor… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
