# vllm-project/vllm#25670: [RFC]: Migration from buildkite to GHA

| 字段 | 值 |
| --- | --- |
| Issue | [#25670](https://github.com/vllm-project/vllm/issues/25670) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 27; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Migration from buildkite to GHA

### Issue 正文摘录

# Main motivation In order to increase the hardware offering and enable other organisations to easily offer computational capabilities for vLLM CI and benchmark, migrating to GitHub Actions is a smart choice: * Industry standard and widely used and supported; * Enable powerful monitoring tooling that already exists today; * Flexible reusable workflows enable the construction of sophisticated jobs that are fully human-readable and don't require automation tooling to generate workflows; * Organisations can easily contribute with compute, using [ARC](https://github.com/actions/actions-runner-controller) or [terraform-aws-github-runner](https://github.com/pytorch/test-infra/tree/main/terraform-aws-github-runner); * Simplification of current CI, easing onboarding of newer contributors; # Bonus content * Integrate vLLM on [HUD](https://hud.pytorch.org/) used for pytorch; * Enable DrCI, to automatically retry and flag flaky workflows; # The change ![Image](https://github.com/user-attachments/assets/7c46518a-a484-4c14-8c94-820ebc5c468b) The proposed change involves using reusable actions to perform common tasks like docker image builds / push / pulls and other common tasks. The main contr...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [RFC]: Migration from buildkite to GHA RFC;stale # Main motivation In order to increase the hardware offering and enable other organisations to easily offer computational capabilities for vLLM CI and benchmark, migratin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: capabilities for vLLM CI and benchmark, migrating to GitHub Actions is a smart choice: * Industry standard and widely used and supported; * Enable powerful monitoring tooling that already exists today; * Flexible reusab...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: organisations to easily offer computational capabilities for vLLM CI and benchmark, migrating to GitHub Actions is a smart choice: * Industry standard and widely used and supported; * Enable powerful monitoring tooling...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ** | Y | Y | *BuildKite supports by both dynamic workflows / plugins and blocked workflows that can be unblocked; GHA uses conditionals: trigger conditionals and steps / flows conditionals.* | | **Strong marketplace of...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [RFC]: Migration from buildkite to GHA RFC;stale # Main motivation In order to increase the hardware offering and enable other organisations to easily offer computational capabilities for vLLM CI and benchmark, migratin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
