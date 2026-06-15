# vllm-project/vllm#5565: [RFC]: Branch based version control, and development version

| 字段 | 值 |
| --- | --- |
| Issue | [#5565](https://github.com/vllm-project/vllm/issues/5565) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Branch based version control, and development version

### Issue 正文摘录

### Motivation. Currently, vLLM manages the release and development version all through the main branch: * `vllm.__version__ = A` while A is the current public version being released * When it is time to bump the version to B, a PR is submitted setting `vllm.__version__ = B`. * Then a git tag will be applied to that commit, or typically few hotfix commits later. * The git tag will be picked up by GitHub workflows and built wheels. * The git tag will also show up on the GitHub release page. It presents some challenges * At any given, the development version is equivalent to the released version * No branching meaning the main branch included some potentially hotfixes * Patch release becomes difficult as we always release from the main branch ### Proposed Change. I think this RFC is open for suggestions. One straw man proposal is as follows, which roughly follows the way in `ray-project/ray`: * Keep the version in the main branch `v0.k+1.0.dev0` where `k` is the current minor version * When it is time to cut a new release, the release manager creates a new branch and set the version to `v0.k.j`, creates the tag and cherry-pick any hot fixes. The downside of this approach is the cumb...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [RFC]: Branch based version control, and development version RFC;stale ### Motivation. Currently, vLLM manages the release and development version all through the main branch: * `vllm.__version__ = A` while A is the cur...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [RFC]: Branch based version control, and development version RFC;stale ### Motivation. Currently, vLLM manages the release and development version all through the main branch: * `vllm.__version__ = A` while A is the cur...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
