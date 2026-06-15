# vllm-project/vllm#35779: [Bug]: Harmony models incorrectly drops prior-turn analysis channel in multi-turn conversations

| 字段 | 值 |
| --- | --- |
| Issue | [#35779](https://github.com/vllm-project/vllm/issues/35779) |
| 状态 | open |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Harmony models incorrectly drops prior-turn analysis channel in multi-turn conversations

### Issue 正文摘录

### Your current environment Dynamo V0.9.0 + vLLM V0.14.1 The current main have same logic on dropping analysis channel for chat completions for harmony models with the above tag release. ### 🐛 Describe the bug `auto_drop_analysis_messages` in `harmony_utils.py` currently drops all analysis channel messages from prior turns once a final channel is formed when processing multi-turn Chat Completion requests: https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/openai/parser/harmony_utils.py#L175 This prevents clients from preserving reasoning context across conversation turns - the model cannot see its own prior reasoning even when the client explicitly provides reasoning_content on assistant messages. This can lead to incorrect or repeated reasoning. In the following multi-turn Chat Completion example where the assistant's prior reasoning_content contains a fact not present in content: ``` curl http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "example-model", "messages": [ { "role": "user", "content": "Pick a secret number between 1 and 1000. Only think about it, do not reveal it." }, { "role": "assistant", "content": "OK,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: - the model cannot see its own prior reasoning even when the client explicitly provides reasoning_content on assistant messages. This can lead to incorrect or repeated reasoning. In the following multi-turn Chat Complet...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: el. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Harmony models incorrectly drops prior-turn analysis channel in multi-turn conversations bug ### Your current environment Dynamo V0.9.0 + vLLM V0.14.1 The current main have same logic on dropping analysis channel...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nce a final channel is formed when processing multi-turn Chat Completion requests: https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/openai/parser/harmony_utils.py#L175 This prevents clients from preservin...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
