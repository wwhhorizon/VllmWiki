# vllm-project/vllm#40213: [CI Failure]: mi325_1: Kernels MoE Test 3

| 字段 | 值 |
| --- | --- |
| Issue | [#40213](https://github.com/vllm-project/vllm/issues/40213) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;moe |
| 子分类 |  |
| Operator 关键词 | kernel;moe |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_1: Kernels MoE Test 3

### Issue 正文摘录

## AMD nightly — failing test group **Group:** `mi325_1: Kernels MoE Test 3` **Current streak start:** 2026-03-31 **First failure in 60d window:** 2026-03-31 **Last successful nightly:** — **Break frequency (60d, pass↔fail flips):** 0 **Latest nightly date:** 2026-04-18 **Latest build(s):** #7791 ### Hardware status in latest nightly | hardware | status | |---|---| | `mi325_1` | fail | Auto-managed by `sync_ready_tickets.py`. Closed + moved to Done when this group passes on all AMD hardware. *Last sync: https://github.com/AndreasKaratzas/vllm-internal-project-dashboard/actions/runs/24602867596*

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi325_1: Kernels MoE Test 3 ci-failure ## AMD nightly — failing test group **Group:** `mi325_1: Kernels MoE Test 3` **Current streak start:** 2026-03-31 **First failure in 60d window:** 2026-03-31 **Last s
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [CI Failure]: mi325_1: Kernels MoE Test 3 ci-failure ## AMD nightly — failing test group **Group:** `mi325_1: Kernels MoE Test 3` **Current streak start:** 2026-03-31 **First failure in 60d window:** 2026-03-31 **Last s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: mi325_1: Kernels MoE Test 3 ci-failure ## AMD nightly — failing test group **Group:** `mi325_1: Kernels MoE Test 3` **Current streak start:** 2026-03-31 **First failure in 60d window:** 2026-03-31 **Last s...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
