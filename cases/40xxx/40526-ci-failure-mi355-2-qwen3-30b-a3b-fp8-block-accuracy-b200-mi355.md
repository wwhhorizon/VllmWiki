# vllm-project/vllm#40526: [CI Failure]: mi355_2: Qwen3-30B-A3B-FP8-block Accuracy (B200-MI355)

| 字段 | 值 |
| --- | --- |
| Issue | [#40526](https://github.com/vllm-project/vllm/issues/40526) |
| 状态 | closed |
| 标签 | rocm;ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;quantization |
| 子分类 | precision |
| Operator 关键词 | fp8 |
| 症状 | build_error |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi355_2: Qwen3-30B-A3B-FP8-block Accuracy (B200-MI355)

### Issue 正文摘录

## AMD nightly — failing test group **Group:** `mi355_2: Qwen3-30B-A3B-FP8-block Accuracy (B200-MI355)` **Current streak start:** 2026-04-21 **First failure in 60d window:** 2026-04-21 **Last successful nightly:** 2026-04-20 **Break frequency (60d, pass↔fail flips):** 1 **Latest nightly date:** 2026-04-21 **Latest build(s):** [amd-ci #7854](https://buildkite.com/vllm/amd-ci/builds/7854) ### Hardware status in latest nightly | hardware | status | |---|---| | `mi355_2` | fail | Auto-managed by `sync_ready_tickets.py`. Closed + moved to Done when this group passes on all AMD hardware. *Last sync: https://github.com/AndreasKaratzas/vllm-ci-dashboard/actions/runs/24731404470*

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [CI Failure]: mi355_2: Qwen3-30B-A3B-FP8-block Accuracy (B200-MI355) rocm;ci-failure ## AMD nightly — failing test group **Group:** `mi355_2: Qwen3-30B-A3B-FP8-block Accuracy (B200-MI355)` **Current streak start:** 2026...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi355_2: Qwen3-30B-A3B-FP8-block Accuracy (B200-MI355) rocm;ci-failure ## AMD nightly — failing test group **Group:** `mi355_2: Qwen3-30B-A3B-FP8-block Accuracy (B200-MI355)` **Current streak start:** 2026
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [CI Failure]: mi355_2: Qwen3-30B-A3B-FP8-block Accuracy (B200-MI355) rocm;ci-failure ## AMD nightly — failing test group **Group:** `mi355_2: Qwen3-30B-A3B-FP8-block Accuracy (B200-MI355)` **Current streak start:** 2026...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [CI Failure]: mi355_2: Qwen3-30B-A3B-FP8-block Accuracy (B200-MI355) rocm;ci-failure ## AMD nightly — failing test group **Group:** `mi355_2: Qwen3-30B-A3B-FP8-block Accuracy (B200-MI355)` **Current streak start:** 2026...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: mi355_2: Qwen3-30B-A3B-FP8-block Accuracy (B200-MI355) rocm;ci-failure ## AMD nightly — failing test group **Group:** `mi355_2: Qwen3-30B-A3B-FP8-block Accuracy (B200-MI355)` **Current streak start:** 2026...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
