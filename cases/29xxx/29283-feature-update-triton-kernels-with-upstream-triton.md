# vllm-project/vllm#29283: [Feature]: Update triton_kernels with upstream triton

| 字段 | 值 |
| --- | --- |
| Issue | [#29283](https://github.com/vllm-project/vllm/issues/29283) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Update triton_kernels with upstream triton

### Issue 正文摘录

### 🚀 The feature, motivation and pitch `triton_kernels` is a critical package and is used in vllm to support gpt-oss model. Currently, we pinned the `triton_kernels` version to the main triton release version to ensure compatibility. `triton_kernels` recently introduced [backward](https://github.com/triton-lang/triton/pull/8375)-[breaking](https://github.com/triton-lang/triton/pull/8765) changes that require vllm backend change. Ideally, we want to do that before pytorch 2.10 [release](https://dev-discuss.pytorch.org/t/pytorch-release-2-10-key-dates-updated/3259), so that we can update the `triton_kernels` package together with the triton/pytorch release ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Feature]: Update triton_kernels with upstream triton feature request;stale ### 🚀 The feature, motivation and pitch `triton_kernels` is a critical package and is used in vllm to support gpt-oss model. Currently, we pinn...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: h `triton_kernels` is a critical package and is used in vllm to support gpt-oss model. Currently, we pinned the `triton_kernels` version to the main triton release version to ensure compatibility. `triton_kernels` recen...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Update triton_kernels with upstream triton feature request;stale ### 🚀 The feature, motivation and pitch `triton_kernels` is a critical package and is used in vllm to support gpt-oss model. Currently, we pinn...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: vllm to support gpt-oss model. Currently, we pinned the `triton_kernels` version to the main triton release version to ensure compatibility. `triton_kernels` recently introduced [backward](https://github.com/triton-lang...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
