# vllm-project/vllm#34641: [ROCm] Default VLLM_ROCM_USE_AITER_FP4BMM=True crashes on MI300X (gfx942)

| 字段 | 值 |
| --- | --- |
| Issue | [#34641](https://github.com/vllm-project/vllm/issues/34641) |
| 状态 | closed |
| 标签 | rocm;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;distributed_parallel;hardware_porting;quantization |
| 子分类 | runtime_err |
| Operator 关键词 | fp8;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [ROCm] Default VLLM_ROCM_USE_AITER_FP4BMM=True crashes on MI300X (gfx942)

### Issue 正文摘录

## Summary vLLM crashes on AMD MI300X/MI300A (gfx942) with default settings due to `VLLM_ROCM_USE_AITER_FP4BMM=True`. MI300X doesn't support FP4, but vLLM attempts to use it anyway. **Impact**: Affects ~90% of AMD GPU users (MI300X is most common) ## Environment - GPU: AMD MI300X (gfx942) - vLLM: v0.16.0rc2.dev151+g4453ba8d9 - ROCm: 7.1.1, AITER: 0.1.10.post2 ## Reproduce ```bash export VLLM_ROCM_USE_AITER=1 vllm serve deepseek-ai/DeepSeek-V3 --tensor-parallel-size 8 # Error: RuntimeError: MXFP4 quantization is not supported on gfx942 ``` ## Root Cause vLLM only checks env vars, not hardware capability: **vllm/envs.py:110** ```python VLLM_ROCM_USE_AITER_FP4BMM: bool = True # ⚠️ Wrong for MI300X! ``` **vllm/_aiter_ops.py:1001-1002** ```python def is_fp4bmm_enabled(cls) -> bool: return cls._AITER_ENABLED and cls._FP4BMM_ENABLED # ❌ No hardware check! ``` AITER library knows FP4 only works on gfx950 (MI325X/MI350X), but vLLM never queries this. ## Workaround ```bash export VLLM_ROCM_USE_AITER_FP4BMM=0 # Disable FP4 on MI300X vllm serve deepseek-ai/DeepSeek-V3 --kv-cache-dtype fp8 ``` ## Proposed Fix Add hardware detection to `vllm/_aiter_ops.py`: ## Timeline - Introduced: Commit 8c11...

## 现有链接修复摘要

#34647 [ROCm] Add hardware detection for FP4 BMM to prevent MI300X crashes | #35103 [Bugfix][Hardware][AMD] Gate FP4 BMM on gfx950 to fix MI300X crash | #39325 fix: Disable VLLM_ROCM_USE_AITER_FP4BMM by default to prevent crashes on MI300X

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [ROCm] Default VLLM_ROCM_USE_AITER_FP4BMM=True crashes on MI300X (gfx942) rocm;stale ## Summary vLLM crashes on AMD MI300X/MI300A (gfx942) with default settings due to `VLLM_ROCM_USE_AITER_FP4BMM=True`. MI300X doesn't s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [ROCm] Default VLLM_ROCM_USE_AITER_FP4BMM=True crashes on MI300X (gfx942) rocm;stale ## Summary vLLM crashes on AMD MI300X/MI300A (gfx942) with default settings due to `VLLM_ROCM_USE_AITER_FP4BMM=True`. MI300X doesn't su
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [ROCm] Default VLLM_ROCM_USE_AITER_FP4BMM=True crashes on MI300X (gfx942) rocm;stale ## Summary vLLM crashes on AMD MI300X/MI300A (gfx942) with default settings due to `VLLM_ROCM_USE_AITER_FP4BMM=True`. MI300X doesn't s...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: LLM: v0.16.0rc2.dev151+g4453ba8d9 - ROCm: 7.1.1, AITER: 0.1.10.post2 ## Reproduce ```bash export VLLM_ROCM_USE_AITER=1 vllm serve deepseek-ai/DeepSeek-V3 --tensor-parallel-size 8 # Error: RuntimeError: MXFP4 quantizatio...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: _parallel;hardware_porting;quantization fp8;quantization crash dtype;env_dependency #34647 [ROCm] Add hardware detection for FP4 BMM to prevent MI300X crashes | #35103 [Bugfix][Hardware][AMD] Gate FP4 BMM on gfx950 to f...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34647](https://github.com/vllm-project/vllm/pull/34647) | closes_keyword | 0.95 | [ROCm] Add hardware detection for FP4 BMM to prevent MI300X crashes | Fixes #34641 - Prevent vLLM crashes on AMD MI300X (gfx942) by adding hardware detection for FP4 BMM. **Problem**: vLLM crashes on MI300X with default settings because `VLLM_ROCM_U |
| [#35103](https://github.com/vllm-project/vllm/pull/35103) | closes_keyword | 0.95 | [Bugfix][Hardware][AMD] Gate FP4 BMM on gfx950 to fix MI300X crash | Fixes #34641 |
| [#39325](https://github.com/vllm-project/vllm/pull/39325) | closes_keyword | 0.95 | fix: Disable VLLM_ROCM_USE_AITER_FP4BMM by default to prevent crashes on MI300X | Fixes vllm-project/vllm#34641 The FP4 BMM kernel crashes on MI300X (gfx942). This fix changes the default value of VLLM_ROCM_USE_AITER_FP4BMM from True to False. Users who need F |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
