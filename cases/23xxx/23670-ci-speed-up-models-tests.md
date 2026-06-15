# vllm-project/vllm#23670: [CI]: Speed up Models Tests

| 字段 | 值 |
| --- | --- |
| Issue | [#23670](https://github.com/vllm-project/vllm/issues/23670) |
| 状态 | closed |
| 标签 | ci/build;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI]: Speed up Models Tests

### Issue 正文摘录

Top level test groups: - Basic Models - Language Models Test (Standard) - Language Models Test (Hybrid) Tasks: - Understand where time is being spent - Keep minimal set that runs on all PRs - Larger set with better scoping to source file changes (i.e. when any of the corresponding model implementations are changed)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI]: Speed up Models Tests ci/build;stale Top level test groups: - Basic Models - Language Models Test (Standard) - Language Models Test (Hybrid) Tasks: - Understand where time is being spent - Keep minimal set that run
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [CI]: Speed up Models Tests ci/build;stale Top level test groups: - Basic Models - Language Models Test (Standard) - Language Models Test (Hybrid) Tasks: - Understand where time is being spent - Keep minimal set that ru...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [CI]: Speed up Models Tests ci/build;stale Top level test groups: - Basic Models - Language Models Test (Standard) - Language Models Test (Hybrid) Tasks: - Understand where time is being spent - Keep minimal set that ru...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI]: Speed up Models Tests ci/build;stale Top level test groups: - Basic Models - Language Models Test (Standard) - Language Models Test (Hybrid) Tasks: - Understand where time is being spent - Keep minimal set that ru...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
