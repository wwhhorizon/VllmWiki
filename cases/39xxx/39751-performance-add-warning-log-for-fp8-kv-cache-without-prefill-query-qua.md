# vllm-project/vllm#39751: [Performance]: Add warning log for FP8 KV cache without prefill query quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#39751](https://github.com/vllm-project/vllm/issues/39751) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Add warning log for FP8 KV cache without prefill query quantization

### Issue 正文摘录

## Context When using `--kv-cache-dtype fp8` with MLA models (e.g. DeepSeek-R1), the prefill FMHA kernel dispatches `QkvBfloat16` by default. the FP8 variant (`QkvE4m3`) requires explicitly setting `use_prefill_query_quantization=true` in `--attention-config`, which is not easy discoverable. Per PR #31195 by @pavanimajety, this was intentionally gated because at short sequence lengths, the BF16 to FP8 cast overhead slight degrades end-to-end performance despite ~1.5x kernel-level improvement. **However, for **long-context prefill (128K+)**, the kernel time dominates and the FP8 path is significantly faster.** Our profiling on GB300 (DeepSeek-R1-FP4, PP=4, ISL=128K) shows: | Kernel Variant | Avg Latency | |---|---| | `fmhaSm103aKernel_QkvBfloat16...` (default) | 287 ms | | `fmhaSm103aKernel_QkvE4m3...` (FP8) | 225 ms | **This is a 1.28x speedup that users silently miss.** ## Short-Seq Benchmark To verify whether the cast overhead has improved since the original analysis (Dec 2025), we ran end-to-end benchmarks on GB300 with the following setup: - **Model**: DeepSeek-R1-0528-FP4 - **Parallelism**: DP=4 (matching Pavani's PR #31195 config, but we used `max-model-len=34816` to also te...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Performance]: Add warning log for FP8 KV cache without prefill query quantization performance ## Context When using `--kv-cache-dtype fp8` with MLA models (e.g. DeepSeek-R1), the prefill FMHA kernel dispatches `QkvBflo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: he kernel time dominates and the FP8 path is significantly faster.** Our profiling on GB300 (DeepSeek-R1-FP4, PP=4, ISL=128K) shows: | Kernel Variant | Avg Latency | |---|---| | `fmhaSm103aKernel_QkvBfloat16...` (defaul...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: P=4, ISL=128K) shows: | Kernel Variant | Avg Latency | |---|---| | `fmhaSm103aKernel_QkvBfloat16...` (default) | 287 ms | | `fmhaSm103aKernel_QkvE4m3...` (FP8) | 225 ms | **This is a 1.28x speedup that users silently mi...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Performance]: Add warning log for FP8 KV cache without prefill query quantization performance ## Context When using `--kv-cache-dtype fp8` with MLA models (e.g. DeepSeek-R1), the prefill FMHA kernel dispatches `QkvBflo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ation performance ## Context When using `--kv-cache-dtype fp8` with MLA models (e.g. DeepSeek-R1), the prefill FMHA kernel dispatches `QkvBfloat16` by default. the FP8 variant (`QkvE4m3`) requires explicitly setting `us...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
