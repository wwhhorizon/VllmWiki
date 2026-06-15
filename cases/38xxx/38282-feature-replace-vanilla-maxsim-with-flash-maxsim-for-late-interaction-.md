# vllm-project/vllm#38282: [Feature]: Replace vanilla MaxSim with flash-maxsim for late-interaction scoring

| 字段 | 值 |
| --- | --- |
| Issue | [#38282](https://github.com/vllm-project/vllm/issues/38282) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | kernel;quantization;triton |
| 症状 | build_error;oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Replace vanilla MaxSim with flash-maxsim for late-interaction scoring

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Replace vanilla MaxSim with flash-maxsim for late-interaction scoring The current `compute_maxsim_scores` in `vllm/v1/pool/late_interaction.py` has three performance bottlenecks: 1. **Python for-loop padding** — copies embeddings one-by-one into padded tensors (~84% of scoring time) 2. **Full similarity matrix in HBM** — materializes `[batch, Lq, Ld]` tensor (peaks at 549 MB, OOMs at scale) 3. **Serial mini-batching** — `max_score_matrix_elements=64M` cap forces up to 157 sequential batches **Proposal:** Replace with [flash-maxsim](https://github.com/roipony/flash-maxsim), a fused Triton kernel that computes MaxSim via IO-aware tiling in SRAM. Never materializes the similarity matrix — O(1) memory. No `max_score_matrix_elements` cap needed — handles arbitrarily large batches without OOM or mini-batching. ### Benchmarks (exact `compute_maxsim_scores` function, A100 40GB) | Config | Vanilla | Flash-MaxSim | Speedup | |--------|---------|-------------|---------| | Serving pairs N=64 | 0.377 ms | 0.045 ms | **8.3×** | | Rerank B=1,000 | 4.82 ms | 0.22 ms | **22×** | | Rerank B=10,000 | 48.1 ms | 2.22 ms | **22×** | | Memory | Vanilla | Flash-...

## 现有链接修复摘要

#40337 [Perf] Integrate flash-maxsim Triton kernels for late-interaction scoring

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 10K, Lq=1024, Ld=1024 | 39.1 GB → **OOM** | **0 MB** ✓ | Numerical precision: flash-maxsim uses FP32 accumulation → **1000× more precise** than the current FP16 bmm path. ### Integration approach The kernel source can b...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: MB** | | B=10K, Lq=1024, Ld=1024 | 39.1 GB → **OOM** | **0 MB** ✓ | Numerical precision: flash-maxsim uses FP32 accumulation → **1000× more precise** than the current FP16 bmm path. ### Integration approach The kernel s...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: HBM** — materializes `[batch, Lq, Ld]` tensor (peaks at 549 MB, OOMs at scale) 3. **Serial mini-batching** — `max_score_matrix_elements=64M` cap forces up to 157 sequential batches **Proposal:** Replace with [flash-maxs...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ini-batching. ### Benchmarks (exact `compute_maxsim_scores` function, A100 40GB) | Config | Vanilla | Flash-MaxSim | Speedup | |--------|---------|-------------|---------| | Serving pairs N=64 | 0.377 ms | 0.045 ms | **...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: handles arbitrarily large batches without OOM or mini-batching. ### Benchmarks (exact `compute_maxsim_scores` function, A100 40GB) | Config | Vanilla | Flash-MaxSim | Speedup | |--------|---------|-------------|--------...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40337](https://github.com/vllm-project/vllm/pull/40337) | mentioned | 0.6 | [Perf] Integrate flash-maxsim Triton kernels for late-interaction scoring | esses feature request #38282. ## Why this isn't a duplicate - Issue #38282 explicitly asks for this integration; no other open PR addresses it (searched `is:pr is:open flash maxsi… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
