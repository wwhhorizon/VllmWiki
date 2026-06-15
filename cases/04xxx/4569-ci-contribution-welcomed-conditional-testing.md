# vllm-project/vllm#4569: [CI][Contribution Welcomed] Conditional Testing

| 字段 | 值 |
| --- | --- |
| Issue | [#4569](https://github.com/vllm-project/vllm/issues/4569) |
| 状态 | closed |
| 标签 | help wanted;good first issue;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI][Contribution Welcomed] Conditional Testing

### Issue 正文摘录

### Anything you want to discuss about vllm. Currently we run all CI tests matrix on every single commit in pull requests. The CI cost of the vLLM has been doubling each week as we add more tests and receiving many PRs from the community. A good first step would be to only run some tests when relevant code is changed. For example, do not run unit/integration tests when docs or examples are changed.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Contribution Welcomed] Conditional Testing help wanted;good first issue;stale ### Anything you want to discuss about vllm. Currently we run all CI tests matrix on every single commit in pull requests. The CI cost of th...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [CI][Contribution Welcomed] Conditional Testing help wanted;good first issue;stale ### Anything you want to discuss about vllm. Currently we run all CI tests matrix on every single commit in pull requests. The CI cost of
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI][Contribution Welcomed] Conditional Testing help wanted;good first issue;stale ### Anything you want to discuss about vllm. Currently we run all CI tests matrix on every single commit in pull requests. The CI cost o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
