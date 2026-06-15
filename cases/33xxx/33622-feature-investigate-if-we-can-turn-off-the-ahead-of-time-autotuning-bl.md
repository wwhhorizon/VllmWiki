# vllm-project/vllm#33622: [Feature]: investigate if we can turn off the ahead-of-time autotuning block in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#33622](https://github.com/vllm-project/vllm/issues/33622) |
| 状态 | open |
| 标签 | feature request;torch.compile;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: investigate if we can turn off the ahead-of-time autotuning block in vLLM

### Issue 正文摘录

### 🚀 The feature, motivation and pitch This should make things less complicated. But we may have discussed this before and there may have been a good reason for it (I don't remember anymore). ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: te if we can turn off the ahead-of-time autotuning block in vLLM feature request;torch.compile;stale ### 🚀 The feature, motivation and pitch This should make things less complicated. But we may have discussed this befor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: urn off the ahead-of-time autotuning block in vLLM feature request;torch.compile;stale ### 🚀 The feature, motivation and pitch This should make things less complicated. But we may have discussed this before and there ma...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Feature]: investigate if we can turn off the ahead-of-time autotuning block in vLLM feature request;torch.compile;stale ### 🚀 The feature, motivation and pitch This should make things less complicated. But we may have...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
