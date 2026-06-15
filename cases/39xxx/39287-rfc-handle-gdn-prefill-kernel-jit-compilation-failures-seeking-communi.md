# vllm-project/vllm#39287: [RFC]: Handle GDN prefill kernel JIT compilation failures - seeking community input

| 字段 | 值 |
| --- | --- |
| Issue | [#39287](https://github.com/vllm-project/vllm/issues/39287) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;kernel;triton |
| 症状 | build_error;oom |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Handle GDN prefill kernel JIT compilation failures - seeking community input

### Issue 正文摘录

## Problem Summary **Symptom:** H100 users loading Qwen3.5/Qwen3-Next models experience OOM or hangs during FlashInfer GDN kernel JIT compilation, consuming 150-200GB RAM. **Root Cause:** Default compilation uses all CPU cores (64-128) with ~3GB per task. **Affected Users:** ~7% of H100 users (Qwen3.5 + no precompiled cubins). --- ## Deep Analysis ### Why Only H100? ``` GDN FlashInfer kernel requires Compute Capability 9.0+ (Hopper architecture) GPU | Compute Capability | Uses FlashInfer GDN? | Affected? -------------|-------------------|---------------------|---------- A100 | 8.0 | No (auto-fallback) | ❌ V100 | 7.0 | No | ❌ RTX 4090 | 8.9 | No | ❌ H100/H800 | 9.0 | Yes | ✅ B200 | 9.0+ | Yes | ✅ RTX 5090 | 9.0+ | Yes | ✅ ``` **A100 users are safe** — they automatically fall back to Triton/FLA and never trigger FlashInfer GDN. ### Memory Consumption Formula ``` Compilation Memory = MAX_JOBS × ~3GB per task Default: MAX_JOBS = CPU cores (64-128 on servers) Typical: 64 cores × 3GB = 192GB 128 cores × 3GB = 384GB Total System Memory Needed: - Compilation: 192GB - Model (72B): 140GB - KV Cache: 20-50GB - System/Other: 10-20GB ───────────────────────── Total: ~362-402GB ``` ### Why This...

## 现有链接修复摘要

#39381 [Core]Fix/handle kernel failures

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 9: failures - seeking community input RFC ## Problem Summary **Symptom:** H100 users loading Qwen3.5/Qwen3-Next models experience OOM or hangs during FlashInfer GDN kernel JIT compilation, consuming 150-200GB RAM. **Root C...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: h ~3GB per task. **Affected Users:** ~7% of H100 users (Qwen3.5 + no precompiled cubins). --- ## Deep Analysis ### Why Only H100? ``` GDN FlashInfer kernel requires Compute Capability 9.0+ (Hopper architecture) GPU | Co...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: 0 users loading Qwen3.5/Qwen3-Next models experience OOM or hangs during FlashInfer GDN kernel JIT compilation, consuming 150-200GB RAM. **Root Cause:** Default compilation uses all CPU cores (64-128) with ~3GB per task...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: community input RFC ## Problem Summary **Symptom:** H100 users loading Qwen3.5/Qwen3-Next models experience OOM or hangs during FlashInfer GDN kernel JIT compilation, consuming 150-200GB RAM. **Root Cause:** Default com...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ry **Symptom:** H100 users loading Qwen3.5/Qwen3-Next models experience OOM or hangs during FlashInfer GDN kernel JIT compilation, consuming 150-200GB RAM. **Root Cause:** Default compilation uses all CPU cores (64-128)...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39381](https://github.com/vllm-project/vllm/pull/39381) | closes_keyword | 0.95 | [Core]Fix/handle kernel failures | Fixes #39287 ## Purpose ## Test Plan ## Test Result --- <details> <summary> Essential Elements of an Effective PR Description Checklist </summary> - [ ] The purp |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
