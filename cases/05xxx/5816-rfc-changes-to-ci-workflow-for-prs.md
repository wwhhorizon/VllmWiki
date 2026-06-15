# vllm-project/vllm#5816: [RFC] Changes to CI workflow for PRs

| 字段 | 值 |
| --- | --- |
| Issue | [#5816](https://github.com/vllm-project/vllm/issues/5816) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC] Changes to CI workflow for PRs

### Issue 正文摘录

### Motivation. - We need to aggressively drive down CI cost since the current burn rate is not sustainable for vLLM. - Currently, we run full CI tests for every commits on every PR which is quite a lot and unnecessary. ### Proposed Change. This is the same workflow that `ray` CI is using which I think is working great in terms of maintaining the same CI signals & cost reduction. I think vLLM would benefit from the same system. Instead of having a single CI pipeline that runs on every PRs, we can break it down to 3 separate pipelines, each serving a different purpose. **1. `Fast-check` pipeline** - **Purpose**: quickly catch small errors in between PR commits that don't require unnecessary tests. - Run a small, fast, and essential subset of tests (e.g. basic correctness, regression, engine, core, etc..) - Trigger on every commit within a PR. **2. `Pre-merge` pipeline** - **Purpose**: catch as many errors as possible before PR is merged to main. - Run all tests for now. Once we have a mature automated test selection (planned for Q3), it can be applied here to cut costs even more. - Required to pass in order to merge PR - Should be triggered when: - PR is ready to merge - PR author...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: rrent burn rate is not sustainable for vLLM. - Currently, we run full CI tests for every commits on every PR which is quite a lot and unnecessary. ### Proposed Change. This is the same workflow that `ray` CI is using wh...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [RFC] Changes to CI workflow for PRs RFC;stale ### Motivation. - We need to aggressively drive down CI cost since the current burn rate is not sustainable for vLLM. - Currently, we run full CI tests for every commits on...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rent purpose. **1. `Fast-check` pipeline** - **Purpose**: quickly catch small errors in between PR commits that don't require unnecessary tests. - Run a small, fast, and essential subset of tests (e.g. basic correctness...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [RFC] Changes to CI workflow for PRs RFC;stale ### Motivation. - We need to aggressively drive down CI cost since the current burn rate is not sustainable for vLLM. - Currently, we run full CI tests for every commits on...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
