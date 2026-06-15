# vllm-project/vllm#16430: [Bug]: Qwen2.5 assistant output on tool call is empty

| 字段 | 值 |
| --- | --- |
| Issue | [#16430](https://github.com/vllm-project/vllm/issues/16430) |
| 状态 | closed |
| 标签 | bug;stale;tool-calling |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5 assistant output on tool call is empty

### Issue 正文摘录

### Your current environment Latest vLLM (dev) and Pydantic AI version ### 🐛 Describe the bug I'm using pydantic ai for agents and tool calling, but I'm not sure what update has broken broken agentic functionality. The tool gets called (yes it does get called) but then it gets called and called again until it's out of context window size. When looking at the traces, Qwen2.5 says nothing after a tool call, and tries to call the tool again. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: -calling ### Your current environment Latest vLLM (dev) and Pydantic AI version ### 🐛 Describe the bug I'm using pydantic ai for agents and tool calling, but I'm not sure what update has broken broken agentic functional...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: n. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Qwen2.5 assistant output on tool call is empty bug;stale;tool-calling ### Your current environment Latest vLLM (dev) and Pydantic AI version ### 🐛 Describe the bug I'm using pydantic ai for agents and tool callin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Qwen2.5 assistant output on tool call is empty bug;stale;tool-calling ### Your current environment Latest vLLM (dev) and Pydantic AI version ### 🐛 Describe the bug I'm using pydantic ai for agents and tool callin...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ool call is empty bug;stale;tool-calling ### Your current environment Latest vLLM (dev) and Pydantic AI version ### 🐛 Describe the bug I'm using pydantic ai for agents and tool calling, but I'm not sure what update has...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
