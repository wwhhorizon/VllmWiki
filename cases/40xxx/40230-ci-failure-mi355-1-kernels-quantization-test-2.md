# vllm-project/vllm#40230: [CI Failure]: mi355_1: Kernels Quantization Test 2

| 字段 | 值 |
| --- | --- |
| Issue | [#40230](https://github.com/vllm-project/vllm/issues/40230) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;quantization |
| 子分类 |  |
| Operator 关键词 | kernel;quantization |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi355_1: Kernels Quantization Test 2

### Issue 正文摘录

## AMD nightly — failing test group **Group:** `mi355_1: Kernels Quantization Test 2` **Current streak start:** 2026-03-31 **First failure in 60d window:** 2026-03-31 **Last successful nightly:** — **Break frequency (60d, pass↔fail flips):** 0 **Latest nightly date:** 2026-04-18 **Latest build(s):** #7791 ### Hardware status in latest nightly | hardware | status | |---|---| | `mi355_1` | fail | Auto-managed by `sync_ready_tickets.py`. Closed + moved to Done when this group passes on all AMD hardware. *Last sync: https://github.com/AndreasKaratzas/vllm-internal-project-dashboard/actions/runs/24602867596*

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi355_1: Kernels Quantization Test 2 ci-failure ## AMD nightly — failing test group **Group:** `mi355_1: Kernels Quantization Test 2` **Current streak start:** 2026-03-31 **First failure in 60d window:** 2
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [CI Failure]: mi355_1: Kernels Quantization Test 2 ci-failure ## AMD nightly — failing test group **Group:** `mi355_1: Kernels Quantization Test 2` **Current streak start:** 2026-03-31 **First failure in 60d window:** 2...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: mi355_1: Kernels Quantization Test 2 ci-failure ## AMD nightly — failing test group **Group:** `mi355_1: Kernels Quantization Test 2` **Current streak start:** 2026-03-31 **First failure in 60d window:** 2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
