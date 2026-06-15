# vllm-project/vllm#24682: [CI]: Investigate/fix cases of CI tests not running on latest code from PR branch

| 字段 | 值 |
| --- | --- |
| Issue | [#24682](https://github.com/vllm-project/vllm/issues/24682) |
| 状态 | closed |
| 标签 | bug;ci/build;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI]: Investigate/fix cases of CI tests not running on latest code from PR branch

### Issue 正文摘录

We've seen a couple of recent cases where PR changes fail on main after being merged, but the same test that ran on the PR's CI prior to merge passed. It appears that the code which the passing test ran on wasn't the latest code from the PR branch. This is separate to the issue of test scoping. In these cases the test in question did run and passed. It also shouldn't be a consequence of the use of `USE_PRECOMPILED_WHEELS` because the code differences in question were just changes to python files. Examples: - Tensorizer test: https://github.com/vllm-project/vllm/pull/23928#issuecomment-3273252592 - Basic models test: https://github.com/vllm-project/vllm/pull/24392 Slack threads: [here](https://vllm-dev.slack.com/archives/C07R5PAL2L9/p1757474223819419), [here](https://vllm-dev.slack.com/archives/C07R5PAL2L9/p1757510850053039). This is obviously very high priority since it's causing frequent unnecessary breakages to main. cc @dougbtv

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [CI]: Investigate/fix cases of CI tests not running on latest code from PR branch bug;ci/build;stale We've seen a couple of recent cases where PR changes fail on main after being merged, but the same test that ran on the
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: roject/vllm/pull/24392 Slack threads: [here](https://vllm-dev.slack.com/archives/C07R5PAL2L9/p1757474223819419), [here](https://vllm-dev.slack.com/archives/C07R5PAL2L9/p1757510850053039). This is obviously very high pri...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: /github.com/vllm-project/vllm/pull/23928#issuecomment-3273252592 - Basic models test: https://github.com/vllm-project/vllm/pull/24392 Slack threads: [here](https://vllm-dev.slack.com/archives/C07R5PAL2L9/p17574742238194...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: cases of CI tests not running on latest code from PR branch bug;ci/build;stale We've seen a couple of recent cases where PR changes fail on main after being merged, but the same test that ran on the PR's CI prior to mer...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI]: Investigate/fix cases of CI tests not running on latest code from PR branch bug;ci/build;stale We've seen a couple of recent cases where PR changes fail on main after being merged, but the same test that ran on th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
