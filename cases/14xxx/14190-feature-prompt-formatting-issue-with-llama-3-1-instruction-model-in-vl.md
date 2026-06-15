# vllm-project/vllm#14190: [Feature]: Prompt Formatting Issue with LLaMA 3.1 Instruction Model in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#14190](https://github.com/vllm-project/vllm/issues/14190) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Prompt Formatting Issue with LLaMA 3.1 Instruction Model in vLLM

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When running the LLaMA 3.1 instruction model with vLLM and passing inputs in ChatML style, I think there is an issue where the prompt format is not properly maintained for multi-turn conversations. Special tokens such as ` {role} \n\n{content} ` should be included in the prompt, but `tokenizer.chat_template` alone does not seem to enforce this format correctly. Relevant code: [chat_utils.py#L296](https://github.com/vllm-project/vllm/blob/f78c0be80a8341167a5ebf20ce4eb62421a351a6/vllm/entrypoints/chat_utils.py#L296) Reference: [LLaMA 3.1 Instruct Model Prompt Format](https://www.llama.com/docs/model-cards-and-prompt-formats/llama3_1/#-instruct-model-prompt-) Additionally, I understand that even in a single-turn scenario, when providing input to the LLaMA 3.1 instruction model in ChatML style, the format does not automatically convert to ` {role} \n\n{content}`. Is this behavior intentional? Thanks! ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](ht...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Prompt Formatting Issue with LLaMA 3.1 Instruction Model in vLLM feature request;stale ### 🚀 The feature, motivation and pitch When running the LLaMA 3.1 instruction model with vLLM and passing inputs in Chat...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Prompt Formatting Issue with LLaMA 3.1 Instruction Model in vLLM feature request;stale ### 🚀 The feature, motivation and pitch When running the LLaMA 3.1 instruction model with vLLM and passing inputs in ChatML style, I...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: pt format is not properly maintained for multi-turn conversations. Special tokens such as ` {role} \n\n{content} ` should be included in the prompt, but `tokenizer.chat_template` alone does not seem to enforce this form...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
