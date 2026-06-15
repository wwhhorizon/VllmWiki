# vllm-project/vllm#32832: [Performance]: H200 Kimi K2 TP8 Triton MoE min-latency

| 字段 | 值 |
| --- | --- |
| Issue | [#32832](https://github.com/vllm-project/vllm/issues/32832) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support;moe;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | fp8;kernel;moe;quantization;triton |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: H200 Kimi K2 TP8 Triton MoE min-latency

### Issue 正文摘录

### Proposal to improve performance Here's a nsys screenshot of DeepSeek-V3.1 TP=8, conc=16 gen step. 2 triton MoE kernels take about 109us. The nsys screenshot of Kimi-K2-Instruct TP=8, conc=16, gen step. 2 triton MoE kernels take 234us. - DeepSeek‑V3/V3.1: ≈671B total params, ~37B activated per token, blockscale FP8 weight, MoE with 256 routed experts + 1 shared expert, top‑8 routing per token. - Kimi‑K2: ≈1.04T total params, ~32B activated per token, w4a16 int4 weight, 384 experts + shared expert, also top‑8 routing per token. Haven't dive deep yet but would expect the two model runs with similar perf. There may be some perf optimization opportunity toward int4 triton MoE kernel. ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: - DeepSeek‑V3/V3.1: ≈671B total params, ~37B activated per token, blockscale FP8 weight, MoE with 256 routed experts + 1 shared expert, top‑8 routing per token. - Kimi‑K2: ≈1.04T total params, ~32B activated per token,...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Performance]: H200 Kimi K2 TP8 Triton MoE min-latency performance ### Proposal to improve performance Here's a nsys screenshot of DeepSeek-V3.1 TP=8, conc=16 gen step. 2 triton MoE kernels take about 109us. The nsys sc...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Performance]: H200 Kimi K2 TP8 Triton MoE min-latency performance ### Proposal to improve performance Here's a nsys screenshot of DeepSeek-V3.1 TP=8, conc=16 gen step. 2 triton MoE kernels take about 109us. The nsys sc...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Performance]: H200 Kimi K2 TP8 Triton MoE min-latency performance ### Proposal to improve performance Here's a nsys screenshot of DeepSeek-V3.1 TP=8, conc=16 gen step. 2 triton MoE kernels take about 109us. The nsys sc...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: t;moe;quantization fp8;kernel;moe;quantization;triton slowdown dtype;env_dependency Proposal to improve performance

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
