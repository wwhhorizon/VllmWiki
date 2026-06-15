# vllm-project/vllm#44209: [Bug]: Non-deterministic KV-cache reservation on hybrid GDN model (Qwen3.6) → CUDA-graph capture OOMs after /health passes → restart crash-loop (native full RTX 5090 / sm120)

| 字段 | 值 |
| --- | --- |
| Issue | [#44209](https://github.com/vllm-project/vllm/issues/44209) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;quantization |
| 症状 | build_error;crash;nondeterministic;oom |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Non-deterministic KV-cache reservation on hybrid GDN model (Qwen3.6) → CUDA-graph capture OOMs after /health passes → restart crash-loop (native full RTX 5090 / sm120)

### Issue 正文摘录

# [Bug]: Non-deterministic KV-cache reservation on a hybrid GDN model (Qwen3.6) → CUDA-graph capture OOMs *after* `/health` passes → restart crash-loop (native full RTX 5090 / sm120) ## Summary On a **full, non-sliced, native-Linux** RTX 5090 (sm_120), serving a hybrid GDN+attention model (Qwen3.6-35B-A3B, 30 GatedDeltaNet + 10 full-attention layers, AutoRound int4 → INC/gptq-Marlin, fp8 KV), `determine_available_memory()` produces a **non-deterministic KV-cache pool size across byte-for-byte identical cold boots**. The CUDA-graph capture reserve is not deterministically accounted for, so some boots size the KV pool too large and then **OOM during CUDA-graph capture**. Critically, **capture runs *after* the server reports `/health` 200**, so an over-sized boot passes its healthcheck, *then* dies in capture. With `restart: unless-stopped` (or any orchestrator that trusts the healthcheck) this becomes a **silent crash-loop of a container that already looked healthy**. There is a clean built-in workaround (`--kv-cache-memory-bytes` + capped `cudagraph_capture_sizes` + `cudagraph_mode=PIECEWISE`), but it forfeits the auto-sizing that `--gpu-memory-utilization` is supposed to provide....

## 现有链接修复摘要

#34571 [Bugfix] Cap FULL decode cudagraph sizes for Mamba/hybrid models (#34094)

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: (Qwen3.6-35B-A3B, 30 GatedDeltaNet + 10 full-attention layers, AutoRound int4 → INC/gptq-Marlin, fp8 KV), `determine_available_memory()` produces a **non-deterministic KV-cache pool size across byte-for-byte identical c...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 5: [Bug]: Non-deterministic KV-cache reservation on hybrid GDN model (Qwen3.6) → CUDA-graph capture OOMs after /health passes → restart crash-loop (native full RTX 5090 / sm120) # [Bug]: Non-deterministic KV-cache reservat...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: A RTX 5090, 32 GiB, sm_120 (Blackwell) — **full card, no MIG/MPS/HAMi slicing, native Linux (no WSL2)** - **vLLM:** reproduced on `v0.22.0` and on nightly **`v0.22.1rc1.dev22+g3fd9d2d35`** (commit `3fd9d2d35`) - **Image...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: : Non-deterministic KV-cache reservation on hybrid GDN model (Qwen3.6) → CUDA-graph capture OOMs after /health passes → restart crash-loop (native full RTX 5090 / sm120) # [Bug]: Non-deterministic KV-cache reservation o...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: Non-deterministic KV-cache reservation on hybrid GDN model (Qwen3.6) → CUDA-graph capture OOMs after /health passes → restart crash-loop (native full RTX 5090 / sm120) # [Bug]: Non-deterministic KV-cache reservat...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34571](https://github.com/vllm-project/vllm/pull/34571) | mentioned | 0.45 | [Bugfix] Cap FULL decode cudagraph sizes for Mamba/hybrid models (#34094) | r overhead; native linux is fine there. this is **native linux**. - **#34571 / #34094** (cap full decode cudagraph sizes for mamba/hybrid) — related and partially mitigating (capp… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
