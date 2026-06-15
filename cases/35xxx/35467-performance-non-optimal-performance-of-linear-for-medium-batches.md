# vllm-project/vllm#35467: [Performance]: non-optimal performance of `linear` for medium batches

| 字段 | 值 |
| --- | --- |
| Issue | [#35467](https://github.com/vllm-project/vllm/issues/35467) |
| 状态 | open |
| 标签 | performance;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;gemm;kernel;moe;quantization |
| 症状 | build_error;mismatch;nondeterministic;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Performance]: non-optimal performance of `linear` for medium batches

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I reported earlier about non-optimal performance of `linear` for small batch. Now, after analysis of Qwen3.5 for high throughput, I found a case where it is not optimal for batch=257 (in fact batch=272 due to CUDA graph padding). From the profile I see that the projection for GDN attention takes around 48.8 us, but there is a kernel configuration that achieves 34.1 us. E2E impact for best case on `Qwen3.5-397B` is around 1.4% The effort to add gemm_f16 to FlashInfer: https://github.com/flashinfer-ai/flashinfer/issues/1974 Below is the detailed report. --- # BF16 GEMM Benchmark: `in_proj_qkvz` for Qwen3.5-397B GDN Attention on B200 ## TL;DR Benchmarked the `in_proj_qkvz` BF16 GEMM `[272, 4096] x [4096, 14336]` on B200 across 26 configurations: PyTorch eager/compile/CUDAGraph, FlashInfer cuDNN/CUTLASS, and cublasLt with explicit tile selection in both TN and NN layouts. - **vLLM production** runs at **48.6 us** with a suboptimal nvjet kernel selected by cuBLAS auto-tuning. - **F.linear** (standalone) runs at **42.6 us** -- a different nvjet kernel, also not optimal. - **Best achievable with TN layout** (cublasLt 256x144, matching vLLM's weight...

## 现有链接修复摘要

#12 Implement preemption via recomputation & Refactor scheduling logic

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: shinfer-ai/flashinfer/issues/1974 Below is the detailed report. --- # BF16 GEMM Benchmark: `in_proj_qkvz` for Qwen3.5-397B GDN Attention on B200 ## TL;DR Benchmarked the `in_proj_qkvz` BF16 GEMM `[272, 4096] x [4096, 14...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: nce of `linear` for small batch. Now, after analysis of Qwen3.5 for high throughput, I found a case where it is not optimal for batch=257 (in fact batch=272 due to CUDA graph padding). From the profile I see that the pr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: est case on `Qwen3.5-397B` is around 1.4% The effort to add gemm_f16 to FlashInfer: https://github.com/flashinfer-ai/flashinfer/issues/1974 Below is the detailed report. --- # BF16 GEMM Benchmark: `in_proj_qkvz` for Qwe...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: aster than TN due to no transpose overhead. - cuBLAS kernel selection is non-deterministic across processes and leaves 16-20% on the table vs its own best tile. - `torch.compile(reduce-overhead/max-autotune)` adds ~75 u...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: , 4096] x [4096, 14336]` on B200 across 26 configurations: PyTorch eager/compile/CUDAGraph, FlashInfer cuDNN/CUTLASS, and cublasLt with explicit tile selection in both TN and NN layouts. - **vLLM production** runs at **...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | -select. 2. **cublas auto-selects the 7th-best tile** (128x136, rank #12 in tn). the heuristic leaves 16% performance on the table for tn and 15% for nn. 3. **nn layout is ~2 us f… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
