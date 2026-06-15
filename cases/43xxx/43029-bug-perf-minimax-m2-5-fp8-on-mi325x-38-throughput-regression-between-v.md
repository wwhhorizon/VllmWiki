# vllm-project/vllm#43029: [Bug][Perf] MiniMax-M2.5 FP8 on MI325X — ~38% throughput regression between vLLM ROCm v0.18.0 and v0.21.0

| 字段 | 值 |
| --- | --- |
| Issue | [#43029](https://github.com/vllm-project/vllm/issues/43029) |
| 状态 | closed |
| 标签 | rocm |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | hardware_porting;moe;quantization |
| 子分类 | throughput |
| Operator 关键词 | fp8;moe |
| 症状 | slowdown |
| 根因提示 | dtype |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][Perf] MiniMax-M2.5 FP8 on MI325X — ~38% throughput regression between vLLM ROCm v0.18.0 and v0.21.0

### Issue 正文摘录

### Human hi @hongxiayang +viz @powderluv @chunfangamd @andyluo7 minimax is regression on mi325 a lot, can u take a look? thanks Live: https://inferencex.semianalysis.com/inference?g_model=MiniMax-M2.5&g_rundate=2026-05-18&i_gpus=mi325x_vllm&i_dstart=2026-03-29&i_dend=2026-05-18&i_prec=fp8 ### AI Summary We're observing a large throughput regression for **MiniMax-M2.5 (FP8)** on **AMD MI325X** between vLLM ROCm **v0.18.0** and **v0.21.0**. | Date | vLLM ROCm | Token Throughput / GPU @ 35 tok/s/user | InferenceX run | |---|---|---|---| | 2026-03-29 | **v0.18.0** | **~2,600 tok/s/gpu** (peak) | commit [`d43805f`](https://github.com/SemiAnalysisAI/InferenceX/commit/d43805fc3417ee83e42c0e4567d0d7fdcfad3a3b) · [Actions run 23700855432](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/23700855432) | | 2026-05-18 | **v0.21.0** | **~1,600 tok/s/gpu** | commit [`a0f295e`](https://github.com/SemiAnalysisAI/InferenceX/commit/a0f295eec916dd280415cbc837483539b5bdd402) · [Actions run 26062952448](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/26062952448) | **Net regression: ~−38% (≈1,000 tok/s/gpu absolute) from peak to current head.** The drop is not a single cliff at the...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug][Perf] MiniMax-M2.5 FP8 on MI325X — ~38% throughput regression between vLLM ROCm v0.18.0 and v0.21.0 rocm ### Human hi @hongxiayang +viz @powderluv @chunfangamd @andyluo7 minimax is regression on mi325 a lot, can u...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug][Perf] MiniMax-M2.5 FP8 on MI325X — ~38% throughput regression between vLLM ROCm v0.18.0 and v0.21.0 rocm ### Human hi @hongxiayang +viz @powderluv @chunfangamd @andyluo7 minimax is regression on mi325 a lot, can u...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rf] MiniMax-M2.5 FP8 on MI325X — ~38% throughput regression between vLLM ROCm v0.18.0 and v0.21.0 rocm ### Human hi @hongxiayang +viz @powderluv @chunfangamd @andyluo7 minimax is regression on mi325 a lot, can u take a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ke a look? thanks Live: https://inferencex.semianalysis.com/inference?g_model=MiniMax-M2.5&g_rundate=2026-05-18&i_gpus=mi325x_vllm&i_dstart=2026-03-29&i_dend=2026-05-18&i_prec=fp8 ### AI Summary We're observing a large...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: eleases/tag/v0.21.0) (`ad7125a`, 2026-05-15) that progressively degraded MoE/FP8 perf on gfx942 (MI325X). Range to bisect: [`bcf2be9...ad7125a`](https://github.com/vllm-project/vllm/compare/v0.18.0...v0.21.0) ### Chart...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
