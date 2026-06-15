# vllm-project/vllm#9435: [RFC]: Enable stale bot for issues and PRs

| 字段 | 值 |
| --- | --- |
| Issue | [#9435](https://github.com/vllm-project/vllm/issues/9435) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Enable stale bot for issues and PRs

### Issue 正文摘录

### Motivation. There are currently >400 open PRs and ~1.7k open issues. Many of these are not active and could be closed. This problem is often more challenging in a very active and popular project like vLLM. GitHub provides an action to help automate this process. https://github.com/actions/stale By adopting this action, those with the time and interest in helping with issue triage or PR reviews will have an easier time ensuring their time is used most effectively. ### Proposed Change. I propose adopting `actions/stale` to automate the process of pruning the issue and PR queues of items with no activity. A sample policy would be something like this: * Add the `stale` label and leave a comment after an issue or PR has not had any activity within 90 days. * Close an issue and add another comment if an issue or PR continues to have no activity for an addition 30 days. The times are configurable. An interested party can leave a comment to reset the stale timer. Configuring a label that will tell the bot to ignore that issue or PR (like `keep-open` or something) is also possible. If there's interest, I am happy to do the PR for it. Agreeing on the policy is the harder and more import...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: Enable stale bot for issues and PRs RFC ### Motivation. There are currently >400 open PRs and ~1.7k open issues. Many of these are not active and could be closed. This problem is often more challenging in a very...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: happy to do the PR for it. Agreeing on the policy is the harder and more important part. ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: PR continues to have no activity for an addition 30 days. The times are configurable. An interested party can leave a comment to reset the stale timer. Configuring a label that will tell the bot to ignore that issue or...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
