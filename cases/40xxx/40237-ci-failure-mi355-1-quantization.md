# vllm-project/vllm#40237: [CI Failure]: mi355_1: Quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#40237](https://github.com/vllm-project/vllm/issues/40237) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;quantization |
| 子分类 |  |
| Operator 关键词 | quantization |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi355_1: Quantization

### Issue 正文摘录

## AMD nightly — failing test group **Group:** `mi355_1: Quantization` **Current streak start:** 2026-03-31 **First failure in 60d window:** 2026-03-31 **Last successful nightly:** — **Break frequency (60d, pass↔fail flips):** 0 **Latest nightly date:** 2026-04-21 **Latest build(s):** [amd-ci #7854](https://buildkite.com/vllm/amd-ci/builds/7854) ### Hardware status in latest nightly | hardware | status | |---|---| | `mi355_1` | fail | Auto-managed by `sync_ready_tickets.py`. Closed + moved to Done when this group passes on all AMD hardware. *Last sync: https://github.com/AndreasKaratzas/vllm-ci-dashboard/actions/runs/24731404470*

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi355_1: Quantization ci-failure ## AMD nightly — failing test group **Group:** `mi355_1: Quantization` **Current streak start:** 2026-03-31 **First failure in 60d window:** 2026-03-31 **Last successful ni
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [CI Failure]: mi355_1: Quantization ci-failure ## AMD nightly — failing test group **Group:** `mi355_1: Quantization` **Current streak start:** 2026-03-31 **First failure in 60d window:** 2026-03-31 **Last successful ni...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: mi355_1: Quantization ci-failure ## AMD nightly — failing test group **Group:** `mi355_1: Quantization` **Current streak start:** 2026-03-31 **First failure in 60d window:** 2026-03-31 **Last successful ni...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
