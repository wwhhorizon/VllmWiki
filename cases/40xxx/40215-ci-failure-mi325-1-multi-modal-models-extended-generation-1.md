# vllm-project/vllm#40215: [CI Failure]: mi325_1: Multi-Modal Models (Extended Generation 1)

| 字段 | 值 |
| --- | --- |
| Issue | [#40215](https://github.com/vllm-project/vllm/issues/40215) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: mi325_1: Multi-Modal Models (Extended Generation 1)

### Issue 正文摘录

## AMD nightly — failing test group **Group:** `mi325_1: Multi-Modal Models (Extended Generation 1)` **Current streak start:** 2026-03-31 **First failure in 60d window:** 2026-03-31 **Last successful nightly:** — **Break frequency (60d, pass↔fail flips):** 0 **Latest nightly date:** 2026-04-19 **Latest build(s):** [amd-ci #7806](https://buildkite.com/vllm/amd-ci/builds/7806) ### Hardware status in latest nightly | hardware | status | |---|---| | `mi325_1` | fail | Auto-managed by `sync_ready_tickets.py`. Closed + moved to Done when this group passes on all AMD hardware. *Last sync: https://github.com/AndreasKaratzas/vllm-ci-dashboard/actions/runs/24647351649*

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi325_1: Multi-Modal Models (Extended Generation 1) ci-failure ## AMD nightly — failing test group **Group:** `mi325_1: Multi-Modal Models (Extended Generation 1)` **Current streak start:** 2026-03-31 **Fi
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [CI Failure]: mi325_1: Multi-Modal Models (Extended Generation 1) ci-failure ## AMD nightly — failing test group **Group:** `mi325_1: Multi-Modal Models (Extended Generation 1)` **Current streak start:** 2026-03-31 **Fi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Modal Models (Extended Generation 1) ci-failure ## AMD nightly — failing test group **Group:** `mi325_1: Multi-Modal Models (Extended Generation 1)` **Current streak start:** 2026-03-31 **First failure in 60d window:**...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
