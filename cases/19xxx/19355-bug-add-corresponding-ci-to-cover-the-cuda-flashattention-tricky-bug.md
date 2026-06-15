# vllm-project/vllm#19355: [Bug]: Add corresponding CI to cover the CUDA + FlashAttention tricky bug

| 字段 | 值 |
| --- | --- |
| Issue | [#19355](https://github.com/vllm-project/vllm/issues/19355) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Add corresponding CI to cover the CUDA + FlashAttention tricky bug

### Issue 正文摘录

### Your current environment This is a follow up of https://github.com/vllm-project/vllm/pull/19321 We should introduce an appropriate test to ensure the logic is covered appropriately. ### 🐛 Describe the bug See some repro shape in https://gist.github.com/yinghai/4d72cb67a056a033a7a86e59d8051d90 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Add corresponding CI to cover the CUDA + FlashAttention tricky bug bug;stale ### Your current environment This is a follow up of https://github.com/vllm-project/vllm/pull/19321 We should introduce an appropriate...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: Add corresponding CI to cover the CUDA + FlashAttention tricky bug bug;stale ### Your current environment This is a follow up of https://github.com/vllm-project/vllm/pull/19321 We should introduce an appropriate...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: Add corresponding CI to cover the CUDA + FlashAttention tricky bug bug;stale ### Your current environment This is a follow up of https://github.com/vllm-project/vllm/pull/19321 We should introduce an appropriate...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: : Add corresponding CI to cover the CUDA + FlashAttention tricky bug bug;stale ### Your current environment This is a follow up of https://github.com/vllm-project/vllm/pull/19321 We should introduce an appropriate test...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: hub.com/vllm-project/vllm/pull/19321 We should introduce an appropriate test to ensure the logic is covered appropriately. ### 🐛 Describe the bug See some repro shape in https://gist.github.com/yinghai/4d72cb67a056a033a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
