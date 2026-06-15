# vllm-project/vllm#43171: [Feature]: Add separate_reasoning option for OpenAI chat completion API

| 字段 | 值 |
| --- | --- |
| Issue | [#43171](https://github.com/vllm-project/vllm/issues/43171) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add separate_reasoning option for OpenAI chat completion API

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Problem Currently vLLM OpenAI-compatible chat completion responses expose reasoning separately: ```json { "message": { "reasoning": "...", "content": "..." } } ``` Some OpenAI-compatible clients, SDKs, and agent frameworks expect all generated text to appear in content only and do not parse the reasoning field. As a result, users currently need to add custom post-processing logic on the client side to merge reasoning back into content. ## Proposed feature Add a new optional request parameter: separate_reasoning: bool = True Behavior: separate_reasoning=True (default) Keep existing behavior Return reasoning and content separately ```json { "reasoning": "...", "content": "..." } ``` separate_reasoning=False Merge reasoning into content Suppress the reasoning field ```json { "content": " " } ``` ## Motivation This improves compatibility with: Existing OpenAI-compatible APIs SDKs and client libraries that only consume content Agent frameworks that do not understand a separate reasoning field Existing applications migrating to vLLM without additional response transformations ## Why this approach No breaking changes Default behavior remains unc...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: on { "reasoning": "...", "content": "..." } ``` separate_reasoning=False Merge reasoning into content Suppress the reasoning field ```json { "content": " " } ``` ## Motivation This improves compatibility with: Existing...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Existing applications migrating to vLLM without additional response transformations ## Why this approach No breaking changes Default behavior remains unchanged Requires minimal changes Applies consistently to both strea...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e]: Add separate_reasoning option for OpenAI chat completion API feature request ### 🚀 The feature, motivation and pitch ## Problem Currently vLLM OpenAI-compatible chat completion responses expose reasoning separately:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
