# vllm-project/vllm#40554: [AMD][CI Failure][Tracker] Static dashboard tracker for current CI failures

| 字段 | 值 |
| --- | --- |
| Issue | [#40554](https://github.com/vllm-project/vllm/issues/40554) |
| 状态 | open |
| 标签 | rocm;ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [AMD][CI Failure][Tracker] Static dashboard tracker for current CI failures

### Issue 正文摘录

This is the single dashboard-managed umbrella issue for current AMD CI failures tracked by `AndreasKaratzas/vllm-ci-dashboard`. ## Rules - The dashboard automation updates only one managed comment on this issue. - The dashboard automation must not create or modify any other `vllm-project/vllm` issues. - Engineers should open separate manual issues when they pick up a specific failure to work on. - Those manual issues can move through [project #39](https://github.com/orgs/vllm-project/projects/39) and be referenced by the dashboard, but they are not edited by the dashboard automation. ## Engineer workflow - Check the managed comment on this issue for the latest failing groups. - Open a separate issue for any failure you pick up. - Move that separate issue through the appropriate [project #39](https://github.com/orgs/vllm-project/projects/39) column and assign an owner there. ## Ownership - Dashboard owner: `@AndreasKaratzas` - Repo: `AndreasKaratzas/vllm-ci-dashboard`

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: D][CI Failure][Tracker] Static dashboard tracker for current CI failures rocm;ci-failure This is the single dashboard-managed umbrella issue for current AMD CI failures tracked by `AndreasKaratzas/vllm-ci-dashboard`. ##...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [AMD][CI Failure][Tracker] Static dashboard tracker for current CI failures rocm;ci-failure This is the single dashboard-managed umbrella issue for current AMD CI failures tracked by `AndreasKaratzas/vllm-ci-dashboard`....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ## Engineer workflow - Check the managed comment on this issue for the latest failing groups. - Open a separate issue for any failure you pick up. - Move that separate issue through the appropriate [project #39](https:/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
