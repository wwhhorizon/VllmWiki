# vllm-project/vllm#36598: [Bug]: Triton autotuner OOM on Qwen3.5/Qwen3-Next GDN layers (non-SM90 GPUs)

| 字段 | 值 |
| --- | --- |
| Issue | [#36598](https://github.com/vllm-project/vllm/issues/36598) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Triton autotuner OOM on Qwen3.5/Qwen3-Next GDN layers (non-SM90 GPUs)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Description Running Qwen3.5-9B with vLLM on non-SM90 GPUs (e.g. RTX 5090, SM120) causes a Triton `out of memory` error during the first inference request. The error originates from the Triton autotuner trying to benchmark kernel configurations for GDN (Gated Delta Net) linear attention layers after vLLM has already allocated most GPU memory for KV cache. **Root cause:** During V1 profile runs, `_forward_core` in `Qwen3NextGatedDeltaNet` returns early when `attn_metadata is None` ([qwen3_next.py#L640-L642](https://github.com/vllm-project/vllm/blob/179547d62/vllm/model_executor/models/qwen3_next.py#L640-L642)), so the Triton-autotuned kernels (`solve_tril`, `chunk_scaled_dot_kkt`, etc.) are never invoked during profiling. After profiling, vLLM allocates KV cache using most of the remaining GPU memory. When the first real inference triggers the Triton autotuner, it OOMs because there is insufficient memory left for benchmarking. This only affects GPUs using the Triton-based `forward_native` path (non-SM90). SM90 GPUs (H100/H200) use the FlashInfer `forward_cuda` path which has no Triton autotuner. ### Reproduction ```python from...

## 现有链接修复摘要

#36599 [Bugfix] Warm up Triton autotuner for GDN layers during V1 profiling | #43044 [Core] Add shmem-aware autotune pruner for non-H100 Triton kernels | #43047 [Core] Add shmem-aware autotune pruner for non-H100 Triton kernels

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Triton autotuner OOM on Qwen3.5/Qwen3-Next GDN layers (non-SM90 GPUs) bug ### Your current environment ### 🐛 Describe the bug ### Description Running Qwen3.5-9B with vLLM on non-SM90 GPUs (e.g. RTX 5090, SM120) c...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: inference triggers the Triton autotuner, it OOMs because there is insufficient memory left for benchmarking. This only affects GPUs using the Triton-based `forward_native` path (non-SM90). SM90 GPUs (H100/H200) use the...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: erence request. The error originates from the Triton autotuner trying to benchmark kernel configurations for GDN (Gated Delta Net) linear attention layers after vLLM has already allocated most GPU memory for KV cache. *...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: Triton autotuner OOM on Qwen3.5/Qwen3-Next GDN layers (non-SM90 GPUs) bug ### Your current environment ### 🐛 Describe the bug ### Description Running Qwen3.5-9B with vLLM on non-SM90 GPUs (e.g. RTX 5090, SM120) c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Triton autotuner OOM on Qwen3.5/Qwen3-Next GDN layers (non-SM90 GPUs) bug ### Your current environment ### 🐛 Describe the bug ### Description Running Qwen3.5-9B with vLLM on non-SM90 GPUs (e.g. RTX 5090, SM120) c...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36599](https://github.com/vllm-project/vllm/pull/36599) | closes_keyword | 0.95 | [Bugfix] Warm up Triton autotuner for GDN layers during V1 profiling | Fix Triton autotuner OOM for Qwen3.5 / Qwen3-Next models with Gated Delta Net (GDN) linear attention layers. As is mentioned in #36598, during V1 profile runs, `_forward_core` in |
| [#43044](https://github.com/vllm-project/vllm/pull/43044) | closes_keyword | 0.95 | [Core] Add shmem-aware autotune pruner for non-H100 Triton kernels | closes #36598 reproducer end-to-end) Validated on RTX PRO 6000 TP=4 (SM_120) after this PR's helper + chunk_delta_h wiring landed: * **Cold-load succeeded cleanly.** No `OutOfRes |
| [#43047](https://github.com/vllm-project/vllm/pull/43047) | closes_keyword | 0.95 | [Core] Add shmem-aware autotune pruner for non-H100 Triton kernels | closes #36598 reproducer end-to-end) Validated on RTX PRO 6000 TP=4 (SM_120) after this PR's helper + chunk_delta_h wiring landed: * **Cold-load succeeded cleanly.** No `OutOfRes |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
