# vllm-project/vllm#30374: [Feature][CPU Backend]: Add Paged Attention Benchmarks for CPU backend

| 字段 | 值 |
| --- | --- |
| Issue | [#30374](https://github.com/vllm-project/vllm/issues/30374) |
| 状态 | closed |
| 标签 | feature request;cpu |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api |
| 子分类 |  |
| Operator 关键词 | attention;cuda;kernel |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Feature][CPU Backend]: Add Paged Attention Benchmarks for CPU backend

### Issue 正文摘录

### 🚀 The feature, motivation and pitch #27954 introduced a new attention backend for CPU. #29193 and #30068 accelerated that paged attn impl for Arm. It'd be nice to have a unified script to benchmark paged attention perf on CPU, instead of having each contributor writing their own benchmarks (and then throwing them). We need something similar to [benchmark_paged_attention.py](https://github.com/vllm-project/vllm/blob/main/benchmarks/kernels/benchmark_paged_attention.py) for CUDA. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#27954 [CPU] Refactor CPU attention backend | #29193 [perf][cpu] Accelerate paged attention GEMMs (QK, PV) on Arm CPUs with NEON | #30068 [CPU][Perf] Add fast vectorized exp impl from Arm Optimized Routines | #31720 [cpu][bench] Add CPU paged attention benchmarks

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ject/vllm/blob/main/benchmarks/kernels/benchmark_paged_attention.py) for CUDA. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searche...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Feature][CPU Backend]: Add Paged Attention Benchmarks for CPU backend feature request;cpu ### 🚀 The feature, motivation and pitch #27954 introduced a new attention backend for CPU. #29193 and #30068 accelerated that pa...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature][CPU Backend]: Add Paged Attention Benchmarks for CPU backend feature request;cpu ### 🚀 The feature, motivation and pitch #27954 introduced a new attention backend for CPU. #29193 and #30068 accelerated that pa...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: or CPU attention backend | #29193 [perf][cpu] Accelerate paged attention GEMMs (QK, PV) on Arm CPUs with NEON | #30068 [CPU][Perf] Add fast vectorized exp impl from Arm Optimized Routines | #31720 [cpu][bench] Add CPU p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: re][CPU Backend]: Add Paged Attention Benchmarks for CPU backend feature request;cpu ### 🚀 The feature, motivation and pitch #27954 introduced a new attention backend for CPU. #29193 and #30068 accelerated that paged at...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#27954](https://github.com/vllm-project/vllm/pull/27954) | mentioned | 0.45 | [CPU] Refactor CPU attention backend | n benchmarks for cpu backend ### 🚀 the feature, motivation and pitch #27954 introduced a new attention backend for cpu. #29193 and #30068 accelerated that paged attn impl for arm.… |
| [#29193](https://github.com/vllm-project/vllm/pull/29193) | mentioned | 0.45 | [perf][cpu] Accelerate paged attention GEMMs (QK, PV) on Arm CPUs with NEON | ivation and pitch #27954 introduced a new attention backend for cpu. #29193 and #30068 accelerated that paged attn impl for arm. it'd be nice to have a unified script to benchmark… |
| [#30068](https://github.com/vllm-project/vllm/pull/30068) | mentioned | 0.45 | [CPU][Perf] Add fast vectorized exp impl from Arm Optimized Routines | pitch #27954 introduced a new attention backend for cpu. #29193 and #30068 accelerated that paged attn impl for arm. it'd be nice to have a unified script to benchmark paged atten… |
| [#31720](https://github.com/vllm-project/vllm/pull/31720) | closes_keyword | 0.95 | [cpu][bench] Add CPU paged attention benchmarks | Fixes: #30374 ## Test Plan ## Test Result --- <details> <summary> Essential Elements of an Effective PR Description Checklist </summary> - [ Y] The purpose of the PR, such as " |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
