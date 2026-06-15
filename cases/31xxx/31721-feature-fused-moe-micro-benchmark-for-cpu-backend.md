# vllm-project/vllm#31721: [Feature]: Fused MoE Micro Benchmark for CPU Backend

| 字段 | 值 |
| --- | --- |
| Issue | [#31721](https://github.com/vllm-project/vllm/issues/31721) |
| 状态 | closed |
| 标签 | feature request;cpu |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;moe |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;moe |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Feature]: Fused MoE Micro Benchmark for CPU Backend

### Issue 正文摘录

### 🚀 The feature, motivation and pitch A unified script to benchmark Fused MoE performance on CPU, instead of having each contributor writing their own benchmarks (and then throwing them). We need something similar to [benchmark_paged_attention.py](https://github.com/vllm-project/vllm/blob/main/benchmarks/kernels/benchmark_paged_attention.py) for CUDA. It's easier (and less noisy) to have a micro benchmark (that runs in ~ seconds) to iterate over instead of re-running end to end benchmarks which take ~ minutes. Object to benchmark: - #30531 Similar issue for reference: - Issue #30374 -> PR #31720 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#30531 [CPU] Refactor CPU fused MOE | #31720 [cpu][bench] Add CPU paged attention benchmarks | #32092 [cpu][bench] Add Fused MoE Micro Benchmark for CPU Backend

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ject/vllm/blob/main/benchmarks/kernels/benchmark_paged_attention.py) for CUDA. It's easier (and less noisy) to have a micro benchmark (that runs in ~ seconds) to iterate over instead of re-running end to end benchmarks...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Feature]: Fused MoE Micro Benchmark for CPU Backend feature request;cpu ### 🚀 The feature, motivation and pitch A unified script to benchmark Fused MoE performance on CPU, instead of having each contributor writing the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: Fused MoE Micro Benchmark for CPU Backend feature request;cpu ### 🚀 The feature, motivation and pitch A unified script to benchmark Fused MoE performance on CPU, instead of having each contributor writing the...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Feature]: Fused MoE Micro Benchmark for CPU Backend feature request;cpu ### 🚀 The feature, motivation and pitch A unified script to benchmark Fused MoE performance on CPU, instead of having each contributor writing the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Fused MoE Micro Benchmark for CPU Backend feature request;cpu ### 🚀 The feature, motivation and pitch A unified script to benchmark Fused MoE performance on CPU, instead of having each contributor writing the...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#30531](https://github.com/vllm-project/vllm/pull/30531) | mentioned | 0.45 | [CPU] Refactor CPU fused MOE | end to end benchmarks which take ~ minutes. object to benchmark: - #30531 similar issue for reference: - issue #30374 -> pr #31720 ### alternatives _no response_ ### additional co |
| [#31720](https://github.com/vllm-project/vllm/pull/31720) | mentioned | 0.45 | [cpu][bench] Add CPU paged attention benchmarks | enchmark: - #30531 similar issue for reference: - issue #30374 -> pr #31720 ### alternatives _no response_ ### additional context _no response_ ### before submitting a new issue... |
| [#32092](https://github.com/vllm-project/vllm/pull/32092) | closes_keyword | 0.95 | [cpu][bench] Add Fused MoE Micro Benchmark for CPU Backend | Fixes: #31721 ## Test Plan Tested using this instance: <img width="912" height="217" alt="Screenshot 2026-01-10 at 22 51 33" src="https://github.com/user-attachments/assets/1e4c9 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
