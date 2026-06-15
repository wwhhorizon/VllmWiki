# vllm-project/vllm#40212: [CI Failure]: mi325_1: Kernels MoE Test %N

| 字段 | 值 |
| --- | --- |
| Issue | [#40212](https://github.com/vllm-project/vllm/issues/40212) |
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
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [CI Failure]: mi325_1: Kernels MoE Test %N

### Issue 正文摘录

## AMD nightly — failing test group **Group:** `mi325_1: Kernels MoE Test %N` **Current streak start:** 2026-03-31 **First failure in 60d window:** 2026-03-31 **Last successful nightly:** — **Break frequency (60d, pass↔fail flips):** 0 **Latest nightly date:** 2026-04-20 **Latest build(s):** [amd-ci #7824](https://buildkite.com/vllm/amd-ci/builds/7824) ### Hardware status in latest nightly | hardware | status | |---|---| | `mi325_1` | fail | Auto-managed by `sync_ready_tickets.py`. Closed + moved to Done when this group passes on all AMD hardware. *Last sync: https://github.com/AndreasKaratzas/vllm-ci-dashboard/actions/runs/24731404470*

## 现有链接修复摘要

#7824 [Bugfix][Intel] Fix XPU Dockerfile Build

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: mi325_1: Kernels MoE Test %N ci-failure ## AMD nightly — failing test group **Group:** `mi325_1: Kernels MoE Test %N` **Current streak start:** 2026-03-31 **First failure in 60d window:** 2026-03-31 **Last
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [CI Failure]: mi325_1: Kernels MoE Test %N ci-failure ## AMD nightly — failing test group **Group:** `mi325_1: Kernels MoE Test %N` **Current streak start:** 2026-03-31 **First failure in 60d window:** 2026-03-31 **Last...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: mi325_1: Kernels MoE Test %N ci-failure ## AMD nightly — failing test group **Group:** `mi325_1: Kernels MoE Test %N` **Current streak start:** 2026-03-31 **First failure in 60d window:** 2026-03-31 **Last...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#7824](https://github.com/vllm-project/vllm/pull/7824) | mentioned | 0.45 | [Bugfix][Intel] Fix XPU Dockerfile Build | ** 0 **latest nightly date:** 2026-04-20 **latest build(s):** [amd-ci #7824](https://buildkite.com/vllm/amd-ci/builds/7824) ### hardware status in latest nightly \| hardware \| stat… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
