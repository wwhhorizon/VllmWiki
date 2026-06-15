# vllm-project/vllm#33229: [Bug]: vllm v0.14.0 GGUF model with architecture minimax-m2 is not supported yet

| 字段 | 值 |
| --- | --- |
| Issue | [#33229](https://github.com/vllm-project/vllm/issues/33229) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm v0.14.0 GGUF model with architecture minimax-m2 is not supported yet

### Issue 正文摘录

### Your current environment ## Docker `vllm/vllm-openai:v0.14.0` ### 🐛 Describe the bug ```shell vllm serve /unsloth/MiniMax-M2.1-GGUF/UD-IQ2_M/MiniMax-M2.1-UD-IQ2_M-00001-of-00002.gguf \ --host 0.0.0.0 \ --port 8000 \ --max-model-len auto \ --enable-auto-tool-choice ``` ```shell ValueError: GGUF model with architecture minimax-m2 is not supported yet. ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nimax-m2 is not supported yet bug;stale ### Your current environment ## Docker `vllm/vllm-openai:v0.14.0` ### 🐛 Describe the bug ```shell vllm serve /unsloth/MiniMax-M2.1-GGUF/UD-IQ2_M/MiniMax-M2.1-UD-IQ2_M-00001-of-000...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug]: vllm v0.14.0 GGUF model with architecture minimax-m2 is not supported yet bug;stale ### Your current environment ## Docker `vllm/vllm-openai:v0.14.0` ### 🐛 Describe the bug ```shell vllm serve /unsloth/MiniMax-M2...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: llm/vllm-openai:v0.14.0` ### 🐛 Describe the bug ```shell vllm serve /unsloth/MiniMax-M2.1-GGUF/UD-IQ2_M/MiniMax-M2.1-UD-IQ2_M-00001-of-00002.gguf \ --host 0.0.0.0 \ --port 8000 \ --max-model-len auto \ --enable-auto-too...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: vllm v0.14.0 GGUF model with architecture minimax-m2 is not supported yet bug;stale ### Your current environment ## Docker `vllm/vllm-openai:v0.14.0` ### 🐛 Describe the bug ```shell vllm serve /unsloth/MiniMax-M2...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: v0.14.0 GGUF model with architecture minimax-m2 is not supported yet bug;stale ### Your current environment ## Docker `vllm/vllm-openai:v0.14.0` ### 🐛 Describe the bug ```shell vllm serve /unsloth/MiniMax-M2.1-GGUF/UD-I...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
