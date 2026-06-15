# vllm-project/vllm#9110: [Feature]: LLMEngine and ModelConfig explicitly require path or HF model id, but no InferenceClient class for locally running VLLM server

| 字段 | 值 |
| --- | --- |
| Issue | [#9110](https://github.com/vllm-project/vllm/issues/9110) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: LLMEngine and ModelConfig explicitly require path or HF model id, but no InferenceClient class for locally running VLLM server

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I reviewed the code for LLMEngine and ModelConfig. It only allows you to load the model from huggingface hub or from a local directory. However, in my langchain app, I use LCEL to chain runnables together, and I want to be able to invoke my locally run vllm server. Because the VLLM class that implements BaseLLM uses "VLLModel" and that in turn depends on LLMEngine and ModelConfig, there is no way to use an InferenceClient, similar to how langchain_huggingface does it. I am ok to implement my own class for VLLM that implements langchain BaseLLM, but then I cannot use LLMEngine and ModelConfig at all and that removes the use of a ton of code. Aside from using OpenAI with VLLM, is there any plans to have an InferenceClient? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: LLMEngine and ModelConfig explicitly require path or HF model id, but no InferenceClient class for locally running VLLM server feature request ### 🚀 The feature, motivation and pitch I reviewed the code for L...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: LLMEngine and ModelConfig explicitly require path or HF model id, but no InferenceClient class for locally running VLLM server feature request ### 🚀 The feature, motivation and pitch I reviewed the code for L...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: id, but no InferenceClient class for locally running VLLM server feature request ### 🚀 The feature, motivation and pitch I reviewed the code for LLMEngine and ModelConfig. It only allows you to load the model from huggi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
