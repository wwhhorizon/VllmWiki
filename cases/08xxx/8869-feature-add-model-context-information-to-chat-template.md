# vllm-project/vllm#8869: [Feature]: Add model context information to chat template

| 字段 | 值 |
| --- | --- |
| Issue | [#8869](https://github.com/vllm-project/vllm/issues/8869) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add model context information to chat template

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I'm currently working on tool use PRs and I'm seeing that some models are very sensitive to the given prompt. So it would be nice to be able to detect what model is being used in the chat template and adjust the input accordingly. For example, in LLama 3.1 the model seems to perform better if the tool list is passed in the first user message, whereas Llama 3.2 seems to prefer the tools to be in the system prompt. In the llama chat template this behavior is controlled by the `tools_in_user_message` flag that can be passed in the `tokenizer.apply_chat_template()` call: ``` {%- if not tools_in_user_message is defined %} {%- set tools_in_user_message = false %} {%- endif %} ``` Passing extra flags is already supported in the vllm's version of the OpenAI API using the `chat_template_kwargs` field in the request JSON, but this is not supported in the `openai` client library, making it hard to use. Therefore, it would be nice if we could have extra context inserted in the chat template to conditionally create different prompts. To illustrate the idea, here is a simplistic PoC that adds the model name as a variable passed to the chat template: ``` $...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: Add model context information to chat template feature request;stale ### 🚀 The feature, motivation and pitch I'm currently working on tool use PRs and I'm seeing that some models are very sensitive to the giv...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add model context information to chat template feature request;stale ### 🚀 The feature, motivation and pitch I'm currently working on tool use PRs and I'm seeing that some models are very sensitive to the giv...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: {%- endif %} ``` Passing extra flags is already supported in the vllm's version of the OpenAI API using the `chat_template_kwargs` field in the request JSON, but this is not supported in the `openai` client library, mak...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ools_in_user_message is defined %} {%- set tools_in_user_message = false %} {%- endif %} ``` Passing extra flags is already supported in the vllm's version of the OpenAI API using the `chat_template_kwargs` field in the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
