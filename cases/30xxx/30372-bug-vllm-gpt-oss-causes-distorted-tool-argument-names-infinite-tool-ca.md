# vllm-project/vllm#30372: [Bug]: vLLM (GPT-OSS) causes distorted tool argument names + infinite tool-call loop with Korean messenger tool

| 字段 | 值 |
| --- | --- |
| Issue | [#30372](https://github.com/vllm-project/vllm/issues/30372) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;frontend_api;model_support |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM (GPT-OSS) causes distorted tool argument names + infinite tool-call loop with Korean messenger tool

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have two issues to report. The use case is: the user sends messages in Korean, and the model is supposed to call a custom tool. The tool format is something like: { "type": "messenger", "arguments": { "name": "...", "content": "..." } } The tool call itself works, but strange behavior occurs. 1. Parameter name distortion when using vLLM When running inference with the Transformers library, the tool call correctly uses the exact argument names: name and content. However, when using vLLM, the model outputs a tool call where the argument names become distorted — for example, changed into something that sounds similar to the Korean pronunciation, or mutated slightly. It still produces valid JSON/formatted calls, but with incorrect parameter names. 2. Infinite repeated tool-calling loop When consecutive tool calls occur, vLLM keeps invoking the same messenger tool repeatedly, with slightly changed content each time. This leads to an infinite tool-calling loop, and the conversation never terminates. Additional notes Outside of tool-calling, the model generates Korean normally. I’m unsure whether this is: model hallucination, or a vLL...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: r this is expected model behavior or a bug in vLLM’s tool-calling mechanism. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom righ...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: vLLM (GPT-OSS) causes distorted tool argument names + infinite tool-call loop with Korean messenger tool bug;stale ### Your current environment ### 🐛 Describe the bug I have two issues to report. The use case is:...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: example, changed into something that sounds similar to the Korean pronunciation, or mutated slightly. It still produces valid JSON/formatted calls, but with incorrect parameter names. 2. Infinite repeated tool-calling l...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: stions. correctness distributed_parallel;frontend_api;model_support cuda mismatch env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: argument names + infinite tool-call loop with Korean messenger tool bug;stale ### Your current environment ### 🐛 Describe the bug I have two issues to report. The use case is: the user sends messages in Korean, and the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
