# vllm-project/vllm#35126: [CI Failure]:  mi355_1: Kernels MoE Test %N

| 字段 | 值 |
| --- | --- |
| Issue | [#35126](https://github.com/vllm-project/vllm/issues/35126) |
| 状态 | closed |
| 标签 | rocm;ci-failure |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;moe |
| 子分类 |  |
| Operator 关键词 | kernel;moe |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]:  mi355_1: Kernels MoE Test %N

### Issue 正文摘录

## AMD nightly — failing test group **Group:** `mi355_1: Kernels MoE Test %N` **Current streak start:** 2026-03-31 **First failure in 60d window:** 2026-03-31 **Last successful nightly:** — **Break frequency (60d, pass↔fail flips):** 0 **Latest nightly date:** 2026-04-21 **Latest build(s):** [amd-ci #7854](https://buildkite.com/vllm/amd-ci/builds/7854) ### Hardware status in latest nightly | hardware | status | |---|---| | `mi355_1` | fail | Auto-managed by `sync_ready_tickets.py`. Closed + moved to Done when this group passes on all AMD hardware. *Last sync: https://github.com/AndreasKaratzas/vllm-ci-dashboard/actions/runs/24731404470*

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi355_1: Kernels MoE Test %N rocm;ci-failure ## AMD nightly — failing test group **Group:** `mi355_1: Kernels MoE Test %N` **Current streak start:** 2026-03-31 **First failure in 60d window:** 2026-03-31
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [CI Failure]: mi355_1: Kernels MoE Test %N rocm;ci-failure ## AMD nightly — failing test group **Group:** `mi355_1: Kernels MoE Test %N` **Current streak start:** 2026-03-31 **First failure in 60d window:** 2026-03-31 *...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [CI Failure]: mi355_1: Kernels MoE Test %N rocm;ci-failure ## AMD nightly — failing test group **Group:** `mi355_1: Kernels MoE Test %N` **Current streak start:** 2026-03-31 **First failure in 60d window:** 2026-03-31 *...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: mi355_1: Kernels MoE Test %N rocm;ci-failure ## AMD nightly — failing test group **Group:** `mi355_1: Kernels MoE Test %N` **Current streak start:** 2026-03-31 **First failure in 60d window:** 2026-03-31 *...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
