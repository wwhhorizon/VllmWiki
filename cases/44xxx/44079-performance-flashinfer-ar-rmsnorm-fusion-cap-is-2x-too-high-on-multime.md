# vllm-project/vllm#44079: [Performance]: FlashInfer AR+RMSNorm fusion cap is ~2x too high on multimem NVLink Hopper (TP8): it displaces the faster multimem all-reduce in the 256KB-512KB band

| 字段 | 值 |
| --- | --- |
| Issue | [#44079](https://github.com/vllm-project/vllm/issues/44079) |
| 状态 | open |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;distributed_parallel;hardware_porting |
| 子分类 | latency_reg |
| Operator 关键词 | activation;cuda;kernel;operator |
| 症状 | slowdown |
| 根因提示 | dtype;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Performance]: FlashInfer AR+RMSNorm fusion cap is ~2x too high on multimem NVLink Hopper (TP8): it displaces the faster multimem all-reduce in the 256KB-512KB band

### Issue 正文摘录

### Proposal to improve performance ## Summary On a multimem/NVSwitch sm90 node at TP8 (default settings), `AllReduceFusionPass` fuses `all_reduce + residual + RMSNorm` into flashinfer's one-shot trtllm AR whenever the message is below `FI_ALLREDUCE_FUSION_MAX_SIZE_MB[90][8] = 0.5 MB`. But above **256 KB** the *unfused* all-reduce uses vLLM's fast `multimem_all_reduce` (NVLink multicast), which is faster than flashinfer's one-shot AR. So in the **256 KB–512 KB** band the pass trades the fast `multimem` AR for a slower fused AR — a net regression: - **−1.9 to −4.3 µs/op** (microbench, CUDA-graph timed) - **−3.4 % / −7.4 % decode throughput at batch 96 / 128** (Qwen3-30B-A3B, TP8) Fix: cap the fusion at the size where the fast unfused AR takes over (256 KB here), gated on multimem availability. ## Environment 8×H200 (sm_90), NVLink/NVSwitch, TP8, bf16. vLLM `0.1.dev1916`, flashinfer `0.6.11.post2`. Defaults `VLLM_ALLREDUCE_USE_SYMM_MEM=1`, `VLLM_USE_NCCL_SYMM_MEM=0`, `VLLM_ALLREDUCE_USE_FLASHINFER=0`. ## Root cause `cuda_communicator.all_reduce` sends the unfused AR to vLLM's custom one-shot kernel below `CUSTOM_ALL_REDUCE_MAX_SIZES["9.0"][8] = 262144 B` and to `multimem_all_reduce`...

## 现有链接修复摘要

#37756 [Perf] Add SM 10.3 (B300/GB300) all-reduce communicator tuning | #42409 [ROCm] Widen AITER fused AR RMSNorm 1-stage gate | #44080 [Perf] Gate AR+RMSNorm fusion cap on the active fast all-reduce threshold

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ce]: FlashInfer AR+RMSNorm fusion cap is ~2x too high on multimem NVLink Hopper (TP8): it displaces the faster multimem all-reduce in the 256KB-512KB band performance ### Proposal to improve performance ## Summary On a...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Performance]: FlashInfer AR+RMSNorm fusion cap is ~2x too high on multimem NVLink Hopper (TP8): it displaces the faster multimem all-reduce in the 256KB-512KB band performance ### Proposal to improve performance ## Sum...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: and the pass trades the fast `multimem` AR for a slower fused AR — a net regression: - **−1.9 to −4.3 µs/op** (microbench, CUDA-graph timed) - **−3.4 % / −7.4 % decode throughput at batch 96 / 128** (Qwen3-30B-A3B, TP8)...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ormance]: FlashInfer AR+RMSNorm fusion cap is ~2x too high on multimem NVLink Hopper (TP8): it displaces the faster multimem all-reduce in the 256KB-512KB band performance ### Proposal to improve performance ## Summary...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: imem availability. ## Environment 8×H200 (sm_90), NVLink/NVSwitch, TP8, bf16. vLLM `0.1.dev1916`, flashinfer `0.6.11.post2`. Defaults `VLLM_ALLREDUCE_USE_SYMM_MEM=1`, `VLLM_USE_NCCL_SYMM_MEM=0`, `VLLM_ALLREDUCE_USE_FLAS...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37756](https://github.com/vllm-project/vllm/pull/37756) | mentioned | 0.45 | [Perf] Add SM 10.3 (B300/GB300) all-reduce communicator tuning | haped. thresholds are config-overridable (#23722). precedent: #42409, #37756. ## config caveat with the non-default `vllm_use_nccl_symm_mem=1`, nccl-symm-mem wins from ~128 kib, m… |
| [#42409](https://github.com/vllm-project/vllm/pull/42409) | mentioned | 0.45 | [ROCm] Widen AITER fused AR RMSNorm 1-stage gate | yte/mb-shaped. thresholds are config-overridable (#23722). precedent: #42409, #37756. ## config caveat with the non-default `vllm_use_nccl_symm_mem=1`, nccl-symm-mem wins from ~12… |
| [#44080](https://github.com/vllm-project/vllm/pull/44080) | mentioned | 0.6 | [Perf] Gate AR+RMSNorm fusion cap on the active fast all-reduce threshold | mm-mem/multimem availability. No change on non-multimem nodes. See #44079 for full analysis. Net regression in 256KB-512KB: -1.9..-4.3us/op; -3.4%/-7.4% decode tok/s at B=96/128 (… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
