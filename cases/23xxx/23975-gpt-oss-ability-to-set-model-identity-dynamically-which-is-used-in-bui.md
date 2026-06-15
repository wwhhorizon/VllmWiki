# vllm-project/vllm#23975: [gpt-oss]: Ability to set model_identity dynamically which is used in building the system prompt

| 字段 | 值 |
| --- | --- |
| Issue | [#23975](https://github.com/vllm-project/vllm/issues/23975) |
| 状态 | closed |
| 标签 | feature request;stale;gpt-oss |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [gpt-oss]: Ability to set model_identity dynamically which is used in building the system prompt

### Issue 正文摘录

### 🚀 The feature, motivation and pitch GPT-OSS's chat template offers flexibility in defining a model identity, which is used when assembling the system prompt. Please let me know if I've overlooked the ability to set this, but I don't believe vLLM offers the ability for this to be set from an individual request. We should enable to the user to set the model identity and potentially offer more flexibility for unique fields in chat templates going forward. https://huggingface.co/openai/gpt-oss-120b/blob/main/chat_template.jinja#L197 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [gpt-oss]: Ability to set model_identity dynamically which is used in building the system prompt feature request;stale;gpt-oss ### 🚀 The feature, motivation and pitch GPT-OSS's chat template offers flexibility in definin
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: identity dynamically which is used in building the system prompt feature request;stale;gpt-oss ### 🚀 The feature, motivation and pitch GPT-OSS's chat template offers flexibility in defining a model identity, which is us...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [gpt-oss]: Ability to set model_identity dynamically which is used in building the system prompt feature request;stale;gpt-oss ### 🚀 The feature, motivation and pitch GPT-OSS's chat template offers flexibility in defini...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
