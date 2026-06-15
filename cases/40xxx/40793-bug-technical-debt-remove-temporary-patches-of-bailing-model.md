# vllm-project/vllm#40793: [Bug]: Technical Debt - Remove temporary patches of bailing model

| 字段 | 值 |
| --- | --- |
| Issue | [#40793](https://github.com/vllm-project/vllm/issues/40793) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Technical Debt - Remove temporary patches of bailing model

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Summary This issue tracks the technical debt created by temporary patches implemented in our vllm-ascend integration PR for the Baoling 2.6 model. https://github.com/vllm-project/vllm-ascend/pull/8657 These patches were added as emergency workarounds to address problematic code in the upstream vllm framework. This approach is not sustainable and needs to be addressed through proper upstream fixes followed by removal of the temporary patches. ## Background In our vllm-ascend integration PR, we had to introduce several patches to work around issues in the upstream vllm framework that were causing problems with Ascend hardware compatibility. While these patches allowed us to proceed with the integration, they represent technical debt that compromises code maintainability and creates potential future maintenance issues. ## Current State - Temporary patches have been applied to work around upstream vllm framework issues - The patches are not ideal long-term solutions - Code maintainability is reduced due to workarounds - Future updates from upstream vllm may break our patches ### Alternatives _No response_ ### Additional context _No response_...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Technical Debt - Remove temporary patches of bailing model feature request ### 🚀 The feature, motivation and pitch ## Summary This issue tracks the technical debt created by temporary patches implemented in our v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Bug]: Technical Debt - Remove temporary patches of bailing model feature request ### 🚀 The feature, motivation and pitch ## Summary This issue tracks the technical debt created by temporary patches implemented in our vl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
