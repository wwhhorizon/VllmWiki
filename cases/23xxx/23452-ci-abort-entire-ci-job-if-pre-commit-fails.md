# vllm-project/vllm#23452: [CI]: Abort entire CI job if pre-commit fails

| 字段 | 值 |
| --- | --- |
| Issue | [#23452](https://github.com/vllm-project/vllm/issues/23452) |
| 状态 | closed |
| 标签 | ci/build;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI]: Abort entire CI job if pre-commit fails

### Issue 正文摘录

Tests will need to be re-run regardless in this case so it's better to fail and have the PR author fix linting issues than proceed to run the whole job. It would be good to still run pre-commit in parallel so the total running time isn't impacted, just abort other tests (if possible).

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI]: Abort entire CI job if pre-commit fails ci/build;stale Tests will need to be re-run regardless in this case so it's better to fail and have the PR author fix linting issues than proceed to run the whole job. It wou
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [CI]: Abort entire CI job if pre-commit fails ci/build;stale Tests will need to be re-run regardless in this case so it's better to fail and have the PR author fix linting issues than proceed to run the whole job. It wo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI]: Abort entire CI job if pre-commit fails ci/build;stale Tests will need to be re-run regardless in this case so it's better to fail and have the PR author fix linting issues than proceed to run the whole job. It wo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
