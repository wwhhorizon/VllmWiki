# vllm-project/vllm#17720: [RFC]: Enabling Arm Neoverse CI Runners

| 字段 | 值 |
| --- | --- |
| Issue | [#17720](https://github.com/vllm-project/vllm/issues/17720) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Enabling Arm Neoverse CI Runners

### Issue 正文摘录

### Motivation. Add Arm Neoverse runners to the vLLM CI fleet so that every change is automatically built, tested, and benchmarked on Arm hardware. **Motivations** - Confidence on Arm: Current CI does not cover Arm, leaving Arm changes un-validated until after merge. - Faster feedback: Contributors can catch functional or performance regressions early. - Broader adoption: Ensures vLLM remains stable for the growing Arm cloud/server ecosystem. ### Proposed Change. Hello vLLM Team, Arm would like to support the vLLM project by enabling Arm Neoverse CI runners. Currently, there are no Arm-based runners available, which poses a challenge for testing and validating Arm-specific contributions. Enabling these runners would improve the stability and confidence in community-driven changes targeting Arm platforms. As part of this initiative: - We will try to provision a set of Arm Neoverse CI runners for use by the vLLM project. - We will coordinate with the vLLM CI team to hand off access and support integration into the existing CI setup. We would appreciate your input on the following: - Feedback from the vLLM team on this proposal. - Any potential blockers or requirements you foresee fo...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: unners to the vLLM CI fleet so that every change is automatically built, tested, and benchmarked on Arm hardware. **Motivations** - Confidence on Arm: Current CI does not cover Arm, leaving Arm changes un-validated unti...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: Enabling Arm Neoverse CI Runners RFC;stale ### Motivation. Add Arm Neoverse runners to the vLLM CI fleet so that every change is automatically built, tested, and benchmarked on Arm hardware. **Motivations** - Con...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [RFC]: Enabling Arm Neoverse CI Runners RFC;stale ### Motivation. Add Arm Neoverse runners to the vLLM CI fleet so that every change is automatically built, tested, and benchmarked on Arm hardware. **Motivations** - Con...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: lowing: - Feedback from the vLLM team on this proposal. - Any potential blockers or requirements you foresee for enabling this integration. We’re excited to collaborate and help improve cross-platform support for vLLM....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
