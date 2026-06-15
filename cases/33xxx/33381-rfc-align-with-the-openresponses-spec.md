# vllm-project/vllm#33381: [RFC]: Align with the openresponses spec.

| 字段 | 值 |
| --- | --- |
| Issue | [#33381](https://github.com/vllm-project/vllm/issues/33381) |
| 状态 | open |
| 标签 | RFC;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Align with the openresponses spec.

### Issue 正文摘录

### Motivation. Open Responses is an open-source specification for multi-provider, interoperable LLM interfaces inspired by the OpenAI Responses API. It defines a shared request/response model, streaming semantics, and tool invocation patterns so clients and providers can exchange structured inputs and outputs in a consistent shape. ref: https://www.openresponses.org ### Proposed Change. 1. Fully compatible with all fields of openresponses. 2. Pass the openresponses conformance tests. 3. Contribute some vLLM-specific fields currently in the responses API to the upstream. TODO: - [ ] Fields https://www.openresponses.org/reference - [ ] Acceptance Tests https://www.openresponses.org/compliance ### Feedback Period. _No response_ ### CC List. @yeqcharlotte @bbrowning @qandrew @simon-mo ### Any Other Things. Currently, many PRs are attempting to directly replicate the fields from the chat completion interface into the responses API. Instead of fully duplicating the chat completion interface, we should prioritize contributing these to the upstream or providing them through the openresponses extension mechanism. see: #33378 #32609 #33249 _No response_ ### Before submitting a new issue......

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: he upstream or providing them through the openresponses extension mechanism. see: #33378 #32609 #33249 _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and ask...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: Align with the openresponses spec. RFC;stale ### Motivation. Open Responses is an open-source specification for multi-provider, interoperable LLM interfaces inspired by the OpenAI Responses API. It defines a shar...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ses spec. RFC;stale ### Motivation. Open Responses is an open-source specification for multi-provider, interoperable LLM interfaces inspired by the OpenAI Responses API. It defines a shared request/response model, strea...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: spired by the OpenAI Responses API. It defines a shared request/response model, streaming semantics, and tool invocation patterns so clients and providers can exchange structured inputs and outputs in a consistent shape...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: with all fields of openresponses. 2. Pass the openresponses conformance tests. 3. Contribute some vLLM-specific fields currently in the responses API to the upstream. TODO: - [ ] Fields https://www.openresponses.org/ref...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
