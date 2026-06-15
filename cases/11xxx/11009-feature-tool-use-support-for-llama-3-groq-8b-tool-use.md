# vllm-project/vllm#11009: [Feature]: Tool-use support for Llama-3-Groq-8B-Tool-Use

| 字段 | 值 |
| --- | --- |
| Issue | [#11009](https://github.com/vllm-project/vllm/issues/11009) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Tool-use support for Llama-3-Groq-8B-Tool-Use

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I am able to deploy https://huggingface.co/Groq/Llama-3-Groq-8B-Tool-Use using vllm but I cannot use its tool-use capabilities. It would be nice with a tool_chat_template that supports this. I have tested tool_chat_template_llama3.1_json.jinja which failed. I can see that Ollama has this template, maybe one can use that: https://ollama.com/library/llama3-groq-tool-use:8b/blobs/4d1abb94190b. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Tool-use support for Llama-3-Groq-8B-Tool-Use feature request;stale ### 🚀 The feature, motivation and pitch I am able to deploy https://huggingface.co/Groq/Llama-3-Groq-8B-Tool-Use using vllm but I cannot use...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Tool-use support for Llama-3-Groq-8B-Tool-Use feature request;stale ### 🚀 The feature, motivation and pitch I am able to deploy https://huggingface.co/Groq/Llama-3-Groq-8B-Tool-Use using vllm but I cannot use...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: s. It would be nice with a tool_chat_template that supports this. I have tested tool_chat_template_llama3.1_json.jinja which failed. I can see that Ollama has this template, maybe one can use that: https://ollama.com/li...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
