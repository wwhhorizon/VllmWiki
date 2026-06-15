# vllm-project/vllm#40242: [CI Failure]: mi355_2: NixlConnector PD + Spec Decode acceptance (2 GPUs)

| 字段 | 值 |
| --- | --- |
| Issue | [#40242](https://github.com/vllm-project/vllm/issues/40242) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: mi355_2: NixlConnector PD + Spec Decode acceptance (2 GPUs)

### Issue 正文摘录

## AMD nightly — failing test group **Group:** `mi355_2: NixlConnector PD + Spec Decode acceptance (2 GPUs)` **Current streak start:** 2026-04-02 **First failure in 60d window:** 2026-04-02 **Last successful nightly:** — **Break frequency (60d, pass↔fail flips):** 0 **Latest nightly date:** 2026-04-21 **Latest build(s):** [amd-ci #7854](https://buildkite.com/vllm/amd-ci/builds/7854) ### Hardware status in latest nightly | hardware | status | |---|---| | `mi355_2` | fail | Auto-managed by `sync_ready_tickets.py`. Closed + moved to Done when this group passes on all AMD hardware. *Last sync: https://github.com/AndreasKaratzas/vllm-ci-dashboard/actions/runs/24731404470*

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi355_2: NixlConnector PD + Spec Decode acceptance (2 GPUs) ci-failure ## AMD nightly — failing test group **Group:** `mi355_2: NixlConnector PD + Spec Decode acceptance (2 GPUs)` **Current streak start:**
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [CI Failure]: mi355_2: NixlConnector PD + Spec Decode acceptance (2 GPUs) ci-failure ## AMD nightly — failing test group **Group:** `mi355_2: NixlConnector PD + Spec Decode acceptance (2 GPUs)` **Current streak start:**...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: PD + Spec Decode acceptance (2 GPUs) ci-failure ## AMD nightly — failing test group **Group:** `mi355_2: NixlConnector PD + Spec Decode acceptance (2 GPUs)` **Current streak start:** 2026-04-02 **First failure in 60d wi...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
