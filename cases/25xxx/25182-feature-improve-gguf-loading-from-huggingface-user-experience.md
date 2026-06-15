# vllm-project/vllm#25182: [Feature]: improve GGUF loading from HuggingFace user experience

| 字段 | 值 |
| --- | --- |
| Issue | [#25182](https://github.com/vllm-project/vllm/issues/25182) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: improve GGUF loading from HuggingFace user experience

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Something like `vllm serve unsloth/Qwen3-4B-Instruct-2507-GGUF:Q4_K_XL` should simply work, downloading the model from Huggingface automatically and caching it. Or maybe specifying it as `unsloth/Qwen3-4B-Instruct-2507-GGUF/Qwen3-4B-Instruct-2507-Q4_K_XL.gguf` (although I think this is less preferred). ### Alternatives _No response_ ### Additional context This is a followup to [#20084](https://github.com/vllm-project/vllm/issues/20084) and https://github.com/vllm-project/vllm/pull/20793 which I personally think are incomplete solutions and not what users expect from other projects like Llama.cpp, Ollama, etc. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: improve GGUF loading from HuggingFace user experience good first issue;feature request ### 🚀 The feature, motivation and pitch Something like `vllm serve unsloth/Qwen3-4B-Instruct-2507-GGUF:Q4_K_XL` should si...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ng the model from Huggingface automatically and caching it. Or maybe specifying it as `unsloth/Qwen3-4B-Instruct-2507-GGUF/Qwen3-4B-Instruct-2507-Q4_K_XL.gguf` (although I think this is less preferred). ### Alternatives...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: tc. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: st ### 🚀 The feature, motivation and pitch Something like `vllm serve unsloth/Qwen3-4B-Instruct-2507-GGUF:Q4_K_XL` should simply work, downloading the model from Huggingface automatically and caching it. Or maybe specif...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e GGUF loading from HuggingFace user experience good first issue;feature request ### 🚀 The feature, motivation and pitch Something like `vllm serve unsloth/Qwen3-4B-Instruct-2507-GGUF:Q4_K_XL` should simply work, downlo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
