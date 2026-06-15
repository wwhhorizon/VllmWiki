# vllm-project/vllm#14107: [Feature]: Added the parameter to specify a device for the speculative model when using speculative decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#14107](https://github.com/vllm-project/vllm/issues/14107) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Added the parameter to specify a device for the speculative model when using speculative decoding

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In most cases, the speculative model has a smaller number of parameters. If deployed on a specific device, maybe the inter-GPU communication of the speculative model can be reduced? And reduce the impact on the main model (if any). ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Added the parameter to specify a device for the speculative model when using speculative decoding feature request;stale ### 🚀 The feature, motivation and pitch In most cases, the speculative model has a small...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: eature, motivation and pitch In most cases, the speculative model has a smaller number of parameters. If deployed on a specific device, maybe the inter-GPU communication of the speculative model can be reduced? And redu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: Added the parameter to specify a device for the speculative model when using speculative decoding feature request;stale ### 🚀 The feature, motivation and pitch In most cases, the speculative model has a small...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Added the parameter to specify a device for the speculative model when using speculative decoding feature request;stale ### 🚀 The feature, motivation and pitch In most cases, the speculative model has a small...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
