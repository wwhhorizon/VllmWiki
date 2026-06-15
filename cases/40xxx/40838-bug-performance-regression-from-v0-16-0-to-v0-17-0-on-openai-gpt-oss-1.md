# vllm-project/vllm#40838: [Bug]: Performance regression from v0.16.0 to v0.17.0+ on openai/gpt-oss-120b

| 字段 | 值 |
| --- | --- |
| Issue | [#40838](https://github.com/vllm-project/vllm/issues/40838) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Performance regression from v0.16.0 to v0.17.0+ on openai/gpt-oss-120b

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary A significant performance regression was introduced in vLLM v0.17.0 and persists through v0.19.0. The regression **scales with concurrency** — ~8% throughput loss at concurrency 50, ~11% at concurrency 200, and **~16% at concurrency 300**. Per-token latency (TPOT) degrades by up to 20%. ## Setup - **Model:** `openai/gpt-oss-120b` - **Hardware:** H200 GPUs - **Tensor Parallelism:** TP=4 - **Versions tested:** v0.16.0, v0.17.0, v0.17.1, v0.18.0, v0.19.0 - **Concurrency:** 300 ## Benchmark Results | Version | measured rps | output_tok/s | total_tok/s | ttft_median (ms) | ttft_p95 (ms) | ttft_p999 (ms) | tpot_median (ms) | tpot_p95 (ms) | tpot_p99 (ms) | tpot_p999 (ms) | |---------|-------------|-------------|-------------|-------------------|---------------|-----------------|-------------------|---------------|---------------|-----------------| | **v0.16.0** | **15.4667** | **16055.10** | **32416.16** | 473.90 | 1434.60 | 4431.58 | **18.67** | **20.80** | **21.46** | **21.77** | | v0.17.0 | 12.6556 | 13305.99 | 26771.83 | 380.14 | 1285.32 | 2730.03 | 22.40 | 24.75 | 25.74 | 25.81 | | v0.17.1 | 13.1756 | 13340.97 | 27342.8...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: [Bug]: Performance regression from v0.16.0 to v0.17.0+ on openai/gpt-oss-120b bug ### Your current environment ### 🐛 Describe the bug ## Summary A significant performance regression was introduced in vLLM v0.17.0 and pe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: `openai/gpt-oss-120b` - **Hardware:** H200 GPUs - **Tensor Parallelism:** TP=4 - **Versions tested:** v0.16.0, v0.17.0, v0.17.1, v0.18.0, v0.19.0 - **Concurrency:** 300 ## Benchmark Results | Version | measured rps | ou...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Performance regression from v0.16.0 to v0.17.0+ on openai/gpt-oss-120b bug ### Your current environment ### 🐛 Describe the bug ## Summary A significant performance regression was introduced in vLLM v0.17.0 and pe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 120b` - **Hardware:** H200 GPUs - **Tensor Parallelism:** TP=4 - **Versions tested:** v0.16.0, v0.17.0, v0.17.1, v0.18.0, v0.19.0 - **Concurrency:** 300 ## Benchmark Results | Version | measured rps | output_tok/s | tot...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ntroduced in vLLM v0.17.0 and persists through v0.19.0. The regression **scales with concurrency** — ~8% throughput loss at concurrency 50, ~11% at concurrency 200, and **~16% at concurrency 300**. Per-token latency (TP...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
