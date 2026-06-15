# vllm-project/vllm#29525: [CI Failure]: mi325_1: Quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#29525](https://github.com/vllm-project/vllm/issues/29525) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;quantization |
| 子分类 |  |
| Operator 关键词 | quantization |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [CI Failure]: mi325_1: Quantization

### Issue 正文摘录

## AMD nightly — failing test group **Group:** `mi325_1: Quantization` **Current streak start:** 2026-03-31 **First failure in 60d window:** 2026-03-31 **Last successful nightly:** — **Break frequency (60d, pass↔fail flips):** 0 **Latest nightly date:** 2026-04-20 **Latest build(s):** [amd-ci #7824](https://buildkite.com/vllm/amd-ci/builds/7824) ### Hardware status in latest nightly | hardware | status | |---|---| | `mi325_1` | fail | Auto-managed by `sync_ready_tickets.py`. Closed + moved to Done when this group passes on all AMD hardware. *Last sync: https://github.com/AndreasKaratzas/vllm-ci-dashboard/actions/runs/24731404470*

## 现有链接修复摘要

#7824 [Bugfix][Intel] Fix XPU Dockerfile Build | #31072 [ROCm][Test] Skip RTN quantization tests on ROCm

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: mi325_1: Quantization ci-failure ## AMD nightly — failing test group **Group:** `mi325_1: Quantization` **Current streak start:** 2026-03-31 **First failure in 60d window:** 2026-03-31 **Last successful ni
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [CI Failure]: mi325_1: Quantization ci-failure ## AMD nightly — failing test group **Group:** `mi325_1: Quantization` **Current streak start:** 2026-03-31 **First failure in 60d window:** 2026-03-31 **Last successful ni...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ion build_error #7824 [Bugfix][Intel] Fix XPU Dockerfile Build | #31072 [ROCm][Test] Skip RTN quantization tests on ROCm AMD nightly — failing test group
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: mi325_1: Quantization ci-failure ## AMD nightly — failing test group **Group:** `mi325_1: Quantization` **Current streak start:** 2026-03-31 **First failure in 60d window:** 2026-03-31 **Last successful ni...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#7824](https://github.com/vllm-project/vllm/pull/7824) | mentioned | 0.45 | [Bugfix][Intel] Fix XPU Dockerfile Build | ** 0 **latest nightly date:** 2026-04-20 **latest build(s):** [amd-ci #7824](https://buildkite.com/vllm/amd-ci/builds/7824) ### hardware status in latest nightly \| hardware \| stat… |
| [#31072](https://github.com/vllm-project/vllm/pull/31072) | closes_keyword | 0.95 | [ROCm][Test] Skip RTN quantization tests on ROCm | Fixes #29525 (AMD MI325 CI failure - Quantization Test) RTN quantization is not supported on ROCm/AMD GPUs. This PR adds explicit platform detection to skip RTN quantization tests |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
