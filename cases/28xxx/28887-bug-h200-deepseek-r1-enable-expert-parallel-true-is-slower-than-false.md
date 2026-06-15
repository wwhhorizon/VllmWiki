# vllm-project/vllm#28887: [Bug]: [H200] DeepSeek R1 `--enable-expert-parallel True` is slower than `False`.

| 字段 | 值 |
| --- | --- |
| Issue | [#28887](https://github.com/vllm-project/vllm/issues/28887) |
| 状态 | closed |
| 标签 | bug;stale;deepseek |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;gemm_linear;model_support;moe;quantization;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | fp8;gemm;moe;triton |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [H200] DeepSeek R1 `--enable-expert-parallel True` is slower than `False`.

### Issue 正文摘录

### Your current environment 5a84b76 ### 🐛 Describe the bug With `--enable-expert-parallel True` I'm not getting any improvement from expert parallelism, due to context phase taking too long (high TTFT). After examined the nsys of concurrency=32, the issue is 1. Triton MoE backend EP at context phase has higher latency (3.4ms per layer) comparing to TP (3.1 ms per layer), the difference is mainly from MoE gemm (FC1, act, FC2). After https://github.com/vllm-project/vllm/pull/27134 merged I'm able to benchmark with FlashInfer FP8 (DeepGEMM swapAB backend) w. FlashInfer 0.5.2. I'm seeing improved context phase latency (3.2 ms per layer), but 2. even at higher concurrencies, the performance are still worse than EP=False. We can neglect the low concurrency case due to expert imbalance. (All are 8xH200, 1600/600) Mean TTFT (ms) Max Requests | TP8-TRITON | TEP8-TRITON | TEP8-FLASHINFER -- | -- | -- | -- 8 | 545.59 | 641.8 | 562.96 16 | 683.84 | 823.33 | 744.31 **32** | **816.39** | **1051.92** | **913.23** 64 | 1069.97 | 1682.02 | 1271.02 128 | 1580.61 | 2271.73 | 1752.98 256 | 2703.51 | 3426.17 | 2911.41 512 | 36292.59 | 41492.41 | 37524.58 OTPS Max request concurrency | TP8 (Triton) |...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: igh TTFT). After examined the nsys of concurrency=32, the issue is 1. Triton MoE backend EP at context phase has higher latency (3.4ms per layer) comparing to TP (3.1 ms per layer), the difference is mainly from MoE gem...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: llm-project/vllm/pull/27134 merged I'm able to benchmark with FlashInfer FP8 (DeepGEMM swapAB backend) w. FlashInfer 0.5.2. I'm seeing improved context phase latency (3.2 ms per layer), but 2. even at higher concurrenci...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: [H200] DeepSeek R1 `--enable-expert-parallel True` is slower than `False`. bug;stale;deepseek ### Your current environment 5a84b76 ### 🐛 Describe the bug With `--enable-expert-parallel True` I'm not getting any i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: DeepSeek R1 `--enable-expert-parallel True` is slower than `False`. bug;stale;deepseek ### Your current environment 5a84b76 ### 🐛 Describe the bug With `--enable-expert-parallel True` I'm not getting any improvement fro...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: =32, the issue is 1. Triton MoE backend EP at context phase has higher latency (3.4ms per layer) comparing to TP (3.1 ms per layer), the difference is mainly from MoE gemm (FC1, act, FC2). After https://github.com/vllm-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
