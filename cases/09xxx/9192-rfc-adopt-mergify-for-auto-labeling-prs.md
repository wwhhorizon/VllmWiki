# vllm-project/vllm#9192: [RFC]: Adopt mergify for auto-labeling PRs

| 字段 | 值 |
| --- | --- |
| Issue | [#9192](https://github.com/vllm-project/vllm/issues/9192) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Adopt mergify for auto-labeling PRs

### Issue 正文摘录

### Motivation. vLLM is a very active project with a large and busy queue of PRs. Additional usage of github labels would assist with narrowing down which PRs to look at given a person's interests, as well as the state of the PR. ### Proposed Change. Adopt mergify to perform automated labeling of PRs. https://docs.mergify.com/ While github also provides an [action for PR labeling](https://github.com/actions/labeler), it only supports labeling based on the branch and the files changed. Mergify supports labeling based on more criteria, such as whether a branch has conflicts with `main`. Configuration would go into `.github/mergify.yml`. An example entry to auto-label PRs that touch files in the `docs/` directory: ```yaml - name: label-documentation description: Automatically apply documentation label conditions: - or: - files~=^[^/]+\.md$ - files~=^CONTRIBUTING/ - files~=^docs/ actions: label: add: - documentation ``` Here is an example that is a bit more unique to Mergify's capabilities. This sample configuration will label a PR and comment tagging the PR author if the PR goes into conflict with the target branch (`main`). It will also automatically remove the label once conflicts...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: RFC ### Motivation. vLLM is a very active project with a large and busy queue of PRs. Additional usage of github labels would assist with narrowing down which PRs to look at given a person's interests, as well as the st...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: /en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork - name: remove 'needs-rebase' label when conflict is resolved conditions: - -conflict - -closed actions: label: remove: - needs-rebase...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: d on more criteria, such as whether a branch has conflicts with `main`. Configuration would go into `.github/mergify.yml`. An example entry to auto-label PRs that touch files in the `docs/` directory: ```yaml - name: la...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
