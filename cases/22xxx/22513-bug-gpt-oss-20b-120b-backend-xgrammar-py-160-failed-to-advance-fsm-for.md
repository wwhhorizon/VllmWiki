# vllm-project/vllm#22513: [Bug]: GPT-OSS 20b/120b [backend_xgrammar.py:160] Failed to advance FSM for request

| 字段 | 值 |
| --- | --- |
| Issue | [#22513](https://github.com/vllm-project/vllm/issues/22513) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GPT-OSS 20b/120b [backend_xgrammar.py:160] Failed to advance FSM for request

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I got issue `[backend_xgrammar.py:160] Failed to advance FSM for request` both gpt-oss 20b (a single H100) and gpt-oss 120b (2 H200 GPUs). I use docker image `vllm-openai:gptoss` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: GPT-OSS 20b/120b [backend_xgrammar.py:160] Failed to advance FSM for request bug ### Your current environment ### 🐛 Describe the bug I got issue `[backend_xgrammar.py:160] Failed to advance FSM for request` both...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: GPT-OSS 20b/120b [backend_xgrammar.py:160] Failed to advance FSM for request bug ### Your current environment ### 🐛 Describe the bug I got issue `[backend_xgrammar.py:160] Failed to advance FSM for request` both...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ` both gpt-oss 20b (a single H100) and gpt-oss 120b (2 H200 GPUs). I use docker image `vllm-openai:gptoss` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the cha...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: GPT-OSS 20b/120b [backend_xgrammar.py:160] Failed to advance FSM for request bug ### Your current environment ### 🐛 Describe the bug I got issue `[backend_xgrammar.py:160] Failed to advance FSM for request` both...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: g]: GPT-OSS 20b/120b [backend_xgrammar.py:160] Failed to advance FSM for request bug ### Your current environment ### 🐛 Describe the bug I got issue `[backend_xgrammar.py:160] Failed to advance FSM for request` both gpt...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
