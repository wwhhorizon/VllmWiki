# vllm-project/vllm#40241: [CI Failure]: mi355_2: Distributed Tests (2 GPUs)(H100-MI355)

| 字段 | 值 |
| --- | --- |
| Issue | [#40241](https://github.com/vllm-project/vllm/issues/40241) |
| 状态 | closed |
| 标签 | rocm;ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: mi355_2: Distributed Tests (2 GPUs)(H100-MI355)

### Issue 正文摘录

## AMD nightly — failing test group **Group:** `mi355_2: Distributed Tests (2 GPUs)(H100-MI355)` **Current streak start:** 2026-04-02 **First failure in 60d window:** 2026-04-02 **Last successful nightly:** — **Break frequency (60d, pass↔fail flips):** 0 **Latest nightly date:** 2026-04-20 **Latest build(s):** [amd-ci #7824](https://buildkite.com/vllm/amd-ci/builds/7824) ### Hardware status in latest nightly | hardware | status | |---|---| | `mi355_2` | fail | Auto-managed by `sync_ready_tickets.py`. Closed + moved to Done when this group passes on all AMD hardware. *Last sync: https://github.com/AndreasKaratzas/vllm-ci-dashboard/actions/runs/24731404470*

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi355_2: Distributed Tests (2 GPUs)(H100-MI355) rocm;ci-failure ## AMD nightly — failing test group **Group:** `mi355_2: Distributed Tests (2 GPUs)(H100-MI355)` **Current streak start:** 2026-04-02 **First
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [CI Failure]: mi355_2: Distributed Tests (2 GPUs)(H100-MI355) rocm;ci-failure ## AMD nightly — failing test group **Group:** `mi355_2: Distributed Tests (2 GPUs)(H100-MI355)` **Current streak start:** 2026-04-02 **First...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: mi355_2: Distributed Tests (2 GPUs)(H100-MI355) rocm;ci-failure ## AMD nightly — failing test group **Group:** `mi355_2: Distributed Tests (2 GPUs)(H100-MI355)` **Current streak start:** 2026-04-02 **First...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
